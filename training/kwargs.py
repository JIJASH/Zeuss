def person(**details):
    print(f'''Hello !!!
My name is {(details['name'])}''')
    print(f'My age is {(details['age'])}')
    print(f'I live in {(details['address'])}')
    print(f'My hobbies are {(details['hobby'])}')
person(name='Jijash Shrestha',age=20,address='Patan Sundhara',hobby='Playing and traveling')
# add more attribute and print in the structure
