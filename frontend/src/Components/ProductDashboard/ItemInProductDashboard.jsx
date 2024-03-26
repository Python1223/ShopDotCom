import React, {useState} from "react"
import {useNavigate} from "react-router-dom"
import './CSS/ProductDashboard.css'
import Item from './Item'
import URLS from '../urls'

const ItemInProductDashboard= ({...props})=> {

	const itemId= props.itemId
	let navigate= useNavigate()
  
	const defaultItemState= {
    'itemName': '', 'itemDetails': '', 'itemPrice': null, 'sellerProfile': '',
    'itemCategory': null, 'itemImage': null
  }
  let [itemState, setItemState]= useState(defaultItemState)

	const handleClick= (event)=> {
		event.preventDefault()
		const itemUrl= URLS.Item+ '/'+ itemId; console.log(itemUrl)
		navigate(itemUrl)
	}
  return(
    <React.Fragment>
          
						<div class="col-2" onClick= {handleClick}>
								<div id="product-1" class="single-product">
										<div class="part-1">
										</div>
										<div class="part-2 right">
												{/* <h3 class="product-title">Here Product Title</h3>
												<h4 class="product-old-price">$79.99</h4>
												<h4 class="product-price">$49.99</h4> */}
												<Item itemId= {itemId} />
										</div>
								</div>
						</div>
  	</React.Fragment>
  )
}
export default ItemInProductDashboard
