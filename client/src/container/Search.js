import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import ProductCard from './ProductCard';

const Search = () =>  {
    const [data, setData] = useState({
        products: [],
        product:"",
        search: "",
        results:[],
        searched:false
    });

    const { products, product, search, results, searched} =data
}

const loadProducts = () =>{
    getProducts().then(res=>{
        if(res.console.error){
            console.log(res.error)
        } else {
            setData({...data, products: res})
        }
    })

    useEffect(()=>{
        loadProducts();
    }, [])


    const searchData= (e) =>{
        e.preventDefault();
        searchData()
    }

    const searchedResult = (results = []) => {
        return (
            <div className='row'>
                {results.map((product, i)=> (<Card key={i} product={product}/>))}
            </div>
        )
    }

    const handleChange = (name) => event => {
        setData({...data, [name]: event.target.value, searched: false})
    };
    return (
        <div className='row'>
            <div className='container mb-3'></div>
            <div className='container-fluid mb-3'>{searchedResult(results)}</div>
        </div>
    )
}