list_1 = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
list_2= []
list_3= []

def asdf(listA):
    result = []
    for item in listA:
        result.extend(item)
    return sorted(result)

print(asdf(list_1))



for items in list_1 :
    if items == [] :
        x =list_1.index(items)
        list_1.pop(x)
        list_2 = list_1
    for item in list_2 :
        list_3 = sorted(item) #list3=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]

print(list_3)
        
    
        
         




    

