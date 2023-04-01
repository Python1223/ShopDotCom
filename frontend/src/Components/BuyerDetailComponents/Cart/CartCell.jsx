import React from "react"
import {useNavigate} from "react-router-dom"
import ItemCell from "../ItemCell"
import axios from "axios"
import URLS from "../../../urls"


const CartCell = ({...props}) => {
  
  const navigate = useNavigate()
  const itemId = itemId
  const CartUrl = URLS.Backend_BASE_URL + URLS.Cart
  const DeleteFromCartUrl = CartUrl + '/' + 'DeleteItem/' + itemId
  
  const deleteItemFromCart = (event) => {
    event.preventDefault()

    const handleDeleteFromCartResponse = (response) => {
      console.log('Response from Deleting Item from Cart -> ', response)
      navigate(to = CartUrl)
    }
    
    const handleDeleteFromCartError = (error) => 
      console.log('Error occured during deleting item from Cart ->', error)

    axios({method : 'patch', 
          url : DeleteFromCartUrl,
          headers : headers}).then(handleDeleteFromCartResponse, handleDeleteFromCartError)
  }

  return(
    <React.Fragment>
      <ItemCell itemId = {itemId} />
      <Button name = "DeleteItemFromCart" type = "submit"
                onClick = {(event) => deleteItemFromCart(event, itemId)}>Delete From Cart</Button>
        
        {/* <Button name = "BuyItem" type = "submit"
                onClick = {(event) => buyItem(event, itemId)}>Buy Now</Button> */}
    </React.Fragment>
  )
}