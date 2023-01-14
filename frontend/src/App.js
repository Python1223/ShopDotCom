import React from 'react'
import {BrowserRouter, Routes, Route} from 'react-router-dom'

import Signup from "./Components/Signup";
import Login from './Components/Login';
import LandingPage from './Components/LandingPage';

const App = () => {
  return (
    <React.Fragment>
      <BrowserRouter>
        <Routes>
          <Route exact path= '/' element= {<LandingPage />} />
          <Route exact path= '/Signup' element= {<Signup />} />
          <Route exact path= '/Login' element= {<Login />} />
        </Routes>
      </BrowserRouter>
    </React.Fragment>
  );
};

export default App;