import { useState } from "react";
import Login from "./Login";

function App() {
  const [auth, setAuth] = useState(false);
  const [token, setToken] = useState("");
  const [role, setRole] = useState("");
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [stats, setStats] = useState({ critical: 0, medium: 0, low: 0 });

  // 🔹 Backend URLs (FastAPI 5175)
  const LOGIN_URL = "http://localhost:5175/login";
  const AI_URL = "http://localhost:5175/ai-secure";

  // 💬 CHAT FUNCTION
  const send = async () => {
    if (!input) return;

    try {
      const res = await fetch(AI_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ token: token, query: input }),
      });

      const data = await res.json();

      setMessages([
        ...messages,
        { role: "user", text: input },
        { role: "ai", text: data.response },
      ]);

      setInput("");
    } catch (err) {
      alert("Error connecting to backend. Make sure backend port 5175 is running.");
      console.error(err);
    }
  };

  // 🔐 LOGIN SUCCESS CALLBACK
  const onLoginSuccess = (loginToken, loginRole) => {
    setToken(loginToken);
    setRole(loginRole);
    setAuth(true);

    // Fake stats for now
    setStats({ critical: 5, medium: 8, low: 12 });
  };

  if (!auth) {
    return (
      <Login
        setAuth={setAuth}
        setToken={setToken}
        setRole={setRole}
        onLoginSuccess={onLoginSuccess}
        LOGIN_URL={LOGIN_URL}
      />
    );
  }

  return (
    <div style={{ display: "flex", color: "white", background: "#020617", minHeight: "100vh" }}>
      {/* Sidebar */}
      <div style={{ width: "250px", padding: "20px", background: "#0f172a" }}>
        <h3>👁️ Third EYE</h3>
        <p>Role: {role}</p>
        <hr />
        <h4>📊 SOC Stats</h4>
        <p>🚨 Critical: {stats.critical}</p>
        <p>⚠️ Medium: {stats.medium}</p>
        <p>ℹ️ Low: {stats.low}</p>
      </div>

      {/* Main Panel */}
      <div style={{ flex: 1, padding: "20px" }}>
        <h2>AI SOC Assistant</h2>

        {/* Chat Window */}
        <div
          style={{
            height: "300px",
            overflowY: "auto",
            background: "#111827",
            padding: "10px",
            borderRadius: "10px",
          }}
        >
          {messages.map((m, i) => (
            <div
              key={i}
              style={{
                textAlign: m.role === "user" ? "right" : "left",
                margin: "10px",
              }}
            >
              <b>{m.role === "user" ? "You" : "AI"}:</b> {m.text}
            </div>
          ))}
        </div>

        {/* Input */}
        <div style={{ marginTop: "10px" }}>
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask SOC..."
            style={{ width: "70%", padding: "10px" }}
          />
          <button onClick={send} style={{ padding: "10px", marginLeft: "10px" }}>
            Send
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;