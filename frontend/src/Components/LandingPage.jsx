import React from 'react'
import {useNavigate} from 'react-router-dom'
import URLS from '../urls'

const LandingPage= ()=> {

  let navigate= useNavigate()

  const navigateToSignup= ()=> navigate(URLS.Signup)

  const navigateToLogin= ()=> navigate(URLS.Login)

  return(
    <React.Fragment>
      <h1>ShopDotCom</h1>
      <button onClick={navigateToSignup}>Signup</button>
      <button onClick={navigateToLogin}>Login</button>
    </React.Fragment>
  )
}

export default LandingPage
