import React, { useState, useEffect } from 'react';
import ProductCard from './ProductCard';
import './product.css';

const Product = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/api/v1/products')
      .then(res => res.json())
      .then(prod => setProducts(prod.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div className="container">
      <div className='row'>
      {products.map(product => (
        <ProductCard key={product.id} product={product} className='col-md-3 mb-4' />
      ))}
      </div>
    </div>
  );
};

export default Product;

