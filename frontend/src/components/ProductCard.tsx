import React from 'react';
import { Link } from 'react-router-dom';

interface Product {
    id: number;
    title: string;
    price: number;
    image_url: string;
    category: string;
}

interface ProductCardProps {
    product: Product;
}

const ProductCard: React.FC<ProductCardProps> = ({ product }) => {
    return (
        <Link to={`/products/${product.id}`} className="group">
            <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition-shadow duration-300">
                <div className="aspect-w-1 aspect-h-1 w-full overflow-hidden bg-gray-200 xl:aspect-w-7 xl:aspect-h-8">
                    <img
                        src={product.image_url}
                        alt={product.title}
                        className="h-full w-full object-cover object-center group-hover:opacity-75"
                    />
                </div>
                <div className="p-4">
                    <h3 className="mt-1 text-lg font-medium text-gray-900 truncate">{product.title}</h3>
                    <p className="mt-1 text-sm text-gray-500">{product.category}</p>
                    <p className="mt-1 text-lg font-bold text-gray-900">₹{product.price}</p>
                </div>
            </div>
        </Link>
    );
};

export default ProductCard;
