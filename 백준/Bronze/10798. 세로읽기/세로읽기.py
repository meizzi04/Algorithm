text = []

for _ in range(5):
    text.append(input())
for i in range(15):
    for j in range(5):
        if i < len(text[j]):
            print(text[j][i], end="")