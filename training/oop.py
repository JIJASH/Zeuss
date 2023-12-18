class House:
    
    window=1
    door=1
    color='red'
    
    #constructor///MEGICCCC METHODDD////Dunder Methodd
    def __init__(self):#Constructor ko method haru aafai call hunxa..class ko method jastai chai call garirakhna paradaina
        print('MY HOUSE')
    def __init__(self,name='Jijash',window=2,door=2,color='grey'):#task///price thapera 3..4 jana ko ghar ko price cmpr ki kasko mahango xa bhanera
        self.name=name
        self.window=window
        self.door=door
        self.color=color
    
    
    def __str__(self) -> str:
        return f'{self.name} ko ghar'
    
    
    def __eq__(self,value) -> bool:
        return self.window==value.window
    
    def __gt__(self,value) -> bool:
        return self.window==value.window
    
    def set_color(self,color):#yaa ko color chai function ko color ho
        self.color=color#yaa ko self .color chai mathi class ko color hooo
    def get_color(self):
        return self.color#mathi clss ko color lai return hanxa
ram_ko_ghar=House()#House ko object creation
shyam_ko_ghar=House(window=12,color='white')#yo methodd ma pass gareko arguments mathi constructor ma gayera overwrite or assign hunxa
ram_ko_ghar.color='Green'
#or
ram_ko_ghar.set_color('blue')
print(ram_ko_ghar.get_color())
print(shyam_ko_ghar.get_color())
print(ram_ko_ghar)
# print(ram_ko_ghar.window)
# print(shyam_ko_ghar.color)
is_name=ram_ko_ghar.__eq__(shyam_ko_ghar)
gt=ram_ko_ghar.__gt__(shyam_ko_ghar)
print(is_name)
print(gt)