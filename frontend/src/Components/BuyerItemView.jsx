import React from 'react'
import {useParams} from 'react-router-dom'
import Item from './Item'
import URLS from '../urls'

const CartUrl= URLS.Backend_BASE_URL+ URLS.Cart

const BuyerItemView= ()=> {

  const itemId= useParams().itemId

  const addItemToCart=(event)=>{
    event.preventDefault()
    
    console.log(event.target.name)
    

    console.log('Data-> ', signupData, 'url-> ', CartUrl)

    // Include Access Token
    axios({method: 'patch', url: CartUrl, data: {'itemId': itemId}}).then(
    ((response)=> console.log(response)),
    ((error)=> console.log(error))
    )

  }


  return(
    <React.Fragment>
    <Item itemId= {itemId} k2= {4}></Item>
    <button name="AddItemToCartButton" type="submit" onClick={addItemToCart}>Add to Cart</button>
    <button>Buy Now</button>
    </React.Fragment>
  )
}

export default BuyerItemView
