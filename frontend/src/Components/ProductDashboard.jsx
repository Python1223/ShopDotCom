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
          src="https://i.gadgets360cdn.com/large/Flipkart-Big-Billion-Days-Sale-1200x800-1632897416071.jpg"
          alt="First slide"
        />
      </Carousel.Item>
      <Carousel.Item>
        <img
          className="d-block w-100 a"
          src="https://pbs.twimg.com/media/EljBauEU4AAToRQ.jpg"
          alt="Second slide"
        />
      </Carousel.Item>
    </Carousel>

      <section class="section-products position">
        <div class="container-fluid">
          <div class="row">
            
          {/* <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard />
          <ItemInProductDashboard /> */}

          <div class="card col-3 back">
            <h4 class="fonts">Male Shirts</h4>
            <div class="row mid">
            <img class="card-img-top noBorderR" src="https://assets.ajio.com/medias/sys_master/root/20221109/61kh/636b8ebaf997ddfdbd664273/-473Wx593H-462323964-purple-MODEL.jpg" alt="Card image cap"/>
            <img class="card-img-top noBorderR" src="https://img3.junaroad.com/uiproducts/19126301/pri_175_p-1673529653.jpg" alt="Card image cap"/>
            <img class="card-img-top noBorderR" src="https://www.muftijeans.in/media/catalog/product/cache/72ecbf8444b2c4d1e625f30416db39ce/1/_/1_mfs-11994-o-03-red_1.jpg" alt="Card image cap"/>
            <img class="card-img-top noBorderR" src="https://cdn.shopify.com/s/files/1/1414/2498/products/ClassicShirt_FrenchBlue1_1024x1024.jpg?v=1667207840" alt="Card image cap"/>
            </div>
          </div>

          <div class="card col-3 back">
            <h4 class="fonts">Female Shirts</h4>
            <div class="row mid">
            <img class="card-img-top noBorderR" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYTb4j_YQqh5D2hZr_DAAGwJZGJOl1H9s_wQ&usqp=CAU" alt="Card image cap"/>
            <img class="card-img-top noBorderR" src="https://img.tatacliq.com/images/i8/437Wx649H/MP000000014412833_437Wx649H_202209101828191.jpeg" alt="Card image cap"/>
            <img class="card-img-top noBorderR" src="https://images.bewakoof.com/t640/women-s-checks-overlap-shirt-top-300373-1656171760-1.jpg" alt="Card image cap"/>
            <img class="card-img-top noBorderR" src="https://images.meesho.com/images/products/92647725/rinpx_256.jpg" alt="Card image cap"/>
            </div>
          </div>

          <div class="card col-3 back">
            <h4 class="fonts">Jeans</h4>
            <div class="row mid">
            <img class="card-img-top noBorderR" src="https://imagescdn.aeo.in/img/app/brands/ae/jeans/men/Skinny_11-12-2019.jpg?auto=format" alt="Card image cap"/>
            <img class="card-img-top noBorderR" src="https://images.lee.com/is/image/Lee/2076456-ALT8?$KDP-MEDIUM$" alt="Card image cap"/>
            <img class="card-img-top noBorderR" src="https://www.petermillar.com/dw/image/v2/BHFJ_PRD/on/demandware.static/-/Sites-pm-master-catalog/default/dw8358ccfe/ME0XB90FB_SWB_ALT_A.jpg?sw=478&sh=649" alt="Card image cap"/>
            <img class="card-img-top noBorderR" src="https://www.politix.com.au/dw/image/v2/ABBA_PRD/on/demandware.static/-/Sites-politix-master-catalog/default/dwd2dbdc2c/images/hires/Summer%202022/B3/B3%20Day%203/Re-Shoot/yd11-dkindigo-6.jpg?sw=2000&sh=2000&sm=fit" alt="Card image cap"/>
            </div>
          </div>

          <div class="card col-3 back">
            <h4 class="fonts">Sweaters</h4>
            <div class="row mid">
            <img class="card-img-top noBorderR" src="https://5.imimg.com/data5/SW/WE/MY-11559983/knitted-mens-sweaters-250x250.jpg" alt="Card image cap"/>
            <img class="card-img-top noBorderR" src="https://imagescdn.planetfashion.in/img/app/product/7/746139-8403776.jpg?auto=format" alt="Card image cap"/>
            <img class="card-img-top noBorderR" src="https://assets.myntassets.com/dpr_1.5,q_60,w_400,c_limit,fl_progressive/assets/images/21334354/2022/12/28/99ffe786-a30a-47ad-b484-60bb0c949c961672229892135AMERICANEAGLEOUTFITTERSMenTanWhiteFairIslePrintedPullover1.jpg" alt="Card image cap"/>
            <img class="card-img-top noBorderR" src="https://assets.myntassets.com/dpr_1.5,q_60,w_400,c_limit,fl_progressive/assets/images/21334356/2022/12/28/327b7dc0-1d00-4bbc-918e-80af97cd21ce1672229884013AMERICANEAGLEOUTFITTERSMenBurgundyWhiteStripedStripedPullove1.jpg" alt="Card image cap"/>
            </div>
            
          </div>
          {/* <div class="row justify-content-center text-center">
              <div class="col-md-8 col-lg-6">
                  <div class="header">
                      <h2>Featured Product</h2>
                  </div>
              </div>
          </div> */}

          </div>
          <div class="row back2">
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

          <div class="row">
            <div class="col-4">

            </div>

          </div>

          </div>
        
      </section>

    </React.Fragment>
 ) 
}

export default ProductDashboard