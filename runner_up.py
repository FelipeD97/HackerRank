

n = int(input())

arr1 = list(map(int,input().strip().split()))[:n]

x = max(arr1)

while max(arr1) == x:
    arr1.remove(max(arr1))

print(arr1)

print(max(arr1))