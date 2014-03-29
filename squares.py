def squares(n):
    list_squares = []
    for i in range(1, n+1):
        list_squares.append(i ** 2)
    return list_squares

print(squares(4))
print(squares(1))
print(squares(0))