import axios from "axios"
import React, {useState, useEffect} from "react"
import ItemInProductDashboard from "./ItemInProductDashboard"
import "./CSS/ProductDashboard.css"
import 'bootstrap/dist/css/bootstrap.css'
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
            
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          </div>
        </div>
      </section>

    </React.Fragment>
 ) 
}

export default ProductDashboard