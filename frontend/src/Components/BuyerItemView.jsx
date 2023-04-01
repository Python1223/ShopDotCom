import React, {useState, useEffect} from 'react'
import {useParams} from 'react-router-dom'
import axios from 'axios'
import Item from './Item'
import URLS from '../urls'
import addItemToCart from '../Utils/AddItemToCart'
import deleteItemFromCart from '../Utils/DeleteItemFromCart'

const CartButtonStates= ['Default', 'AddToCart', 'DeleteFromCart']

const BuyerItemView= ()=> {

  const itemId= useParams().itemId
  let [itemInCartState, setItemInCartState]= useState(null)
  let [cartButtonState, setCartButtonState]= useState(CartButtonStates[0])

  const checkItemInCart= ()=> {
    
    const handleCheckItemInCartResponse= (response)=> {
      response.status == 302 ? setItemInCartState(true) : setItemInCartState(false)
      response.status == 302 ? setCartButtonState(CartButtonStates[1]) : setCartButtonState(CartButtonStates[2])
    }
    
    const handleCheckItemInCartError= (error)=> console.log('Error occured while checking item in Cart-> ', error)
    
    const checkItemInCartUrl= URLS.Cart+ '/ItemInCart/'+ itemId
    const headers= {'Authorization': 'Bearer '+ localStorage.getItem('accessToken')}
    
    axios({method: 'get', url: checkItemInCartUrl, headers: headers}).then
    (handleCheckItemInCartResponse, handleCheckItemInCartError)
  }
  useEffect(checkItemInCart, [])
  
  return(
    <React.Fragment>
      <Item itemId= {itemId} />
      
      {/* <button name = "GoToCartButton" type = "submit"
              onClick = {() => Navigate(URLS.Cart)}>Cart</button> */}

      
      {()=> {
        // Logic for which Cart button to get rendered
        // Instead of buttennames we will add cartbuttonstates here
        if(itemInCartState === true) return <button name="AddItemToCartButton" type="submit" 
                                                    onClick={() => addItemToCart(itemId)}>
                                                      Add Item To Cart
                                            </button>
        else if(itemInCartState === false) return <button name="DeleteFromCartButton" type="submit"
                                                          onClick={() => deleteItemFromCart(itemId)}>
                                                            Remove Item From Cart
                                                  </button>
        else return <button name = "DefaultCartButton">Default Cart Button</button>
        }}()
      
      {/* <p>{CartString}</p> */}
      <button>Buy Now</button>
    </React.Fragment>
  )
}

export default BuyerItemView
