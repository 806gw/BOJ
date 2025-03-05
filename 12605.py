a = int(input())
for i in range(a):
    b = list(map(str, input().split()))
    c = b[::-1]
    print("Case #", i + 1, ": ", end='', sep='')
    for j in c:
        print(j, end=' ')
    print("")