string = input().upper() # 모든 문자열을 대문자로 변환
string_list = list(set(string))
cnt = []

for i in string_list :
    cnt.append(string.count(i))

if cnt.count(max(cnt)) > 1 :
    print('?')
else :
    print(string_list[cnt.index(max(cnt))])