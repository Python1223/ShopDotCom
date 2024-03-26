from django.db import models
from ProfileManagement.models import SellerProfileModel
from django.core.validators import MinValueValidator, MaxValueValidator
# from Backend.settings import EMBEDDING_URL

ITEM_CATEGORY: dict = {
    0: 'Blazer',
    1: 'Blouse',
    2: 'Cardigan',
    3: 'Hoodie',
    4: 'Jacket',
    5: 'Sweater',
    6: 'Tank',
    7: 'Tee',
    8: 'Top',
    9: 'Jeans',
    10: 'Joggers',
    11: 'Leggings',
    12: 'Shirt',
    13: 'Skirt',
    14: 'Strapless Dress',
    15: 'Jumpsuit',
    16: 'Others'
}

DEFAULT_DESTINATION_IMAGE_URL= 'items/defaultItem.jpg'

def getDestinationImageUrl(instance, filename)-> str:
    '''Returns Image Url based on category'''
    global ITEM_CATEGORY

    itemCategoryString: str= ITEM_CATEGORY.get(instance.itemCategory)
    destinationImageUrl: str= ''.join(['Items/', itemCategoryString, '/', filename])
    return destinationImageUrl

#def getDestinationImageEmeddingUrl(item)-> str:
#    '''Returns Image Embedding Url based on category'''
#    global ITEM_CATEGORY
#
#    itemCategoryString: str= ITEM_CATEGORY.get(item.itemCategory)
#    destinationImageEmbeddingUrl: str= "".join([EMBEDDING_URL, itemCategoryString, '/', str(item.itemId), '.txt'])
#    return destinationImageEmbeddingUrl
    
class ItemModel(models.Model):
    '''Model class for Item'''
    global DEFAULT_DESTINATION_IMAGE_URL

    itemId = models.AutoField(primary_key= True)
    itemName = models.CharField(max_length= 100, default=str())
    itemDetails = models.CharField(max_length= 1000, default=str())
    itemPrice = models.PositiveIntegerField(default= 0, validators= [MinValueValidator(0)])
    sellerProfile = models.ForeignKey(to= SellerProfileModel, on_delete= models.CASCADE, null= True)
    itemCategory = models.PositiveIntegerField(validators= [MinValueValidator(0), MaxValueValidator(16)], default=0)
    itemImage = models.ImageField(upload_to= getDestinationImageUrl, default= DEFAULT_DESTINATION_IMAGE_URL, blank= False)
    itemEmbeddingUrl = models.FileField(upload_to="aa", default="aa", blank=False)
    itemLabel = models.IntegerField(default=-1)

#class ItemEmbeddingModel(models.Model):
#    '''Model class for Item Embedding'''
#
#    item= models.OneToOneField(to= ItemModel, on_delete= models.CASCADE)
#    itemEmbeddingUrl= models.CharField(getDestinationImageEmeddingUrl(item), default='', max_length= 100)    
