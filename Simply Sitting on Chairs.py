t=int(input())
for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    forward=0
    backward=0
    for i in range(len(p)):
        if p[i]>i+1:
            forward+=1
        else:
            backward+=1
    print(len(p)-forward)
