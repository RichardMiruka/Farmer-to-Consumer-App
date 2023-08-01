import React, { useState } from 'react';
import {BrowserRouter as Router, Route, Link, Routes} from 'react-router-dom';
import './App.css';
import LoginPage from './container/login';
import HomePage from './container/navbar';
import ProductPage from './container/Product';
import Order from './container/order';

function App() {
  const [loggedIn, setLoggedIn] = useState(false);

  const handleLogin = () => {
    // Our group should perform login logic here (e.g., API call to the backend)
    setLoggedIn(true);
  };

  const handleLogout = () => {
    // We should perform logout logic here (e.g., API call to the backend)
    setLoggedIn(false);
    alert('Logged out successfully!');
  };

  return (
  
    <Router>
      <Route path='/' exact Component={HomePage}/>
      <Route/>
    </Router>
      // {!loggedIn ? (
      //   <LoginPage onLogin={handleLogin} />
      // ) : (
      //   <>  
      //   <HomePage onLogout={handleLogout} /> <br/>
      //   <ProductPage/>
      //   </>
      ) }

export default App;