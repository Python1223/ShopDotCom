from abc import ABC, abstractmethod

class OrderOperation(ABC):
    '''
    OrderOperation is an Abstract Base Class, from which concrete order operation classes
    are inherited. The concrete class are responsible for editting an itemIdList string
    and returning the editted itemIdList string

    editItemIdList is an abstract method in OrderOperation, which represents the strategy
    that will be used to modify the itemIdList string
    '''
    @abstractmethod
    def editItemIdList()-> str: pass

class AddItemOperation(OrderOperation):
    '''
    AddItemOperation adds a specific itemId to an itemIdList string
    '''

    def __init__(self, itemIdList, itemIns)-> None:
        self.itemIdListString= itemIdList
        self.itemIns= itemIns
        
    def editItemIdList(self)-> str:
        editedItemIdListString= str()
        
        itemInsId= self.itemIns.id
        if len(self.itemIdListString)== 0: editedItemIdListString= str(itemInsId)
        else: editedItemIdListString= "".join([self.itemIdListString, ",", str(itemInsId)])
        return editedItemIdListString

# class DeleteItemOperation(OrderOperation):
#     '''
#     DeleteitemOperation deletes a specific itemId from an itemIdList string
#     Raises Exception if Item instance is not found in the itemIdList string
#     '''
#     def __init__(self, itemIdList, itemIns)-> None:
#         self.itemIdListString= itemIdList
#         self.itemIns= itemIns

#     def editItemIdList(self)-> None:
#         itemInsId= self.itemIns.id
#         itemIdList= self.itemIdListString.split(",")
        
#         itemFoundFlag= False
#         for index, itemId in enumerate(itemIdList):
#             if itemId is str(itemInsId): itemIdList.pop(index); itemFoundFlag= True; break

#         if not itemFoundFlag: raise Exception("Item Instance not found")

#         editedItemIdListString= ",".join(itemIdList); editedItemIdListString= editedItemIdListString[0: -1]
#         return editedItemIdListString

class NoneOperation(OrderOperation):
    '''
    NoneOperation class signifying no effective order operation
    '''

    def __init__(self, itemIdList, itemIns)-> None:
        self.itemIdListString= itemIdList
        self.itemIns= itemIns

    def editItemIdList(self)-> str: return self.itemIdListString
        
class OrderOperationFactory:
    '''
    Factory Class to create Order Operation Instances
    '''
    @staticmethod
    def getOrderOperationIns(orderOperationString, itemIdList, itemIns)-> OrderOperation:
        orderOperationIns= None

        if orderOperationString== 'AddItem':
            orderOperationIns= AddItemOperation(itemIdList= itemIdList, itemIns= itemIns)
        # elif orderOperationString== 'DeleteItem':
        #     orderOperationIns= DeleteItemOperation(itemIdList= itemIdList, itemIns= itemIns)
        else:
            orderOperationIns= NoneOperation(itemIdList= itemIdList, itemIns= itemIns)

        return orderOperationIns
