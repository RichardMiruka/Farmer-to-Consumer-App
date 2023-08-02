import React from 'react';
import './navbar.css';
import { Link } from 'react-router-dom';

function Homepage(){
    return(
      <div className="jumbotron">
        <h1 className="display-4"><b>WELCOME TO ECO-GREEN FARMER'S MARKET</b></h1>
        <br/>
        <p className="lead">This is a digital platform that connects farmers directly with consumers.</p>
        {/* <hr className="my-4"/> */}
        <p className='lead'>This platform allows farmers to list their produce, and consumers purchase quality food at affordable rates.</p><br/>
        <p className="lead">
          <Link to="/login" className="btn btn-primary btn-lg active">Login to get started </Link>
        </p>
      </div>
    )
}

export default Homepage