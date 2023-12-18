from abc import ABC, abstractmethod

class Computer(ABC):
    
    def run(self,app):
        self.process(app)
    @abstractmethod
    def process(self):
        pass

    
class Mobile(Computer):
    def process(self,app):
        print('mobile is runnning',app)

class Laptop(Computer):
    def process(self,app):
        print('laptop is runnning',app)
samsung=Mobile()
hp=Laptop()
hp.run('VS code')
samsung.run('PUBG')    
    