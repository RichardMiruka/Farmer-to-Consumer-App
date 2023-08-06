import React, { useEffect, useState } from 'react'

function Order(){
    const [orders, setOrders]= useState([]);

    useEffect(()=>{
        fetch('http://localhost:5000/api/v1/Orders')
        .then((res)=>res.json())
        .then(ord => setOrders(ord.data))
        .catch(error =>console.error(error));
    }, []);

    return(
        <div>
            <h1>Here are your orders</h1>
            <div className='row'>
                
            </div>
        </div>
)   

}

export default Order