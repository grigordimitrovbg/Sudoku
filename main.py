import numpy as np


result=0
def possible(x,y,n):
    global MyMatrix
    for i in range(9):
        if MyMatrix[x][i]==n:
            return False
    for i in range(9):
        if MyMatrix[i][y] == n:
            return False
    for i in range(3):
        for j in range(3):
            if MyMatrix[(x//3)*3+i][(y//3)*3+j]==n:
                return False
    return True

def solve():
    global MyMatrix
    global result
    for i in range(9):
        for j in range(9):
            if MyMatrix[i][j]==0:
                for n in range(1,10):
                    if possible(i,j,n):
                        MyMatrix[i][j]=n
                        solve()
                        MyMatrix[i][j]=0
                return
    result += (100*MyMatrix[0][0]+10*MyMatrix[0][1]+MyMatrix[0][2])

f = open('input.txt','r')

NewMatrix= list()

for line in f:
    if "Grid" in line:
        continue
    for i in line[0:-1]:
        NewMatrix.append(int(i))
for i in range(50):
    MyMatrix=NewMatrix[81*i:81*(i+1)]
    MyMatrix= np.array(MyMatrix)
    MyMatrix =MyMatrix.reshape(9,9)
    solve()
print(result)

