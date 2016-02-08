def sequential_search(items, item):
    count = 0
    found = False
    length = len(items)
    
    while count < length and not found:
        if items[count] == items:
            found = True
        else:
            count = count + 1
        
    return found