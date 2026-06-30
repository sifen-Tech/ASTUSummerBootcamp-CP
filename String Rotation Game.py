t = int(input())

for i in range(t):
    n = int(input())
    s = input()

    ans = 0

    for i in range(n):
        temp= s[i:] + s[:i]
        blocks = 1
        for j in range(1, n):
            if temp[j] != temp[j - 1]:
                blocks += 1

        ans = max(ans, blocks)

    print(ans)
