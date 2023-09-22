#기본 입출력+조건문+반복문
print("입력하세요")
n = int(input())
sum = 0
for num in range(1, n + 1):
    if num % 2 == 0:
        sum += num

print(f"{sum}")