data = [int(n) for n in input().split(" ")]
while data != [0,0]:
    grid = []
    for i in range(data[0]):
        grid.append([])
        for j in range(data[1]):
            grid[i].append(0)
#    grid[x][y]
    
    count = int(input())
    
    for n in range(count):           
        coords = [int(n) for n in input().split(" ")]
        grid[coords[0]][coords[1]] += 1

    next_count = int(input())
    items_found = 0
    
    for n in range(next_count):           
        coords = [int(n) for n in input().split(" ")]
        items_found += grid[coords[0]][coords[1]]
        
    print(items_found)
    data = [int(n) for n in input().split(" ")]