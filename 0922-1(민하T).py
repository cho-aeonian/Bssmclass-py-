#계단 오르기 문제

def jump(n):
    if(n<1):
        return 0
    elif(n==1):
        return 1
    else:
        return jump(n-1)+jump(n-2)+jump(n-3) #
    
n = int(input())
answer=jump(n+1)
print(answer)