T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    F = N % H
    R = (N // H) + 1

    if F == 0:
        F = H
        R -= 1

    print(F * 100 + R)


