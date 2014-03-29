def ends_with_any(s, endings):
    it_ends = False
    index = 0
    #for char in endings:
        #if s[-1] == char:
            #it_ends = True
        #else:
            #it_ends = False
    while not it_ends and index < len(endings):
        if s[-1] == endings[index]:
            it_ends = True
        index += 1
    return it_ends
    
print(ends_with_any("Hi!", ['.', ';', '!', ';'])) # True
print(ends_with_any("Hello", ['.', ';', '!', ';'])) # False