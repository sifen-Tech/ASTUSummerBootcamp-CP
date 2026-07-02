t=int(input())
for i in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    left=0
    right=n-1
    for i in range(1,n):
        if i ==p[left]:
            left+=1
        elif i==p[right]:
            right-=1
        else:
            print("NO")
            break
    else:
        print("YES")
