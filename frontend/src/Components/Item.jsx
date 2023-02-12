import React, {useState, useEffect} from 'react'
import {useHistory, useParams} from 'react-router-dom'
import axios from 'axios'
import URLS from '../urls'

const Item= ()=> {

  const itemId= useParams().itemId
  const defaultItemState= {
    'itemName': '', 'itemDetails': '', 'itemPrice': null, 'sellerProfileId': null,
    'itemCategory': null, 'itemImageUrl': null
  }
  let [itemState, setItemState]= useState(defaultItemState)

  const setItemAttributes= (response)=> {
    let updatedItemState= {
      'itemName': response.data.itemName,
      'itemDetails': response.data.itemDetails,
      'itemPrice': response.data.itemPrice,
      'sellerProfileId': response.data.sellerProfileId,
      'itemCategory': response.data.itemCategory,
      'itemImageUrl': response.data.itemImageUrl,
    }
    setItemState(updatedItemState)
  }
  const handleError= (error)=> console.log('Error-> ',error)
  
  const getItemAttributes= ()=> {
    const url= URLS.Backend_BASE_URL+ URLS.Item+ '/'+ itemId
    axios({method: 'get', url: url, data: {'itemId': itemId}}).then(setItemAttributes, handleError)
  }
  useEffect(getItemAttributes, [])

  // const handleAddToCart= ()=> {
  //   const url= URLS.Backend_BASE_URL+ URLS.Cart
  //   axios({url: url, method: 'patch', data: {itemId: itemId}}).then(
  //     (response)=> useHistory().push(URLS.Cart),
  //     (error)=> console.log(error)
  //   )
  // }

  //const handleBuyNow= ()=> {}

  return(
    <React.Fragment>
      <h3>{itemState.itemName}</h3>
      <h3>{itemState.itemDetails}</h3>
      <h3>{itemState.itemPrice}</h3>
      <h3>{itemState.sellerProfileId}</h3>
      <h3>{itemState.itemCategory}</h3>
      <img src= {itemState.itemImageUrl}/>

      {/* <button type="button" class="btn btn-success" onClick= {handleAddToCart()}>Add To Cart</button> */}
      {/* <button type="button" class="btn btn-success" onClick= {handleBuyNow()}>Buy Now</button> */}
    </React.Fragment>
  )
}

export default Item
