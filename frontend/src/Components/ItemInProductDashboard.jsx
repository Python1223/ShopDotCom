import React, {useState, useEffect, useHistory} from "react";
import './CSS/ProductDashboard.css'

const ItemInProductDashboard= ()=> {

  const defaultItemState= {
    'itemName': '', 'itemDetails': '', 'itemPrice': null, 'sellerProfile': '',
    'itemCategory': null, 'itemImage': null
  }
  let [itemState, setItemState]= useState(defaultItemState)

  return(
    <React.Fragment>
          
						<div class="col-2">
								<div id="product-1" class="single-product">
										<div class="part-1">
										</div>
										<div class="part-2 right">
												<h3 class="product-title">Here Product Title</h3>
												<h4 class="product-old-price">$79.99</h4>
												<h4 class="product-price">$49.99</h4>
										</div>
								</div>
						</div>


   </React.Fragment>
  )
}
export default ItemInProductDashboard