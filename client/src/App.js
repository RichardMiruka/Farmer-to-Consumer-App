import 'bootstrap/dist/css/bootstrap.min.css'
import React from 'react';
import {BrowserRouter as Router, Route, Link, Routes} from 'react-router-dom';
import './App.css';
import Product from './container/Product';
import Homepage from './container/homepage';
import LoginPage from './container/login';
import RegisterPage from './container/register';

function App() {

  return (
    <Router>
     <Routes>
      <Route path='/login'element={<LoginPage/>}/>
      <Route path='/register' element={<RegisterPage/>}/>
      <Route path='/products' element={<Product/>}/>
      <Route path='/' element={<Homepage/>}/>
     </Routes>
    </Router>
      ) }

export default App;
