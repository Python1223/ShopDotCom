from abc import ABC, abstractmethod

class StoreOperation(ABC):
  
    @abstractmethod
    def editItemIdList(): pass

class AddItemOperation(StoreOperation):

    def __init__(self, itemIdList, itemIns):
        self.itemIdListString= itemIdList
        self.itemIns= itemIns
        
    def editItemIdList(self):
        editedItemIdListString= str()
        
        itemInsId= self.itemIns.id
        if len(self.itemIdListString)== 0: editedItemIdListString= str(itemInsId)
        else: editedItemIdListString= "".join([self.itemIdListString, ",", str(itemInsId)])
        return editedItemIdListString

class DeleteItemOperation(StoreOperation):

    def __init__(self, itemIdList, itemIns):
        self.itemIdListString= itemIdList
        self.itemIns= itemIns

    def editItemIdList(self):
        itemInsId= self.itemIns.id
        itemIdList= self.itemIdListString.split(",")
        
        itemFoundFlag= False
        for index, itemId in enumerate(itemIdList):
            if itemId is str(itemInsId): itemIdList.pop(index); itemFoundFlag= True; break

        if not itemFoundFlag: raise Exception("Item Instance not found")

        editedItemIdListString= ",".join(itemIdList); editedItemIdListString= editedItemIdListString[0: -1]
        return editedItemIdListString

class NoneOperation(StoreOperation):

    def __init__(self, itemIdList, itemIns):
        self.itemIdListString= itemIdList
        self.itemIns= itemIns

    def editItemIdList(self): return self.itemIdListString
        
class StoreOperationFactory:

    @staticmethod
    def getStoreOperationIns(storeOperationString, itemIdList, itemIns):
        storeOperationIns= None

        if storeOperationString== 'AddItem':
            storeOperationIns= AddItemOperation(itemIdList= itemIdList, itemIns= itemIns)
        elif storeOperationString== 'DeleteItem':
            storeOperationIns= DeleteItemOperation(itemIdList= itemIdList, itemIns= itemIns)
        else:
            storeOperationIns= NoneOperation(itemIdList= itemIdList, itemIns= itemIns)

        return storeOperationIns
