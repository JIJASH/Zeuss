
# while True:
#     try:
        
#         num1=int(input('Enter two numbers : '))
#         num2=int(input('enter two numbers : '))
#         print(num1/num2)
#     except ZeroDivisionError:
#         print('Cannot divide any number by zero')
#     except Exception as e :
#         print(e)
#     except ValueError:
#         print('Invalid input! INput must be integer')
#     except Exception as e :
#         print('Something went wrong',e)#yedi aru errors haru thaha bhayena bhaney yesto lekhney ani aafai khojera dinxa
        
def divider():
    num1=int(input('Enter two numbers : '))
    num2=int(input('enter two numbers : '))
    if num1==5:
        raise Exception('Input cannot be 5')
    print(num1/num2)
while  True:
    try:
        divider()
    except ZeroDivisionError:
        print('Cannot divide any number by zero')
    except Exception as e :
        print('Something went wrong',e)
        