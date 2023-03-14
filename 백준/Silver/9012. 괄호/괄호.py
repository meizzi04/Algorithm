T = int(input())

for i in range(T):
    stack = []
    PS = input()  # 괄호 문자열(Parenthesis String)

    for j in PS:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")