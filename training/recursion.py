# def number(num=0):
#     print(num)
#     print(num+1)
# number()

#range in recursion

# for i in range(1,4):
#     print(i)
n=int(input('Enter any number : '))  
def recursion(n):
    # n=int(input('Enter any number : '))
    if n<1:
        return ('...')
    else:
       recursion(n-1)
       print(n-1)
recursion(n)