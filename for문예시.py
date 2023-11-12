# for문의 특징
# 튜플이나 리스트를 사용할 때 while보다 더욱 간결하게 코드 작성 가능

tempList = ['유비','관우','장비','제갈량']
for i in tempList:
    print(i)

i = [(1,2),(3,4),(5,6)] # 소괄호()-> 튜플
for (first,last) in i:
    print(first+last) #first에 1 들어감, last에 2 들어감

sum = 0
for a in range(1,5): #1부터 4까지 / range 함수는 시작 숫자부터 (마지막숫자-1)까지 숫자의 나열
    sum = sum+a
print(sum)

for a in range(2,10): #2부터 9까지 출력 (마지막 10 제외)
    for b in range(1,10): #1부터 9까지 출력 (마지막 10 제외)
        print(a,"X",b,"=",a*b)
        if b==9: # O x 9 의 형식이면 줄바꿈
            print("\n")