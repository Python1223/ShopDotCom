import React, {useState, useEffect} from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import ItemCell from '../ItemCell'
import URLS from '../../../urls'
import { Button } from 'react-bootstrap'
import deleteItemFromCart from '../../../Utils/DeleteItemFromCart'

const Cart = () => {

  const navigate = useNavigate()

  const defaultItemIdListState = []
  let [itemIdListState, setItemIdListState] = useState(defaultItemIdListState)
  
  const getItemIdList = () => {
    
    const CartUrl = URLS.Backend_BASE_URL + URLS.Cart
    const headers = {'Authorization' : 'Bearer ' + localStorage.getItem('accessToken')}
    
    const handleResponse = (response) => {
      let itemIdList = response.data.itemIdList.split(",")
      setItemIdListState(itemIdList)
    }
    
    const handleError = (error) => console.log('Error while fetching cart info -> ', error)
    
    axios({method : 'get', url : CartUrl, headers : headers}).then(handleResponse, handleError)
  
  }
  useEffect(getItemIdList, [])

  const renderCell = (itemId) => {
    return(
      <React.Fragment>
        {() => itemIdListState.map((itemId) => return(<CartCell itemId = {itemId} />))}
        

      </React.Fragment>
    )
  }

  return(
    <React.Fragment>
      <p>CART</p>

      {
        // Render the cells
        () => itemIdListState.map(renderCell)()
      }
    </React.Fragment>
  )
}
export default Cart
