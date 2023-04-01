from abc import ABC, abstractmethod


class CartOperation(ABC):
    """
    CartOperation is an Abstract Base Class, from which concrete cart operation classes
    are inherited. The concrete class are responsible for editing an itemIdList string
    and returning the edited itemIdList string

    editItemIdList is an abstract method in CartOperation, which represents the strategy
    that will be used to modify the itemIdList string
    """
    
    @abstractmethod
    def editItemIdList(self) -> str: pass


class AddItemOperation(CartOperation):
    """AddItemOperation adds a specific itemId to an itemIdList string"""

    def __init__(self, itemIdList, itemIns) -> None:
        self.itemIdListString = itemIdList
        self.itemIns = itemIns
        
    def editItemIdList(self) -> str:
        editedItemIdListString = str()
        
        itemInsId= self.itemIns.id
        if len(self.itemIdListString) == 0:  editedItemIdListString= str(itemInsId)
        else: editedItemIdListString= "".join([self.itemIdListString, ",", str(itemInsId)])
        return editedItemIdListString

class DeleteItemOperation(CartOperation):
    '''
    DeleteitemOperation deletes a specific itemId from an itemIdList string
    Raises Exception if Item instance is not found in the itemIdList string
    '''
    def __init__(self, itemIdList, itemIns)-> None:
        self.itemIdListString= itemIdList
        self.itemIns= itemIns

    def editItemIdList(self)-> None:
        itemInsId= self.itemIns.id
        itemIdList= self.itemIdListString.split(",")
        
        itemFoundFlag= False
        for index, itemId in enumerate(itemIdList):
            if itemId is str(itemInsId): itemIdList.pop(index); itemFoundFlag= True; break

        if not itemFoundFlag: raise Exception("Item Instance not found")

        editedItemIdListString= ",".join(itemIdList); editedItemIdListString= editedItemIdListString[0: -1]
        return editedItemIdListString

class NoneOperation(CartOperation):
    '''
    NoneOperation class signbifying no effective cart operation
    '''

    def __init__(self, itemIdList, itemIns)-> None:
        self.itemIdListString= itemIdList
        self.itemIns= itemIns

    def editItemIdList(self)-> str: return self.itemIdListString
        
class CartOperationFactory:
    '''
    Factory Class to create Cart Operation Instances
    '''
    @staticmethod
    def getCartOperationIns(cartOperationString, itemIdList, itemIns)-> CartOperation:
        cartOperationIns= None

        if cartOperationString== 'AddItem':
            cartOperationIns= AddItemOperation(itemIdList= itemIdList, itemIns= itemIns)
        elif cartOperationString== 'DeleteItem':
            cartOperationIns= DeleteItemOperation(itemIdList= itemIdList, itemIns= itemIns)
        else:
            cartOperationIns= NoneOperation(itemIdList= itemIdList, itemIns= itemIns)

        return cartOperationIns
