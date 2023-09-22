#피보나치
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_prev = 0
        fib_curr = 1
        for _ in range(2, n + 1):
            fib_next = fib_prev + fib_curr
            fib_prev, fib_curr = fib_curr, fib_next
        return fib_curr
    
n = int(input("n을 입력하세요:\n")) #사용자로부터 어떤 숫자를 입력 받는다.

result = fibonacci(n) #n번째의 피보나치 수열을 계산한다.
print(f"{n}번째 피보나치 수: {result}") #n번째의 피보나치 수열을 출력한다.