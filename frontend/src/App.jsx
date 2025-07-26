// src/App.jsx
import React, { useState, useEffect } from 'react';
import MessageList from './components/MessageList';
import ChatWindow from './components/ChatWindow';
import UserInput from './components/UserInput';


function App() {
  const [messages, setMessages] = useState([]);

  const handleNewMessage = (message) => {
    setMessages((prev) => [...prev, message]);
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white flex items-center justify-center p-4">
      <ChatWindow messages={messages} onMessageSend={handleNewMessage} />
    </div>
  );
}

export default App;
