meet=0

while meet<4: # 4보다 작을 동안 방문
    meet = meet+1 # 방문횟수 증가
    print("유비가 %d번 방문했습니다." % meet)

    if meet == 3: # 세 번 만났기 때문에 방문 종료(4보다 작을 만큼임)
        print("제갈량이 유비 곁으로 갑니다.")
        break # while 문을 빠져나감