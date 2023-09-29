# 내가 푼 코드
num = int(input())
list = input().split()

a = int(num)
arr = []

for i in range(24):
    arr.append(0)

for i in range(a):
    arr[int(list[i])]+=1

for i in range(1, 24) :
    print(arr[i], end=' ')

# 선생님께서 알려 주신 코드
# map 함수 사용함
# 자료형으로 받은 숫자를 변수형으로 바꿔 주는 코드?
n = int(input())
num = list(map(int, input().split())) #자료형을 변수형으로 바꿔서 넣어 주세요
result = list(0 for _ in range(24))

for i in range(n):
    result[num[i]]+=1

for i in range(1, 24):
    print(result[i], end = ' ')