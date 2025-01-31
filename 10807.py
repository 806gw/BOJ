n = int(input())
v = list(map(int, input().split()))
a = int(input())
b = 0

for i in v:
    if i == a:
        b += 1
    else:
        b += 0
print(b)