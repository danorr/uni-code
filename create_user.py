'''A program to receive user input, create user details and return the created
user details'''

import usernames

def create_user():
    # Request input from user and assign to variables
    
    first_name = input("Please enter the first name: ").strip()
    last_name = input("Please enter the last name: ").strip()
    
    # create full name from inputs
    full_name = first_name + " " + last_name
    
    # create the random number from random_int method (str(int))
    rand_num = str(usernames.random_int(full_name))
    
    # create a lowercase username using inputs and rand_num
    username = (first_name[0] + last_name[:2] + rand_num).lower()

    # create a temporary password using the method from usernames
    temp_password = usernames.get_temporary_password(full_name)
    
    last_name_length = len(last_name)
    factor = 0.05
    #balance = last_name_length * factor
    
    card_balance = (last_name_length * factor + 10)
    
    # output
    print()
    print("{0} {1}".format("Full name:", full_name))
    print("{0} {1}".format("Suggested username:", username))
    print("{0} {1}".format("Suggested password:", temp_password))
    print("{0} {1:.2f}".format("Lucky card balance:", card_balance))
    
create_user()