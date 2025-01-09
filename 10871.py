a, b = map(int, input().split())
c = list(map(int, input().split()))
# 배열안에 입력값을 ['1', '2', '3', '4', '5'] 넣지만, map(int, ...)으로 인하여 [1, 2, 3, 4, 5] 으로 변환된다.

for i in range(a):
    if c[i] < b:
        print(c[i], end = " ")