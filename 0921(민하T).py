n = int(input())
b = [[0 for _ in range(20)] for _ in range(20)]

for _ in range(n):
    a, c = map(int, input().split())
    b[a - 1][c - 1] = 1

for row in b:
    print(" ".join(map(str, row))) #공백에 문자열 row를 하나씩 넣어준다