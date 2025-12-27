import torch
import torch.nn as nn
import timm
import json
from torchvision import models, transforms
from PIL import Image


MODEL_PATH = "./artifacts/best_cnn_vit_skin_model.pth"
CLASSES_PATH = "./classes.json"
IMAGE_SIZE = 224


class CNN_ViT(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.cnn = models.resnet18(pretrained=False)
        self.cnn.fc = nn.Identity()

        self.vit = timm.create_model(
            "vit_tiny_patch16_224", pretrained=False, num_classes=0
        )

        self.classifier = nn.Sequential(
            nn.Linear(512 + self.vit.num_features, 512),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(512, num_classes),
        )

    def forward(self, x):
        cnn_feat = self.cnn(x)
        vit_feat = self.vit(x)
        return self.classifier(torch.cat((cnn_feat, vit_feat), dim=1))


device = "cuda" if torch.cuda.is_available() else "cpu"

with open(CLASSES_PATH) as f:
    CLASSES = json.load(f)

MODEL = CNN_ViT(len(CLASSES)).to(device)
MODEL.load_state_dict(torch.load(MODEL_PATH, map_location=device))
MODEL.eval()

TRANSFORM = transforms.Compose(
    [
        transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)


def predict_disease(image_path: str):
    """
    Args:
        image_path (str): Path to skin image
    Returns:
        disease (str), confidence (float)
    """
    image = Image.open(image_path).convert("RGB")
    x = TRANSFORM(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = MODEL(x)
        probs = torch.softmax(outputs, dim=1)
        conf, pred = torch.max(probs, dim=1)

    disease = CLASSES[pred.item()]
    confidence = conf.item() * 100

    return disease, confidence
