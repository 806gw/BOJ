check = [0] * 31

for i in range(28):
    n = int(input())
    check[n] = 1

answer = []
for j in range(1, 31):
    if check[j] == 0:
        answer.append(j)

print(answer[0])
print(answer[1])