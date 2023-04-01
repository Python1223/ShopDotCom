import React from 'react'
import {useNavigate} from 'react-router-dom'
import URLS from '../../urls'

const ItemCell = ({...props}) => {

  const itemId = props.itemId
  const itemName = props.itemName
  const itemPrice = props.itemPrice
  const itemImageUrl = props.itemImageUrl
  const itemUrl = URLS.Backend_BASE_URL + URLS.Item + '/' + itemId

  const navigate = useNavigate()

  return(
    <React.Fragment>
      <div className ='Cart-Items' onClick = {() => navigate(to = itemUrl)}>
        <div className ='image-box'>
            <img src = {itemImageUrl} className ='image-size' />
        </div>
        <div className = 'about'>
          <h3 className ='subtitle'>{itemName}</h3>
        </div>
        <div className = 'counter'>
        </div>
        <div className = 'prices'>
          <div className = 'amount'>{itemPrice}</div>
          
        </div>      
      </div>
    </React.Fragment>
  )
}

export default ItemCell
