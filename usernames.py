"""Provides some random fun for username and password generation"""
import random

# A constant used for selecting letters of the alphabet
LETTERS = "abcdefghijklmnopqrstuvwxyz"

def random_int(full_name_string):
    """Returns a quasi-random integer between 1 and 999"""
    the_hash = hash(full_name_string)
    result = the_hash % 1000
    # 0 might get mistaken for an O (Oh dear) so change it to 1
    if result == 0:
        result = 1
    return result

def get_temporary_password(full_name_string):
    """Returns a quasi-random password based on the full name string."""
    the_seed = hash(full_name_string)
    random.seed(the_seed)
    password = LETTERS[random.randrange(26)]
    password += LETTERS[random.randrange(26)]
    password += str(random.randrange(10))
    password += LETTERS[random.randrange(26)]
    password += LETTERS[random.randrange(26)]
    password += str(random.randrange(10))
    return password




def _c_mul(a, b):
    """Substitute for c multiply function.
    Don't worry you don't need to understand this!"""
    return eval(hex((int(a) * b) & 0xFFFFFFFF)[:-1])

def hash(name):
    """Takes a name name and returns a hash number based on the name.
    Don't worry, you don't need to understand this!"""
    if name is None:
        return 0 # empty
    value = ord(name[0]) << 7
    for char in name:
        value = _c_mul(1000003, value) ^ ord(char)
    value = value ^ len(name)
    if value == -1:
        value = -2
    return value
    

if __name__ == '__main__':
    """Some testing code - This won't run when you import this module."""
    test1 = random_int("Wiggles")
    print('A pseudo-random number between 1 and 999 =',str(test1))
    test2 = random_int("Woggles")
    print('A pseudo-random number between 1 and 999 =',str(test2))
    test3 = get_temporary_password("Mr Blobby")
    print('A pseudo-random pasword =',test3)
    print('The above above values should be the same every time you run this')
    print('program. So they aren\'t really random... which helps with testing.')