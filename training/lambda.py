# #always returns function
# def sum_by_ten(a):
#     return a+10
# print(sum_by_ten(2))
# #or
# s=lambda a:a+10
# print(s(10))#lambda function lai normal function jastai call matra garna mildaina cauze yesle jailei return garxa so print ma halnai parxa

# x=lambda a,b:a*b
# print(x(5,6))

def myfunc(n):
    return lambda x:x*n
doubler=myfunc(2)#yesle my func(n) call garyo so lambda function store bhayo doubler ma
print(doubler(10))#doubler is just a variable
doubler=myfunc(3)#triples the value
tripler=myfunc(3)
print(doubler(10))
print(tripler(10))
