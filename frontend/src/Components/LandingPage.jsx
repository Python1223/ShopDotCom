import React from 'react'
import {useNavigate} from 'react-router-dom'
import URLS from '../urls'
import 'bootstrap/dist/css/bootstrap.css';


const LandingPage= ()=> {

  let navigate= useNavigate()

  const navigateToSignup= ()=> navigate(URLS.Signup)

  const navigateToLogin= ()=> navigate(URLS.Login)

  return(
    <React.Fragment>
      
      <nav class="navbar bg-light">
    <div class="container-fluid">    
      <img src="https://shopdotapp.com/wp-content/uploads/2023/01/new_logo_orange.svg" alt="Logo" width="50" height="44" class="d-inline-block align-text-top"/>
      <h1 class="navbar-brand">ShopDotCom</h1>
        <div class="btn-grp">      
      <button onClick={navigateToSignup} class="btn btn-primary  m-1">Signup</button>
      <button onClick={navigateToLogin} class="btn btn-primary">Login</button>
      </div>
  </div>
</nav>
    </React.Fragment>
  )
}

export default LandingPage
