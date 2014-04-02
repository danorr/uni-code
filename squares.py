#def squares(n):
    #''' return a list of squares from 1 to n + 1 '''
    
    #list_squares = []
    #for i in range(1, n + 1):
        #list_squares.append(i ** 2)
    #return list_squares


''' list comprehension option'''
def squares(n):
    ''' return a list of squares from 1 to n + 1 '''
    
    list_squares = [i for i in range(1, n +1) list_squares[i] * i]
    
    return list_squares

#def squares(n):
    #result = []
    #for i in range(0, n+1):
        #result[i] = result[i] * i
    #return result

print(squares(4))
print(squares(1))
print(squares(0))