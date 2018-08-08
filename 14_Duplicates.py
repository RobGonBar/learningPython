# This takes a list and removes the duplicates, then outputs a new list
list = [1,2,2,7,4,3,4,8,12,1,3,4,5]

#using a list
def removeDuplicates(list):
    newList = []
    for x in list:
        if x in newList:
            continue
        else:
            newList.append(x)
    newList.sort()
    return newList

#using a set
def noDuplicates(list):
    newSet = set()
    for x in list:
        newSet.add(x)
    return newSet
    
print(list)
print(removeDuplicates(list))
print(noDuplicates(list))
