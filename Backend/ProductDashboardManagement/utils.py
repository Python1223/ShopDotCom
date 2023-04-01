import random

def getFilter(totalElements: int, countPositives: int)-> list[bool]:
    filter_: list= [True]* totalElements
    if totalElements<= countPositives: return filter_

    falseIndices= random.sample(range[0, totalElements], countPositives)
    for  index in falseIndices: filter_[index]= False

    return filter_
