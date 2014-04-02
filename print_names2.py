def print_names2(people):
    ''' Convert the following code from for loops to while loops:
    def print_names2(people):
    for person in people:
        to_print = ""
        for name in person:
            to_print += name + " "
        print(to_print)
    '''
    outer = 0
    while outer < len(people):
        to_print = ""
        inner = 0
        while inner < len(people[outer]):
            to_print += people[outer][inner] + " "
            inner += 1
        to_print = to_print.strip()
        print(to_print)
        outer += 1

print_names2([['John', 'Smith'], ['Mary', 'Keyes'], ['Jane', 'Doe']])
print_names2([['Bilbo', 'Baggins'], ['Gollum'], ['Tom', 'Bombadil'], ['Aragorn']])
