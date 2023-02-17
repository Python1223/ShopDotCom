import React,{useEffect}  from 'react'
import axios from 'axios'
import URLS from '../urls'

const Profile= ()=> {
  const callProfile= ()=> {
    axios({method: 'get', url: URLS.Backend_BASE_URL + URLS.Profile+ '/', data: {'sas': 'aa'}, 
          headers: {'Authorization': 'Bearer '+ localStorage.getItem('accessToken')}
  })
  }
  useEffect(callProfile, [])
  return(
    <React.Fragment>
      <h1>Hello</h1>
    </React.Fragment>
  )
}

export default Profile