import { useRef, useState } from "react";
import { Link } from "react-router-dom";

export default function SkinScan() {
  const fileInputRef = useRef(null);

  const [uploaded, setUploaded] = useState(false);
  const [analyzing, setAnalyzing] = useState(false);
  const [image, setImage] = useState(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setImage(URL.createObjectURL(file));
      setUploaded(true);
      setAnalyzing(false);
    }
  };

  const handleAnalyze = () => {
    if (!uploaded) return;
    setAnalyzing(true);
  };

  return (
    <div className="w-full min-h-screen flex flex-col items-center pt-10 gap-5 text-black">

      {/* Title */}
      <h1 className="text-3xl font-black">Skin Analysis</h1>

      {/* Illustration */}
      <img
        src="/SkinAnalysisImage.png"
        alt="Skin Analysis"
        className="w-80 h-60 object-contain"
      />

      {/* Upload heading */}
      <h2 className="text-2xl font-semibold">Upload a Photo</h2>

      <p className="text-lg font-medium text-center">
        Take a clear photo or upload from your gallery
      </p>

      {/* Upload box */}
      <div
        onClick={() => fileInputRef.current.click()}
        className="
          w-[320px] h-[220px]
          border-2 border-dashed border-black
          flex flex-col items-center justify-center gap-3
          bg-blue-100 rounded-xl
          cursor-pointer hover:bg-blue-200 transition
        "
      >
        {!uploaded ? (
          <>
            <img
              src="/cameraImage.png"
              alt="Camera"
              className="w-10 h-10 object-contain"
            />

            <span className="font-bold">Tap to Upload Image</span>

            <p className="text-sm text-gray-600">
              Supported formats: JPEG, PNG
            </p>
          </>
        ) : (
          <span className="text-sm text-green-600 font-semibold">
            Uploaded Successfully ✅
          </span>
        )}

        <input
          type="file"
          ref={fileInputRef}
          className="hidden"
          accept="image/*"
          onChange={handleFileChange}
        />
      </div>

      {/* Analyze Button */}
      <Link to="/resultPage" state={{ image }}>
        <button
          onClick={handleAnalyze}
          disabled={!uploaded}
          className={`
            px-10 py-4 text-xl font-bold rounded-xl
            ${
              uploaded
                ? "bg-blue-500 text-white hover:bg-blue-600"
                : "bg-gray-300 text-gray-500 cursor-not-allowed"
            }
          `}
        >
          Analyze Image
        </button>
      </Link>

      {/* Analyzing text */}
      {analyzing && (
        <h1 className="text-xl font-bold text-blue-600">
          Analysing Image...
        </h1>
      )}
    </div>
  );
}
