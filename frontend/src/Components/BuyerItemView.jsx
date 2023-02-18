import React from 'react'
import {useParams} from 'react-router-dom'
import Item from './Item'

const BuyerItemView= ()=> {

  const itemId= useParams().itemId
  return(
    <React.Fragment>
    <Item itemId= {itemId} k2= {4}></Item>
    <button>Add to Cart</button>
    <button>Buy Now</button>
    </React.Fragment>
  )
}

export default BuyerItemView
