import React from "react";
import './productcard.css';

const ProductCard=({product})=>{
    return(
        <div className="card">
            <img src={product.image} alt={product.name} className="card-img-top"/>
            <div className="card-body">
                <h3 className="card-title">{product.name}</h3>
                <p className="card-title">{product.description}</p>
                <p className="card-title">price Ksh {product.price}</p>
                <button className="btn btn-primary">Make Order</button>
            </div>
        </div>
    )
}

export default ProductCard