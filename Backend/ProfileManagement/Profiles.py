from abc import ABC, abstractmethod
from ProfileManagement.models import BuyerProfileModel, SellerProfileModel

class Profile(ABC):
    '''
    Base Profile Abstract Class
    '''
    @abstractmethod
    def save()-> None: pass

class BuyerProfile(Profile):
    '''
    Profile for Buyers
    '''
    __model= BuyerProfileModel
    def __init__(self, userIns)-> None:
        self.__userIns= userIns
        self.__profileType= 'Buyer'
        self.__modelIns= None
        
    def save(self)-> None:
        self.__modelIns= BuyerProfile.__model(  userModelIns= self.__userIns,
                                                profileType= self.__profileType)
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
        self.__modelIns= None

    def save(self)-> None:
        self.__modelIns= SellerProfile.__model( userModelIns= self.__userIns,
                                         storeId= self.__storeId,
                                         storeName= self.__storeName,
                                         profileType= self.__profileType)
        self.__modelIns.save()

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
        