from abc import ABC, abstractmethod
from ProfileManagement.models import BuyerProfileModel, SellerProfileModel
from CartManagement.models import CartModel
from OrderManagement.models import OrderListModel
from PurchaseManagement.models import PurchaseListModel
from StoreManagement.models import Store

class Profile(ABC):
    '''
    Base Profile Abstract Class
    '''
    @abstractmethod
    def setProfileResources()-> None: pass
class BuyerProfile(Profile):
    '''
    Profile for Buyers
    '''
    __model= BuyerProfileModel
    def __init__(self, userIns)-> None:
        self.__userIns= userIns
        self.__profileType= 'Buyer'
        self.__modelIns= BuyerProfile.__model(userIns= self.__userIns, profileType= self.__profileType)
        self.__modelIns.save()

    def setProfileResources(self)-> None:
        cartIns= CartModel(buyerProfileIns= self.__modelIns)
        cartIns.save(); cartId= cartIns.cartId
        orderListIns= OrderListModel(buyerProfileIns= self.__modelIns)
        orderListIns.save(); orderListId= orderListIns.orderListId
        purchaseListIns= PurchaseListModel(buyerProfileIns= self.__modelIns)
        purchaseListIns.save(); purchaseListId= purchaseListIns.purchaseListId

        return cartId, orderListId, purchaseListId
class SellerProfile(Profile):
    '''
    Profile for Sellers
    '''
    __model= SellerProfileModel
    def __init__(self, userIns, storeName)-> None:
        self.__userIns= userIns
        self.__storeName= storeName
        self.__profileType= 'Seller'
        self.__modelIns= SellerProfile.__model(userIns= self.__userIns, profileType= self.__profileType)
        self.__modelIns.save()

    def setProfileResources(self)-> None:
        storeIns= Store(storeName= self.__storeName, sellerProfileIns= self.__modelIns)
        storeIns.save(); storeId= storeIns.storeId
        return storeId

class NoneProfile(Profile):
    '''
    None Class for Profile
    '''
    def __init__(self, *args)-> None: pass

    def setProfileResources() -> None: pass

class ProfileFactory:
    '''
    Factory Class to create Profile Instances
    '''
    @staticmethod
    def getProfileIns(profileString, userIns, storeName)-> Profile:
        profileIns= NoneProfile()

        if profileString== 'Buyer': profileIns= BuyerProfile(userIns= userIns)
        elif profileString== 'Seller': profileIns= SellerProfile(userIns= userIns, storeName= storeName)

        return profileIns
        