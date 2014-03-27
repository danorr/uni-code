number_towns = int(input())
week_num = 1
while number_towns != 0:
    towns = set()
    for n in range(number_towns):
        towns.add(input())
        
    print("Week", week_num, len(towns))
    number_towns = int(input())
    week_num = week_num + 1
    
    
    