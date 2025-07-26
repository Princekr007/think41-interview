import React from "react";
import MessageList from "./MessageList";
import UserInput from "./UserInput";

export default function ChatWindow({ messages, onSend }) {
  return (
    <div className="flex flex-col h-screen">
      <div className="flex-1 overflow-y-auto">
        <MessageList messages={messages} />
      </div>
      <UserInput onSend={onSend} />
    </div>
  );
}
