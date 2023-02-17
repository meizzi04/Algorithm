import sys

input = sys.stdin.readline

N = int(input())

string = []

for i in range(N) :
    string.append(input().strip())

string_set = set(string)
string = list(string_set)

string.sort()
string.sort(key=len) # 리스트 요소를 길이 순으로 정렬

for i in string :
    print(i)