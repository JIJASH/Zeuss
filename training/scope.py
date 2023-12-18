# a=10
# def number():
#     print(a)#paila a lai function ma khojxa..xaina bhaney global variable lai access garxa
# number()

# a=10
# def number():
#     global a#mathi ko global variable lai function ko local variable le overwrite garxaa
#     a=11
#     print(a)
# number()
# print(a) 

# a=10
# def outer():
#     a=11
#     def inner():
#         a=12
#         print('inner sees a as',a)
#     inner()
#     print('outer sees a as ',a)
# print('main sees a as ',a)
# outer()

# a=10
# def outer():
#     a=11
#     def inner():
#         global a
#         # a=12
#         print('inner sees a as',a)
#     inner()
#     print('outer sees a as ',a)
# outer()
# print('main sees a as ',a)
     
