import React from 'react'
import axios from 'axios'
import addItemToCart from '../../Utils/AddItemToCart'

const AddItemToCartButton = () => {
  return(
    <Button name = "AddToCartButton" type = "submit"
            onClick = {addItemToCart}>Add To Cart</Button>
  )
}