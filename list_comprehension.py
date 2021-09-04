
x = int(input())
y = int(input())
z = int(input())
n = int(input())

array = []

for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            array.append([i,j,k])
            if i + j + k == n:
                array.remove([i,j,k])
print(array)