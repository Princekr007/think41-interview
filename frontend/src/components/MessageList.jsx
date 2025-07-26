import React from "react";
import Message from "./Message";

export default function MessageList({ messages }) {
  return (
    <div className="p-4 space-y-2">
      {messages.map((msg, index) => (
        <Message key={index} message={msg} />
      ))}
    </div>
  );
}
