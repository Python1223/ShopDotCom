import React, {useState, useEffect} from 'react'
import axios from 'axios'
import URLS from '../urls'

const Item= ({...props})=> {

  console.log(props)
  const itemId= props.itemId
  console.log('itemId-> ', itemId)
  const defaultItemState= {
    'itemName': '', 'itemDetails': '', 'itemPrice': null, 'sellerProfileId': null,
    'itemCategory': null, 'itemImageUrl': null
  }
  let [itemState, setItemState]= useState(defaultItemState)

  const setItemAttributes= (response)=> {
    let updatedItemState= {
      'itemName': response.data.item.itemName,
      'itemDetails': response.data.item.itemDetails,
      'itemPrice': response.data.item.itemPrice,
      'sellerProfileId': response.data.item.sellerProfileId,
      'itemCategory': response.data.item.itemCategory,
      'itemImageUrl': URLS.Backend_BASE_URL+ response.data.item.itemImage,
    }
    setItemState(updatedItemState) 
  }
  const handleError= (error)=> console.log('Error-> ',error)
  
  const getItemAttributes= ()=> {
    const url= URLS.Backend_BASE_URL+ URLS.Item+ '/'+ itemId
    const headers= {'Authorization': 'Bearer '+ localStorage.getItem('accessToken')}

    axios({method: 'get', url: url, headers: headers}).then(setItemAttributes, handleError)
  }
  useEffect(getItemAttributes, [])

  return(
    <React.Fragment>
      <h2>ITEM</h2>
      <h3>{itemState.itemName}</h3>
      <h3>{itemState.itemDetails}</h3>
      <h3>{itemState.itemPrice}</h3>
      <h3>{itemState.sellerProfileId}</h3>
      <h3>{itemState.itemCategory}</h3>
      <img src= {itemState.itemImageUrl} />
    </React.Fragment>
  )
}

export default Item
