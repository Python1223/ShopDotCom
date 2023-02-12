import axios from "axios"
import React, {useState, useEffect} from "react"
import ItemInProductDashboard from "./ItemInProductDashboard"
import "./CSS/ProductDashboard.css"
import 'bootstrap/dist/css/bootstrap.css'
import URLS from '../urls'
import Carousel from 'react-bootstrap/Carousel';

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

<nav class="navbar bg-dark">
    <div class="container-fluid">    
      <div class="col-2">
      <img src="https://shopdotapp.com/wp-content/uploads/2023/01/new_logo_orange.svg" alt="Logo" width="50" height="44" class="d-inline-block align-text-top"/>
      </div>

      <div class="col-4">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search"/>
      </div>
      <div class="col-2">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">My Account</button>
    </div>
      <div class="col-2">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Cart</button>
    </div>
  </div>
</nav>


<Carousel>
      <Carousel.Item>
        <img
          className="d-block w-100 a"
          src="https://i.gadgets360cdn.com/large/big-billion-days-2022-sale_1663819658737.png"
          alt="First slide"
        />
        <Carousel.Caption>
          <h3>First slide label</h3>
          <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
        <img
          className="d-block w-100"
          src="https://pbs.twimg.com/media/EljBauEU4AAToRQ.jpg"
          alt="Second slide"
        />

        <Carousel.Caption>
          <h3>Second slide label</h3>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </Carousel.Caption>
      </Carousel.Item>
    </Carousel>

      <section class="section-products">
        <div class="container-fluid">
          <div class="row justify-content-center text-center">
              <div class="col-md-8 col-lg-6">
                  <div class="header">
                      <h2>Featured Product</h2>
                  </div>
              </div>
          </div>
          <div class="row c over">
            
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          </div>
          <div class="row c over">
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