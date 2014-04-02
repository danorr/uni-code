def my_enumerate(items):
    result = []
    for i in range(0, len(items)):
        temp = [(i, items[i])]
        result.extend(temp)
    return result

print(my_enumerate([10, 20, 30]))
print(my_enumerate(['dog', 'pig', 'cow']))
print(my_enumerate([]))