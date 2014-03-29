def print_sqrs_1_to_n(n):
    result = ""
    if n <=0:
        print("ERROR: n must be at least 1.")
    else:
        for i in range(1, n+1):
            temp = i * i
            print("{} * {} = {}\r".format(i,i,temp))
            
print_sqrs_1_to_n(0)