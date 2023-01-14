import React, {useState} from "react"

const Login= ()=> {

  let defaultLoginState= {'Username': '', 'Password': ''}
  let [loginState, setLoginState]= useState(defaultLoginState)

  const handleLogin= (event)=> {
    event.preventDefault()

    if(event.target.name== 'LoginButton'){
      console.log('loginState-> ', loginState)
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
    </React.Fragment>
  )
}

export default Login
