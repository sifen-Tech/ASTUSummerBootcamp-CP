for _ in range(int(input())):
    n=int(input())
    s=input()
    ans=0
    visited=set()
   
    for i in range(n):
        if  s[i] in visited:
            ans+=1
        else:
            ans+=2
            visited.add(s[i])
    print(ans)
