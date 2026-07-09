for i in range(int(input())):
    n,k=map(int,input().split())
    arry=list(map(int,input().split()))
    a=set(arry)
    for i in a:
        if i-k in a :
            print("YES")
            break
    else:
        print("NO")
