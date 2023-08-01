import React from 'react';
import './navbar.css';
import Homepage from './homepage';

const Navbar = ({ onLogout }) => {
  return (
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
        <Homepage/>
    </div>
  );
};

export default Navbar;