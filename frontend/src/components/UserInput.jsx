import React, { useState } from "react";

const UserInput = ({ onSend }) => {
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (input.trim() !== "") {
      onSend(input);
      setInput(""); // Clear input after sending
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      handleSend();
    }
  };

  return (
    <div className="flex items-center space-x-2">
      <input
        type="text"
        placeholder="Type your message..."
        className="flex-1 border rounded p-2"
        value={input}
        onChange={(e) => setInput(e.target.value)} // <-- This line is IMPORTANT
        onKeyDown={handleKeyPress}
      />
      <button
        onClick={handleSend}
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        Send
      </button>
    </div>
  );
};

export default UserInput;
