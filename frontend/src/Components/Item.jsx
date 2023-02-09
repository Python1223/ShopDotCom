import React, {useState} from "react";
import './CSS/ProductDashboard.css'

const Item= ()=> {

  const defaultItemState= {
    'itemName': '', 'itemDetails': '', 'itemPrice': null, 'sellerProfile': '',
    'itemCategory': null, 'itemImage': null
  }
  let [itemState, setItemState]= useState(defaultItemState)

  return(
    <React.Fragment>
          
            <div class="col-md-6 col-lg-4 col-xl-3">
              <div id="product-1" class="single-product">
                <img src= "https://img.tatacliq.com/images/i7/437Wx649H/MP000000008831694_437Wx649H_202102192220101.jpeg" />
                <div class="part-1">

                  <ul>
                    <li><a href="#"><i class="fa fa-shopping-cart"></i></a></li>
                    <li><a href="#"><i class="fa fa-heart"></i></a></li>
                    <li><a href="#"><i class="fa fa-plus"></i></a></li>
                    <li><a href="#"><i class="fa fa-expand"></i></a></li>
                  </ul>
                </div>
                <div class="part-2">
                  <h3 class="product-title">Here Product Title</h3>
                  <h4 class="product-old-price">$79.99</h4>
                  <h4 class="product-price">$49.99</h4>
                </div>
              </div>
            </div>
    </React.Fragment>
  )
}
export default Item