import os

path = input("enter path: ")

f = open('flist.txt', 'wt')

filenames = os.listdir(path)
for filename in filenames:
    f.write(filename + '\n')
