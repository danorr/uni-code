def count_evens(numbers):
    counter = 0
    for num in numbers:
        if is_even(num):
            counter += 1
    return "{}: {}".format("Number of Evens", counter)

def is_even(num):
    return num % 2 == 0

def odds_squared(numbers):
    result = []
    for num in numbers:
        if not is_even(num):
            result.append(num * num)
    return result
        
            
print(count_evens([2, 1, 2, 3, 4])) #3
print(count_evens([2, 2, 0])) #2
print(odds_squared([1, 2, 3, 5, 7, 9]))