import React, { useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch("http://127.0.0.1:5000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query }),
    });
    const data = await res.json();
    setResponse(typeof data.response === "string" ? data.response : JSON.stringify(data.response, null, 2));
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>🛍️ E-commerce Support Chatbot</h1>
      <form onSubmit={handleSubmit} style={{ marginBottom: "1rem" }}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask me something..."
          style={{ width: "300px", padding: "0.5rem", marginRight: "1rem" }}
        />
        <button type="submit" style={{ padding: "0.5rem 1rem" }}>Send</button>
      </form>
      <pre style={{ background: "#f4f4f4", padding: "1rem", whiteSpace: "pre-wrap" }}>
        {response}
      </pre>
    </div>
  );
}

export default App;
