data = input().split(" ")
while data != ["#"]:
    c = 0
    t = 0
    for char in data:
        if char in ['2', '4', '6', '8', '10']:
            t += 1
        elif char in ['A', '3', '5', '7', '9']:
            c += 1
    if t>c:
        print("Tania")
    elif c>t:
        print("Cheryl")
    else:
        print("Draw")
    data = input().split()