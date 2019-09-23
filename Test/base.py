for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(i) + '*' + str(j) + '=' + str(i * j), end=' ')
    print('')

print('-------------------------------------------------------------')

for i in range(9, 0, -1):
    for j in range(i, 0, -1):
        print('%d*%d=%2d' %(i,j,i*j), end=' ')
    print()

print('-------------------------------------------------------------')

n=9
for i in range(n,0,-1):
    for j in range(1,n+1):
        print(str(j) + '*' + str(i) + '=' + str(j * i), end=' ')
        # m-=1
    n-=1
    print()

print('-------------------------------------------------------------')

for i in range(0,21):
    for j in range(0,21):

        print(str(i) + '+' + str(j) + '=' + str(i+j), end=' ')
    print()
