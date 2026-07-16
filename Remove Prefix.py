for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=0    
    visited=set()
    for i in range(n-1,-1,-1):
        if arr[i] in visited:
            ans=i+1
            break
        visited.add(arr[i])
    print(ans)
    

       
