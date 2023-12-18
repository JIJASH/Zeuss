class Person:
    def __init__(self,name,age,password) -> None:
        self.name=name#public variable
        self._age=age#protected
        self.__password=password#private
        
    # def get_password(self):#private variable ko data access garna lai getter setter we need
    #     return self.__password
    # def set_password(self,password):
    #     self.__password=password
    
    # password=property(get_password,set_password)
    @property#yo decorator le chai getter lai siddai define handinxa ...call garirakhna parena
    def password(self):#private variable ko data access garna lai getter setter we need
        return self.__password
    @password.setter#yo decorator le setter lai call hanxa..matho jastai xuttai setter call hanna parena
    def password(self,password):
        self.__password=password
        
person=Person('ram',12,'1234')
print(person.name)
print(person._age)
# print(person.get_password())
# person.set_password('5678')
# print(person.get_password())
print(person.password)
person.password=5678
print(person.password)