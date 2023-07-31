import React, { useState } from 'react';
import './App.css';
import LoginPage from './container/login';
import HomePage from './container/navbar';

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
    <div className="navbar-container">
      {!loggedIn ? (
        <LoginPage onLogin={handleLogin} />
      ) : (
        <HomePage onLogout={handleLogout} />
      )}
    </div>
  );
}

export default App;