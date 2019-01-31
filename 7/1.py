f = open('number.txt', 'wt')

for i in range(11):
    if i <1:
        pass
    else:
        f.write(str(i) + '\n')
f.close()
