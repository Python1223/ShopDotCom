import React from 'react';
import {useParams} from 'react-router-dom'
import Item from './Item'

const SellerItemView=() =>{

  const itemID= useParams().itemId
  return(
    <React.Fragment>
    <Item itemId= {itemId}></Item>
    <button>Edit</button>
    </React.Fragment>
  )
}

export default SellerItemView
