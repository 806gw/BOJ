C = int(input())

for i in range(0, C):
    N = list(map(int, input().split()))
    avg = sum(N[1:]) / N[0] # 평균값 구하기
    cnt = 0
    for j in N[1:]: # 평균 점수를 넘는 학생 구하기
        if j > avg:
            cnt += 1 # 평균 점수를 넘는 학생 수
    x = cnt / N[0] * 100 # 평균보다 높은 학생 수 / 전체 학생 수 * 100 (백분율을 구하기 위한 식)
    print(f"{x:.3f}%") # 소숫점 자릿수 지정  f"{변수:.숫자f}"

