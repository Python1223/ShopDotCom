import axios from "axios"
import React, {useState} from "react"
import URLS from '../urls'

const LoginUrl= URLS.Backend_BASE_URL+ URLS.Login
const GetTokenUrl= URLS.Backend_BASE_URL+ URLS.GetToken
const loginWithCorrectCredentialsMessage= 'Please try with correct credentials'
const loginRetryMessage= 'Unexpected Error. Please Login again'

const Login= ()=> {

  let defaultLoginState= {'Username': '', 'Password': ''}
  let [loginState, setLoginState]= useState(defaultLoginState)
  let [loginMessage, setLoginMessage]= useState('')

  const handleLogin= (event)=> {
    event.preventDefault()

    if(event.target.name== 'LoginButton'){
      console.log('loginState-> ', loginState)

      const Credentials= {'Username': loginState.Username, 'Password': loginState.Password}

      axios({method: 'post', url: LoginUrl, data: Credentials}).then(
        ((response)=>{
          console.log(response)
          axios({method: 'post', url: GetTokenUrl, data: {username: Credentials.Username, password: Credentials.Password}})
          .then(
            ((response)=> {
              console.log("adad res", response)
              let accessToken= response.data.access
              let refreshToken= response.data.refresh
              localStorage.setItem("accessToken", accessToken)
              localStorage.setItem("refreshToken", refreshToken)
              /*Redirect to Product Page*/
            }),
            ((error)=> {console.log("aaaaaa", error)})
          )
        }),
        ((error)=>{
          let statusCode= error.response.status
          if(statusCode== 400) {
            console.log(loginWithCorrectCredentialsMessage); setLoginMessage(loginWithCorrectCredentialsMessage)
          }
          else
          {
            console.log(loginRetryMessage); setLoginMessage(loginRetryMessage)
          }
        })
      )
    }
    else{
      let newLoginState= {...loginState, [event.target.name]: event.target.value}
      setLoginState(newLoginState)
    }
  }

  return(
    <React.Fragment>
      <form>
      <input
            type="text"
            placeholder="USERNAME"
            name="Username"
            value={loginState.Username}
            onChange={handleLogin}
            />
      <br />
      <input
            type="password"
            placeholder="PASSWORD"
            name="Password"
            value={loginState.Password}
            onChange={handleLogin}
            />
      <button name= "LoginButton" type= "submit" onClick={handleLogin}>Login</button>
      </form>
      <p >{loginMessage}</p>
    </React.Fragment>
  )
}

export default Login
