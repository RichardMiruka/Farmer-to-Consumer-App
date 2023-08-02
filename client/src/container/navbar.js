import React from 'react';
import './navbar.css';
import {BrowserRouter as Router, Route, Link, Routes} from 'react-router-dom';
import Order from './order';
import ProductPage from './Product';
import HomePage from './homepage';

const Navbar = ({ onLogout }) => {
  return (
    <Router>
      <div>
        <nav>
          <div className='navbar-container'>
            <ul className='navbar-menu'>
              <li>
                <a href="/">Home</a>
              </li>
              <li>
                <a href="/search">Search</a>
              </li>
              <li>
                <a href="/orders">Orders</a>
              </li>
              <li>
                <img src='client/src/img/shopping-3.png' alt='logo' />
                <button onClick={onLogout}>Logout</button>
              </li>
            </ul>
          </div>
        </nav>
        <Routes>
          <Route path='/' exact Component={HomePage}/>
          <Route path='/search' exact Component={ProductPage}/>
          <Route path='/orders' exact Component={Order}/>
        </Routes>
      </div>
    </Router>
  );
};

export default Navbar;