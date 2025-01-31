arr = [0] * 10

for i in range(10):
    n = int(input())
    arr[i] = n % 42

print(len(set(arr)))