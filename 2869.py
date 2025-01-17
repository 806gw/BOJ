import math

A, B, V = map(int, input().split())
D = (V - B) / (A - B) 

print(math.ceil(D)) # D 값에 소수가 들어갈 수 있기 때문에 실수를 올림