def star(func):#decorator le sadhai function lai argument linxa
    def wrapper():
        print('*'*10)
        func()
        print('*'*10)
    return wrapper
def hashh(func):
    def wrapp():
        print('#'*10)
        func()
        print('#'*10)
    return wrapp
#@hashh    
#@star
def hello():
    print('hello')
# @hashh
# @star 
def world():
    print('world')

# hello()
# world()
hashh(star(hello))()
# star(hello)()


