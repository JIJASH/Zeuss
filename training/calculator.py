def sum(a,b):
    return (a+b)
def diff(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    if b==0:
        return 'Math Error ! Its infinty.. please enter other digits..'
    else:
        return (a/b)
def exp(a,b):
    return(a**b)
while True:
    print('\n')
    print('--------**************---------')
    print("Select the operations : ")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponential")
    print('6.EXIT')
    
    choice=int(input("Enter choice 1 - 6 : "))
    if choice>6:
        print("Invalid input !! Enter between 1 - 6 .")
        break


    if choice in range(1,6):
            a=int(input("Enter first digit : "))
            b=int(input("Enter second digit : "))
    
        
    if choice==1:
        print(f'{a} + {b} = {sum(a,b)}')
    elif choice==2:
        print(f'{a} - {b} = {diff(a,b)}')
    elif choice==3:
        print(f'{a} * {b} = {mul(a,b)}')
    elif choice==4:
        print(f'{a} / {b} = {div(a,b)}')
    elif choice==5:
        print(f'{a} ** {b} = {exp(a,b)}')
    elif choice==6:
        print('thank you !!!')
   


