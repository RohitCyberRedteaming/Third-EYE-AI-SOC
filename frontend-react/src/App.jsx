import { useState } from "react";
import Login from "./Login";

function App(){

  const [auth, setAuth] = useState(false);
  const [token, setToken] = useState("");
  const [role, setRole] = useState("");

  if(!auth){
    return <Login setAuth={setAuth} setToken={setToken} setRole={setRole}/>
  }

  return (
    <div style={{display:"flex", color:"white", padding:"20px"}}>
      <div style={{width:"250px"}}>
        <h3>👁️ Third EYE</h3>
        <p>Role: {role}</p>
      </div>

      <div>
        <h2>AI SOC Assistant</h2>
      </div>
    </div>
  );
}

export default App;
