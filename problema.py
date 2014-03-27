values = [int(n) for n in input().split(" ")]
while values != [0, 0]:
    if values[1] % values[0] == 0:
        print("factor")
    elif values[0] % values[1] == 0:
        print("multiple")
    else:
        print("neither")
    values = [int(n) for n in input().split(" ")]