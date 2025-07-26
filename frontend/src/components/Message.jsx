import React from "react";

export default function Message({ message }) {
  const isUser = message.sender === "user";
  return (
    <div className={`text-white p-2 rounded ${isUser ? "bg-blue-500 self-end" : "bg-gray-700 self-start"}`}>
      {message.text}
    </div>
  );
}
