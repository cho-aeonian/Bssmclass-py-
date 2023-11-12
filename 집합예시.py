# 집합(set)
# 중복되는 원소가 없이 순서에 상관없는데이터들의 묶음
# 데이터들의 중복을 허용하지 않음
# 중괄호({})로 감싸서 나타냄

myscores = [100,70,88,25]

s1 = set(myscores)
print(s1) # {}안에 원소 담겨서 출력

s2 = {1,2,3}
s3 = {1,3,3}
print(s2,s3,s2-s3) # s2출력, s3(중복원소제거)출력, s2-s3(중복원소합쳐서빼기)