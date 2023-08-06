import React, { useState } from "react";
import './login.css';
import { useNavigate, Link } from 'react-router-dom'

const LoginPage = ({ onLogin }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError]= useState('');

  const navigate=useNavigate()
  const handleLogin=async()=>{
    try { const response=await fetch('http://127.0.0.1:5000/api/v1/Login',{
    method:'POST',
    headers:{
      'Content-Type':'application/json'
    },
    body:JSON.stringify({username, password}),
  }
  );
  const data=await response.json()
  if (response.ok){
    localStorage.setItem("token",data['access_token'])
    navigate('/products')
  }
  else{
    setError(data.error)
  }  
    } catch (error) {
      setError('An error occurred, please do try again')
    }
  }


  return (
    <div>
    <img src="client/src/img/shopping-4.png" alt="logo"/>
    {error && <p>{error}</p>}
      <form>
        <h1>Log in</h1>
        <label>Username</label>
        <input
          type='text'
          placeholder='username'
          value={username}
          onChange={(e) => setUsername(e.target.value)}
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
        <button type='button' onClick={handleLogin}>Login</button>
        <br />
        <Link to="/register">Don't have an account?</Link>
      </form>
    </div>
  );
};

export default LoginPage;