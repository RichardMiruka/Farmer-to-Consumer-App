import React from 'react';

function Login() {
  return (
    <div>
      <form>
        <h1>Log in</h1>
        <label>Email</label>
        <input type='email' placeholder='email' /><br />
        <label>Password</label>
        <input type='password' placeholder='password' />
        
        <button type="button">Forgot your password?</button><br />
        <button type="button">Don't have an account?</button>
      </form>
    </div>
  );
}

export default Login;
