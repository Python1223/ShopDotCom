from ProfileManagement.models import ProfileModel

class ProfileFactory:

    @staticmethod
    def getProfileModelIns(profileString: str)-> ProfileModel:
        profileModelIns= None

        if profileString== "Buyer": profileModelIns= BuyerProfileModel(args)
        elif profileString== "Seller": profileModelIns= SellerProfileModel(args)

        return profileModelIns