# 수행평가문제(for문)
# 리스트 선언해서 입력받고 for문으로 리스트에 있는 값 다 더하는 코드
a = input().split()
sum = int(0)

for i in range (5):
    a[i] = int(a[i])

for i in range(5):
    sum += a[i]

print(sum)