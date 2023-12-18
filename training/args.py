# def sum(*args):
#   total=0
#   for number in args:
#     total+=number
#   print(total)
# sum(1,2,3,4)
  
# create  a function which takes names of persom and print the names of each individual tyo ni my name is smth bhanera

def person(*names):
  for name in names:
    print(f'My name is {name}')
person('Jijash','Suyashh','Sammm','Sadill')
  