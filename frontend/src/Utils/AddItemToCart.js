import {useNavigate} from 'react-router-dom'
import URLS from '../urls'

const CartUrl = URLS.Backend_BASE_URL + URLS.Cart

const addItemToCart = (event, itemId) => {

  event.preventDefault()
  const navigate = useNavigate()

  const handleResponse = (response) => navigate(CartUrl)

  const handleError = (error) => console.log('Error while adding item in cart', error)

  const addToCartUrl = CartUrl + '/AddItem/' + itemId
  const headers = {'Authorization': 'Bearer ' + localStorage.getItem('accessToken')}
  
  axios({method: 'patch', url: addToCartUrl, headers: headers}).then(handleResponse, handleError)
}

export default addItemToCart
