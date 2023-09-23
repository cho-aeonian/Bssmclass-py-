import random
number = random.randint(1,100)
print(number)
 
while True: 
    try:
        num = int(input('1-100중의 숫자를 입력하세요 :'))
        if num == number:
            print('정답입니다')
            break
        elif num > number:
            print('더 작은 수 입니다')
        else:
            print('더 큰 수 입니다.')
    except:
        print('1-100중의 숫자를 입력해주세요')