list = [9,5,7,8,0,2,4,3,1,6]

sorted = False

while not sorted:
    sorted = True
    l = len(list) - 1
    
    for i in range(l):
        if list[i] > list[i + 1]:
            sorted = False
            list[i], list[i + 1] = list[i + 1], list[i]
            
print list