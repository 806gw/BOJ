a = int(input())
c = []
for i in range(a):
    b = int(input())
    if b != 0:
        c.append(b)
    elif b == 0:
        c.pop()
print(sum(c))