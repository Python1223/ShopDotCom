import React from 'react'
import {BrowserRouter, Routes, Route} from 'react-router-dom'

import Signup from "./Components/Signup"
import Login from './Components/Login'
import LandingPage from './Components/LandingPage'
import ProductDashboard from './Components/ProductDashboard'
import Item from './Components/Item'
import Profile from './Components/Profile'

const App = () => {
  return (
    <React.Fragment>
      <BrowserRouter>
        <Routes>
          <Route exact path= '/' element= {<LandingPage />} />
          <Route exact path= '/Signup' element= {<Signup />} />
          <Route exact path= '/Login' element= {<Login />} />
          <Route exact path= '/ProductDashboard' element= {<ProductDashboard />} />
          <Route exact path= '/Profile' element= {<Profile />} />
          <Route exact path= "/Item/:itemId" element= {<Item />}/>
        </Routes>
      </BrowserRouter>
    </React.Fragment>
  )
}

export default App
