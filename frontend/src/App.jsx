import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import SkinScan from "./pages/SkinScan";
 import ResultPage from "./pages/ResultPage";

function App() {
  return (
    
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/skinScan" element={<SkinScan />} />
      <Route path="/resultPage" element={<ResultPage />} />
    </Routes>
    
  );
}

export default App;
