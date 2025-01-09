a = int(input())

for i in range(0, a): # 0부터 a까지 반복
    b, c = 0, 1
    d = list(input())
    for j in d: # d에 들어간 입력값들이 순서대로 j에 대입된다.
        if j == 'O':
            b += c
            c += 1
        else:
            c = 1
    print(b)