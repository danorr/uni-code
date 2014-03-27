rainfalls = [[0, 9, 3, 7],[11, 9, 0, 0],[0, 10, 12, 20],[0, 0, 0, 0],
                [1, 3, 4, 1],[2, 8, 10, 10],[0, 0, 0, 0]]
print("Rainfall Data")
for day in [0, 1, 2, 3, 4, 5, 6]:
    print("Day {}:".format(day), end='') # NB the use of 'end'
    for column in [0, 1, 2, 3]:
        print("{:4}".format(rainfalls[day][column]), end='')
    print()