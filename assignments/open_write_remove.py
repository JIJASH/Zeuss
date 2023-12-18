try:
    a=input('Enter the name of the file you want to create : ')
    with open (a,'x') as p:
        print('Do you wanna write in this file ?')
        choice=int(input('Enter 1 if you wanna write otherwise 2 if you dont wanna write anything : '))
        if choice==1:
            b=input('Enter something you wanna write : ')
            p.write(b)
        else:
            print('')
except Exception as e:
    print('Name with this file already exit !!! Please try to enter other names for your file',e)
print('Do you wanna delete any files ?')
choice1=int(input('Enter 1 if you wanna delete any file otherwise 2 : '))
if choice1==1:
    d=input('Énter name of file you wanna delete : ')
    try:
        import os
        os.remove(d)
    except ValueError:
        print('Your File Doesnot Exit !!!')
else:
    print('Thank you !!')
    exit

