import axios from "axios"
import React, {useState, useEffect} from "react"
import 'bootstrap/dist/css/bootstrap.css'
import "./CSS/ProductDashboard.css"
import URLS from '../urls'

const ProductDashboardUrl= URLS.Backend_BASE_URL+ URLS.ProductDashboard
const accessToken= localStorage.getItem('accessToken')

const ProductDashboard= ()=>{
  let defaultProductListState= new Array()
  let [productListState, setProductListState]= useState(defaultProductListState)

  const getProductList= ()=> {
    /*API Call + Populathe productListState */
    const headers= {'Authorization': 'Bearer'+ ' '+ accessToken}
    axios({method: 'get', url: ProductDashboardUrl, headers: headers}).then(
      ((response)=> setProductListState(response.data.productList)),
      ((error)=>{console.log(error)})
    )
  }
  useEffect(getProductList, [])
  
  return(
    <React.Fragment>
      <section class="section-products">
        <div class="container">
          <div class="row justify-content-center text-center">
              <div class="col-md-8 col-lg-6">
                  <div class="header">
                      <h2>Featured Product</h2>
                  </div>
              </div>
          </div>
          <div class="row">
            <div class="col-md-6 col-lg-4 col-xl-3">
              <div id="product-1" class="single-product">
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
          </div>
        </div>
      </section>
    </React.Fragment>
 ) 
}
