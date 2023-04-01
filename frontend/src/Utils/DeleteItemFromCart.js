import {useNavigate} from 'react-router-dom'
import URLS from '../urls'

const CartUrl = URLS.Backend_BASE_URL + URLS.Cart

const deleteItemFromCart = (event, itemId) => {

  event.preventDefault()
  const navigate = useNavigate()

  const handleResponse = (response) => navigate(to = CartUrl)

  const handleError = (error) => console.log('Error while deleting item from cart', error)

  const deleteFromCartUrl = CartUrl + '/DeleteItem/' + itemId
  const headers = {'Authorization': 'Bearer ' + localStorage.getItem('accessToken')}
  
  axios({method: 'patch', url: deleteFromCartUrl, headers: headers}).then(handleResponse, handleError)
}

export default deleteItemFromCart
