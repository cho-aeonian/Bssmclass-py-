# 함수
# 하나의 특정한 목적의 작업을 수행하기 위해 
# 독립적으로 구성된 프로그램 코드의 집합

# 함수의 구조
# def 함수명(입력 인수):
# 수행문장 1
# 수행문장 2
# 수행문장 3

# sum
# 두 매개변수의 합인 a+b를 반환하는 함수
def sum(a,b):
    return a+b
a=1
b=2
c=sum(a,b) #sum은 a,b 두개의 매개변수를 가짐
print(c)

# 매개변수를 가지지 않는 형태
def hi():
    return 'hi'
x=hi()
print(x)

# multi()
# return(반환값)이 없는 형태
def multi(a,b):
    print("%d X %d의 곱은 %d입니다." % (a,b,a*b))
multi(2,4) #multi의 값에 2,4 넣음

# 다른 수의 매개변수를 전달받는 함수
def sumMany(*args): #매개변수 *args로 선언
    sum=0
    for i in args:
        sum = sum+i
    return sum

temp = sumMany(1,2,3,4,5,6,7,8,9,10)
print(temp)

# I/O함수

temp=input("문자열을 입력하세요 :")
# 문자열을 입력하세요 : 안녕하세요? 반갑습니다.

print(temp)
# 안녕하세요? 반갑습니다.

print("Music""is""my""life")
print("Music"+"is"+"my"+"life")
print("Music","is","my","life")
print("Music is my life")