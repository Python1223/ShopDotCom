import axios from "axios"
import React, { useState } from "react"
import URLS from '../urls'
import "./CSS/Signup.css"

const SignupUrl= URLS.Backend_BASE_URL+ URLS.Signup

const Signup= ()=> {
  const [addclass, setaddclass] = useState("")

  let defaultBuyerProfile= {'Username': '', 'Email': '', 'Password': ''}
  let defaultSellerProfile= {'Username': '', 'Email': '', 'Password': '', 'StoreName': ''}
  let [buyerProfile, setBuyerProfile] = useState(defaultBuyerProfile)
  let [sellerProfile, setSellerProfile] = useState(defaultSellerProfile)

  const handleBuyerSignup= (event) =>{
    event.preventDefault()

    console.log(event.target.name)
    if(event.target.name== 'BuyerSignupButton'){
      console.log(buyerProfile);

      const signupData= {
        'Username': buyerProfile.Username,
        'Email': buyerProfile.Email,
        'Password': buyerProfile.Password,
        'ProfileString': 'Buyer'
      }

      console.log('Data-> ', signupData, 'url-> ', SignupUrl)

      axios({method: 'post', url: SignupUrl, data: signupData}).then(
        ((response)=> console.log(response)), 
        ((error)=> console.log(error))
      )
    }
    else{
      let newBuyerProfile= {...buyerProfile, [event.target.name]: event.target.value}
      setBuyerProfile(newBuyerProfile)
    }
  }
  
  const handleSellerSignup=(event)=>{
    event.preventDefault()
    
    console.log(event.target.name)
    if(event.target.name=== 'SellerSignupButton'){
      console.log(sellerProfile); /*API Call*/

      const signupData= {
        'Username': sellerProfile.Username,
        'Email': sellerProfile.Email,
        'Password': sellerProfile.Password,
        'ProfileString': 'Seller',
        'StoreName': sellerProfile.StoreName
      }

      console.log('Data-> ', signupData, 'url-> ', SignupUrl)

      axios({method: 'post', url: SignupUrl, data: signupData}).then(
        ((response)=> console.log(response)),
        ((error)=> console.log(error))
      )
    }
    else{
      let newSellerProfile= {...sellerProfile, [event.target.name]: event.target.value}
      setSellerProfile(newSellerProfile)
    }
  }

  return (
    <div className="login-body">
      <div className={`container ${addclass}`} id="container">
        

        <div className="form-container  sign-up-container">
          <form className="login-form">
            <h1>Buyer</h1>
            <input
              className="login-input"
              type="text"
              placeholder="USERNAME"
              name="Username"
              value={buyerProfile.Username}
              onChange={handleBuyerSignup}
            />
            <input
              className="login-input"
              type="email"
              placeholder="EMAIL"
              name="Email"
              value={buyerProfile.Email}
              onChange={handleBuyerSignup}
            />
            <input
              className="login-input"
              type="password"
              placeholder="PASSWORD"
              name="Password"
              value={buyerProfile.Password}
              onChange={handleBuyerSignup}
            />

            <button className="login-button" name="BuyerSignupButton" type="submit" onClick={handleBuyerSignup}>
              Sign Up
            </button>
          </form>
        </div>
        
        
        <div className="form-container sign-in-container">
          <form className="login-form" >
            <h1>Seller</h1>
            <input
              className="login-input"
              type="text"
              placeholder="Username"
              name="Username"
              value={sellerProfile.Username}
              onChange={handleSellerSignup}
            />
            <input
              className="login-input"
              type="email"
              placeholder="EMAIL"
              name="Email"
              value={sellerProfile.Email}
              onChange={handleSellerSignup}
            />
            <input
              className="login-input"
              type="text"
              placeholder="STORE"
              name="StoreName"
              value={sellerProfile.StoreName}
              onChange={handleSellerSignup}
            />
            <input
              className="login-input"
              type="password"
              placeholder="Password"
              name="Password"
              value={sellerProfile.Password}
              onChange={handleSellerSignup}
            />
            <button className="login-button" name= "SellerSignupButton" type="submit" onClick={handleSellerSignup}>
              Sign Up
            </button>
          </form>
          
        </div>
        <div className="overlay-container">
          <div className="overlay">
            <div className="overlay-panel overlay-left">
              <button
                className="login-button"
                id="signIn"
                onClick={() => setaddclass("")}
              >
              SELLER
                
              </button>
            </div>
            <div className="overlay-panel overlay-right">
              <button
                className="login-button"
                id="signUp"
                onClick={() => setaddclass("right-panel-active")}
              >
              BUYER
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Signup;