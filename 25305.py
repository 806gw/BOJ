a, b = map(int, input().split())
c = list(map(int, input().split()))
c.sort(reverse=True)
print(c[b - 1])