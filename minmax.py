def findMax(arr, n):
    max = -1
    max_i = -1
    for i in range(n):
        for j in range(n):
            if arr[i][j] > max:
                max = arr[i][j]
                max_i = i
    return max, max_i

def findMin(arr, n, max_i=-1):
    min = 1000000
    min_i = -1
    for i in range(n):
        if max_i != -1 & i == max_i:
            continue
        for j in range(n):
            if arr[i][j] < min:
                min = arr[i][j]
                min_i = i
    return min, min_i

n, b = map(int,input().split())

arr = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    x = list(map(int,input().split()))
    for j in range(n):
        arr[i][j] = x[j]
        
max, max_i = findMax(arr, n)

# print ("Max = ", max)
# print ("Max Line = ", max_i)

# print("Before:")
# print(arr)

for j in range(n):
    arr[max_i][j] += b

# print("After plus:")
# print(arr)

min, min_i = findMin(arr, n, max_i)

# print ("Min = ", min)
# print ("Min Line = ", min_i)

for j in range(n):
    arr[min_i][j] -= b

# print("After minus:")
# print(arr)

max, max_i = findMax(arr, n)
min, min_i = findMin(arr, n)

print ("Output:", max - min)