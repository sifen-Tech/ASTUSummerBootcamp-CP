t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    temp = []

    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            temp.append(i)

    if not temp:
        print("Yes")
        continue

    possible = True

    for i in range(1, len(temp)):
        if temp[i] != temp[i - 1] + 1:
            possible = False
            break

    if possible:
        print("Yes")
    else:
        print("No")
