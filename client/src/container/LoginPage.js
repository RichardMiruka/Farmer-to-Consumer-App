import React, { useState } from "react";
import './login.css';

const LoginPage = ({ onLogin }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    //What to do with our app
    // Wcan perform validation here and make API call to login
    // For us to understand, we'll just log the user in with any input***
    onLogin();
  };

  return (
    <div>
    <img src="client/src/img/shopping-4.png" alt="logo"/>
      <form onSubmit={handleSubmit}>
        <h1>Log in</h1>
        <label>Email</label>
        <input
          type='email'
          placeholder='email'
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <br />
        <label>Password</label>
        <input
          type='password'
          placeholder='password'
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <br />
        <button type='submit'>Login</button>
        <a href="#">Forgot your password?</a>
        <br />
        <a href="#">Don't have an account?</a>
      </form>
    </div>
  );
};

export default LoginPage;