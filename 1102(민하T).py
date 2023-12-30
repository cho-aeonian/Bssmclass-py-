stack_size =5 #리스트용량
list = [None]*stack_size 
top=-1 #연산하는 부분에서 전역 변수로 바꿔줌 

def isEmpty(): #비어 있다
    if top==1:
        return True
    else:
        return False

def isFull(): #가득 차 있다
    return top==stack_size -1

def push(e):
    global top
    if not isFull():
        top=top+1
        list[top]=e
    else:
        print("stack overflow")
        exit()
    

def pop(): #비어있는지 차있는지 top으로 알 수 있음 -> stack_size만큼 가면 가득 찬 거임
    global top
    if not isEmpty():
        top=top-1
        return list[top+1]
    else:
        print("stack underflow")
        exit()
        
def peek():
    if not isEmpty():
        return list[top]
    else: pass

push(1)
push(1)
push(1)
push(1)
push(1)
push(1)