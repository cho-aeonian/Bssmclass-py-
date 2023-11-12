# 문자열이 랜덤으로 주어지는 타자를 입력해서 정확도와 속도를 알려주는 게임 만들기
# 1. word_list 생성 ( word_list의 문장들은 랜덤으로 shuffle된다.)
# 2. word_list 속의 문장들이 돌아가면서 제시됨.
# 3. 사용자가 문장을 입력하면 해당 문장의 타자 속도, 정확도, 오타율을 출력함
# 4. 만약 사용자가 중간에 exit라고 입력하면 프로그램은 종료된다

import time
import random

WORD_LIST=[
    "아무 문장이나 적으세요",
    "코딩하는 하루 되세요",
    "여러분 화이팅",
    "오늘 급식 뭐죠?"
]
random.shuffle(WORD_LIST)

for i in WORD_LIST:
    start_time=time.time() # time->라이브러리 안에 있는 내장 함수
    user_input=str(input(i+'\n')).strip()
    end_time=time.time()-start_time

    correct=0
    for index, c in enumerate(user_input):
        if index >= len(i):
            break
        if c==i[index]:
            correct+=1
    
    total_len=len(i)
    c=correct/total_len*100
    e=(total_len-correct)/total_len*100
    speed=correct/end_time*60

    print("속도 : {:0.2f} 정확도 : {:0.2f} 오타율 {:0.2f}".format(speed,c,e))