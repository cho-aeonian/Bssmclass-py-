# 알고리즘
# 0값이 들어간 바둑판 만들기
# 좌표값 입력 받아서 1 넣기
# 사각형 모양 출력하기

# 아래 코드는 for문이 너무 많아서 효율성이 떨어진다
# list comprethension이라는 문법을 쓸 수 있다
d=[]
for i in range(20):
    d.append([])
for j in range(20):
    d[i].append(0)

n = int(input())
for i in range(n):
    x,y=input().split()
    d[int(x)][int(y)] = 1

for i in range(1,20):
    for j in range(1,20):
        print(d[i][j], end=' ')
    print()