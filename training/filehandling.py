# p=open('text.txt')
# print(p.read())

# with open ('text.txt') as p:
#     print(p.readlines()[0])

with open ('text.txt','a') as p:#append method and append le file nabhayeni aafai create gardiye append gardinxa
    p.write('\n added later from python')

#inport function
# from module import Sum#yedi yo particular file ko bhitra aru diff functions pani accces garnu paryo bhaney from mdule import*

# print(Sum(1,2))


# #yedi sam ename ko function duita file ma xa ani acces garnu paryo bhaney yeuta ko lai as s bhanera access garauney ani arko lai chai tyo name le nai garauney
# from module import Sum as s
# from practise import Sum
# print(Sum(1,2))
# print(s(4,5))

#delete a created file
from time import sleep
with open ('text.txt','w') as p:#with open le 
    p.write('\n added later from python')
sleep(10)
import os 
os.remove('text.py')

#calculator refactor


