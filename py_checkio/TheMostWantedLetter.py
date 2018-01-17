def checkio(text):
    li = sorted([c for c in text.lower() if c.isalpha()])
    res = [[e, li.count(e)] for e in set(li) if li.count(e) > 1]
    # res -> [['b', 3], ['a', 2]]
    
    if len(res) != 0:
        item = res[0]    
        for i, j in enumerate(res):
            if j[1] > item[1]: 
                item = j
            elif (j[1] == item[1]) and (j[0] < item[0]):
                item = j
        
        return item[0]
    else:
        return li[0]
        

# checkio("Hello World!") == "l" 
# checkio("How do you do?") == "o" 
# checkio("One") == "e"
# checkio("Oops!") == "o"
checkio("AAaooo!!!!") == "a"
checkio("abe") == "a"
