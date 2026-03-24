import { useState } from "react";
import axios from "axios";

export default function Login({setAuth, setToken, setRole}) {

  const [user, setUser] = useState("");

  const login = async () => {

    const res = await axios.post("http://localhost:8000/login", {
      username: user
    });

    setToken(res.data.token);
    setRole(res.data.role);
    setAuth(true);
  };

  return (
    <div style={{color:"white"}}>
      <h2>Login</h2>
      <input onChange={(e)=>setUser(e.target.value)} />
      <button onClick={login}>Login</button>
    </div>
  );
}
