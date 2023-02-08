def solution(s):
    answer = 0
    n1 = 0 # 첫 글자
    n2 = 0 # 첫 글자가 아닌 다른 글자

    for i in s :
        if n1 == n2 :
            answer += 1
            tmp = i
        if tmp == i : 
            n1 += 1
        else :
            n2 += 1
    
    return answer