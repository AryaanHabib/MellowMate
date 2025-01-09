import React, { useState, useEffect } from 'react';
import { sendMessage } from '../services/api';
import './Chat.css';

const Chat: React.FC = () => {
  const [messages, setMessages] = useState<{ user: string; bot: string }[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchChatHistory = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/chat/history/');
        if (response.ok) {
          const history = await response.json();
          const formattedHistory = history.map((msg: any) => ({
            user: msg.role === 'user' ? msg.content : '',
            bot: msg.role === 'assistant' ? msg.content : '',
          }));
          setMessages(formattedHistory);
        }
      } catch (error) {
        console.error('Failed to fetch chat history:', error);
      }
    };

    fetchChatHistory();
  }, []);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = input;
    setMessages((prev) => [...prev, { user: userMessage, bot: '' }]);
    setLoading(true);

    try {
      const response = await sendMessage(userMessage);
      setMessages((prev) => [
        ...prev.slice(0, -1),
        { user: userMessage, bot: response.message },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev.slice(0, -1),
        { user: userMessage, bot: 'Failed to connect to backend.' },
      ]);
    } finally {
      setLoading(false);
    }

    setInput('');
  };

  return (
    <div className="chat-container">
      <h2 className="chat-header">Chat with MellowMate</h2>
      <div className="chat-messages">
        {messages.map((msg, index) => (
          <div key={index} className="message-group">
            <div className="message user-message">{msg.user}</div>
            <div className="message bot-message">{msg.bot}</div>
          </div>
        ))}
        {loading && (
          <div className="typing-indicator">
            <div className="dot"></div>
            <div className="dot"></div>
            <div className="dot"></div>
          </div>
        )}
      </div>
      <div className="chat-input">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
};

export default Chat;
