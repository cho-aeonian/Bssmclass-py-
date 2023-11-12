# sort 함수
# 해당 리스트에 저장된 원소들을 오름차순으로 정렬

# reverse 함수
# 해당 리스트에 저장된 원소들의 순서를 정반대로 뒤집어줌

# append 함수
# 해당 리스트의 맨 마지막 위치에 전달받은 데이터를 추가해줌

# ex01
myscores=[100,70,88,25]
yourscores=[55,46,100,98] #리스트선언

myscores.sort() # myscores의 원소를 오름차순으로 정렬
yourscores.reverse() # yourscores의 원소의 순서 정반대로 정렬

print(myscores) # 오름차순으로 정렬된 원소 출력
print(yourscores) # 정반대 순서의 원소 출력

# del->파이썬 내부 함수/전달받은 변수 삭제
del myscores[0] # myscores의 0번째 원소 삭제
myscores.append(45) # myscores의 가장 마지막 원소 뒤에 45저장

print(myscores) #0번째인 25를 삭제하고 4번째에 45 저장