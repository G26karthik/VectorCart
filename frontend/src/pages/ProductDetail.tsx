import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import api from '../api';

interface Product {
    id: number;
    title: string;
    price: number;
    description: string;
    features: string;
    category: string;
    image_url: string;
    product_url: string;
}

const ProductDetail: React.FC = () => {
    const { id } = useParams<{ id: string }>();
    const [product, setProduct] = useState<Product | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchProduct = async () => {
            try {
                const response = await api.get(`/products/${id}`);
                setProduct(response.data);
            } catch (error) {
                console.error('Error fetching product:', error);
            } finally {
                setLoading(false);
            }
        };

        fetchProduct();
    }, [id]);

    if (loading) {
        return (
            <div className="flex justify-center items-center h-screen">
                <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
            </div>
        );
    }

    if (!product) {
        return <div className="text-center py-12">Product not found</div>;
    }

    return (
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <div className="bg-white rounded-lg shadow-lg overflow-hidden">
                <div className="md:flex">
                    <div className="md:flex-shrink-0 md:w-1/2">
                        <img
                            className="h-96 w-full object-cover md:h-full"
                            src={product.image_url}
                            alt={product.title}
                        />
                    </div>
                    <div className="p-8 md:w-1/2">
                        <div className="uppercase tracking-wide text-sm text-indigo-500 font-semibold">
                            {product.category}
                        </div>
                        <h1 className="mt-2 text-3xl leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl">
                            {product.title}
                        </h1>
                        <p className="mt-4 text-2xl font-bold text-gray-900">₹{product.price}</p>

                        <div className="mt-6">
                            <h3 className="text-lg font-medium text-gray-900">Description</h3>
                            <p className="mt-2 text-gray-500">{product.description}</p>
                        </div>

                        <div className="mt-6">
                            <h3 className="text-lg font-medium text-gray-900">Features</h3>
                            <div className="mt-2 flex flex-wrap gap-2">
                                {product.features.split(',').map((feature, index) => (
                                    <span
                                        key={index}
                                        className="inline-flex items-center px-3 py-0.5 rounded-full text-sm font-medium bg-indigo-100 text-indigo-800"
                                    >
                                        {feature.trim()}
                                    </span>
                                ))}
                            </div>
                        </div>

                        <div className="mt-8">
                            <a
                                href={product.product_url}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="inline-flex items-center justify-center px-5 py-3 border border-transparent text-base font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700"
                            >
                                View on Traya
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ProductDetail;
