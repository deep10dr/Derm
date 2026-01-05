
   
   import { Link } from "react-router-dom";



export default function Home() {
  return (
   <div className="w-full h-screen  bg-cover bg-no-repeat bg-fixed flex flex-col items-center justify-center text-black">

    
  
      <h1 className="text-4xl font-bold">welcome </h1><br></br>
        
      <h1 className="text-4xl font-bold">  Skin Disease Analysis!</h1><br></br>

      <img src="/welcomeImage.png" alt="Welcome" className="w-1/5 rounded-lg shadow-lg mb-6" />

      <h2 className="text-3xl font-normal">AI-driven skin disease detection through image-based analysis... </h2>
      <br></br>
      <br></br>

      <Link to="/skinScan">
        <button style={{border:"2px solid", width:"150px" , height:"25px",borderRadius:"5px ", backgroundColor:"blue" ,fontSize:"20px"}}>
              Get Started
        </button>
    </Link>
    
        
    </div>
  )
 
  
}
