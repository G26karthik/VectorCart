import React from 'react';
import { Link } from 'react-router-dom';
import { MessageCircle, ShoppingBag } from 'lucide-react';

const Navbar: React.FC = () => {
    return (
        <nav className="bg-white shadow-sm sticky top-0 z-50">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex justify-between h-16">
                    <div className="flex">
                        <Link to="/" className="flex-shrink-0 flex items-center">
                            <ShoppingBag className="h-8 w-8 text-indigo-600" />
                            <span className="ml-2 text-xl font-bold text-gray-900">VectorCart</span>
                        </Link>
                    </div>
                    <div className="flex items-center">
                        <Link
                            to="/"
                            className="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium"
                        >
                            Home
                        </Link>
                        <Link
                            to="/chat"
                            className="ml-4 flex items-center bg-indigo-600 text-white px-4 py-2 rounded-md text-sm font-medium hover:bg-indigo-700 transition-colors"
                        >
                            <MessageCircle className="h-4 w-4 mr-2" />
                            AI Assistant
                        </Link>
                    </div>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;
