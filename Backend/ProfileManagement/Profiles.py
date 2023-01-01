from abc import ABC, abstractmethod
from ProfileManagement.models import BuyerProfileModel, SellerProfileModel
from CartManagement.models import CartModel

class Profile(ABC):
    '''
    Base Profile Abstract Class
    '''
    @abstractmethod
    def save()-> None: pass

    @abstractmethod
    def setProfileResources()-> None: pass

class BuyerProfile(Profile):
    '''
    Profile for Buyers
    '''
    __model= BuyerProfileModel
    def __init__(self, userIns, cartId= -1, purchaseListId= -1, orderListId= -1)-> None:
        self.__userIns= userIns
        self.__cartId= cartId
        self.__purchaseListId= purchaseListId
        self.__orderListId= orderListId
        self.__profileType= 'Buyer'
        self.__modelIns= None
        
    def save(self)-> None:
        self.__modelIns= BuyerProfile.__model( userModelIns= self.__userIns,
                                        cartId= self.__cartId,
                                        purchaseListId= self.__purchaseListId,
                                        orderListId= self.__orderListId,
                                        profileType= self.__profileType)
        self.__modelIns.save()

    def setProfileResources(self)-> None:
        cartIns= CartModel(buyerProfileModelIns= self.__modelIns)
        cartId= cartIns.cartId

        #############
        # Do same for purchaseList and orderList 
        #############

        self.__modelIns.cartId= cartId

        self.__modelIns.save()
        

class SellerProfile(Profile):
    '''
    Profile for Sellers
    '''
    __model= SellerProfileModel
    def __init__(self, userIns, storeName, storeId= -1)-> None:
        self.__userIns= userIns
        self.__storeId= storeId
        self.__storeName= storeName
        self.__profileType= 'Seller'

    def save(self)-> None:
        modelIns= SellerProfile.__model( userModelIns= self.__userIns,
                                         storeId= self.__storeId,
                                         storeName= self.__storeName,
                                         profileType= self.__profileType)
        modelIns.save()

class NoneProfile(Profile):
    '''
    None Class for Profile
    '''
    def __init__(self, *args)-> None: pass

    def save(self)-> None: pass

class ProfileFactory:
    '''
    Factory Class to create Profile Instances
    '''
    @staticmethod
    def getProfileIns(profileString, userIns, storeName)-> Profile:
        profileModelIns= NoneProfile()

        if profileString== 'Buyer': profileModelIns= BuyerProfile(userIns= userIns)
        elif profileString== 'Seller': profileModelIns= SellerProfile(userIns= userIns, storeName= storeName)

        return profileModelIns
        