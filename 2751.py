import sys

a = int(sys.stdin.readline())
c = []

for i in range(0, a):
    b = int(sys.stdin.readline())
    c.append(b)

print(*sorted(c), sep='\n')