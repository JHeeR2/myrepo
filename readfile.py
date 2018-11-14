import os
os.chdir('C:\\Users\\d104-1\\Desktop\\work')

name = input('? ')

with open("phone.txt") as f:
    lines = f.readlines()

for k in lines:
    a = k.split(',')
    if a[0] == name:
        print(a)
