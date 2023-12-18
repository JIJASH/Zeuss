class Grandfather(object):
    
    def __init__(self) -> None:
        print('Bajeko ghar')
    house='Luxury'
    
    def get_house(self):
        return self.house
    
class Grandmother:
    jwellery='sunn'
class Father(Grandfather,Grandmother):#multipple inheritance
            
    car='Mercedes'
    
    def get_house(self):
        print (super().get_house())
        return 'Jhan babball ghar'
    
class Son(Father):#multilevel inheritance
    console='PS5'
father=Father()
print(father.get_house())
# son=Son()
# print(father.car)
# print(father.house)
# print(father.jwellery)
# print(son.console)
# print(son.house)

# print(isinstance(son,object))