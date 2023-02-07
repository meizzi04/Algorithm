# 먼저 ord() 사용하여 문자열을 아스키코드 값으로 변경
# 마지막에 chr() 사용하여 다시 아스키코드 값을 문자열로 변경
def solution(s, skip, index):
    answer = ''
    skipList = list(ord(s) for s in skip)
    
    for word in s :
        cnt = index
        word = ord(word)
        
        while cnt != 0 :
            word += 1
            
            if word > ord('z') :
                word = word - ord('z') + ord('a') - 1
            
            if word in skipList :
                continue
            
            cnt -= 1
        answer += chr(word)
        
    # 제한사항
    if 5 > len(s) > 50 :
        print("s의 범위 초과")
    if 1 > len(skip) > 10 :
        print("skip의 범위 초과")
    if 1 > index > 20 :
        print("index의 범위 초과")
    if s == skip :
        print("s와 skip 문자열 중복")
    for i in s :
        if ord(i) < ord('Z') :
            print("s 소문자만 가능")
    for j in skip :
        if ord(j) < ord('Z') :
            print("skip 소문자만 가능")

    return answer

