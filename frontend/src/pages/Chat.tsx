import React, { useState, useRef, useEffect } from 'react';
import api from '../api';
import ProductCard from '../components/ProductCard';
import { Send, User, Bot } from 'lucide-react';

interface Message {
    role: 'user' | 'assistant';
    content: string;
    recommendations?: any[];
}

const Chat: React.FC = () => {
    const [messages, setMessages] = useState<Message[]>([
        { role: 'assistant', content: 'Hello! I am your AI shopping assistant. How can I help you find the perfect product today?' }
    ]);
    const [input, setInput] = useState('');
    const [loading, setLoading] = useState(false);
    const messagesEndRef = useRef<HTMLDivElement>(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    };

    useEffect(scrollToBottom, [messages]);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!input.trim()) return;

        const userMessage = input;
        setInput('');
        setMessages(prev => [...prev, { role: 'user', content: userMessage }]);
        setLoading(true);

        try {
            const response = await api.post('/chat', { query: userMessage });
            setMessages(prev => [
                ...prev,
                {
                    role: 'assistant',
                    content: response.data.message,
                    recommendations: response.data.recommended_products
                }
            ]);
        } catch (error) {
            console.error('Error sending message:', error);
            setMessages(prev => [
                ...prev,
                { role: 'assistant', content: 'Sorry, I encountered an error. Please try again.' }
            ]);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="max-w-4xl mx-auto px-4 py-8 h-[calc(100vh-4rem)] flex flex-col">
            <div className="flex-1 overflow-y-auto space-y-6 mb-6 pr-2">
                {messages.map((msg, index) => (
                    <div key={index} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                        <div className={`flex max-w-[80%] ${msg.role === 'user' ? 'flex-row-reverse' : 'flex-row'}`}>
                            <div className={`flex-shrink-0 h-10 w-10 rounded-full flex items-center justify-center ${msg.role === 'user' ? 'bg-indigo-600 ml-3' : 'bg-gray-200 mr-3'}`}>
                                {msg.role === 'user' ? <User className="text-white h-6 w-6" /> : <Bot className="text-gray-600 h-6 w-6" />}
                            </div>
                            <div className={`rounded-lg p-4 ${msg.role === 'user' ? 'bg-indigo-600 text-white' : 'bg-white shadow-md text-gray-900'}`}>
                                <div className="whitespace-pre-wrap">{msg.content}</div>
                                {msg.recommendations && msg.recommendations.length > 0 && (
                                    <div className="mt-4 space-y-4">
                                        <p className="font-medium text-sm opacity-90">Recommended Products:</p>
                                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                            {msg.recommendations.map((product) => (
                                                <ProductCard key={product.id} product={product} />
                                            ))}
                                        </div>
                                    </div>
                                )}
                            </div>
                        </div>
                    </div>
                ))}
                {loading && (
                    <div className="flex justify-start">
                        <div className="bg-gray-200 rounded-lg p-4 ml-13">
                            <div className="flex space-x-2">
                                <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce"></div>
                                <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce delay-100"></div>
                                <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce delay-200"></div>
                            </div>
                        </div>
                    </div>
                )}
                <div ref={messagesEndRef} />
            </div>

            <form onSubmit={handleSubmit} className="relative">
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Ask for recommendations (e.g., 'I have dry scalp')..."
                    className="w-full rounded-lg border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 py-4 pl-4 pr-12 text-gray-900 border"
                    disabled={loading}
                />
                <button
                    type="submit"
                    disabled={loading || !input.trim()}
                    className="absolute right-2 top-2 bottom-2 bg-indigo-600 text-white p-2 rounded-md hover:bg-indigo-700 disabled:opacity-50 transition-colors"
                >
                    <Send className="h-5 w-5" />
                </button>
            </form>
        </div>
    );
};

export default Chat;
