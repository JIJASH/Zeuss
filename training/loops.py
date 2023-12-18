#while loop

# i=0
# while i<=10:
#    # print('hello')
#     print(f'{i} hello')
#     if i==5:
#         break
#     i+=1

#for loop
fruits=[
    'apple',
    'banana',
    'orange',
    123,
    1.5
]
# print('apple' in fruits)#checks whether apple is in fruits or not


# for fruits in fruits:#sabbai bhanda suru ma fruits ko first element aunxa and next line ma print ani feri mathi jada next element aunxxa and so oonn
#     print(fruits)
    
# for index,fruits in enumerate(fruits):
#     print(index,fruits)
    
# numbers=list(range(10))
# print(numbers)
# numbers=list(range(1,10,2))
# print(numbers)

# for i in range(10):
#     print(i)
#     if i==5:
#         break

# for i in range(1,20):
#     if i%2==0:
#         print(i , 'is even')# or print(f'{i} is even')
#     else:
#         print(i, 'is odd')
        
#task
#1
#12
#123 use for and while

# words='hello world'
# for char in words:
#     print(char)
    
for i in range(1,4):
    for j in range(1,i+1):
        print(j,end=' ') 
    print('')
  