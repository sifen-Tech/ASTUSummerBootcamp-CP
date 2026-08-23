from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    s=[int(x) for x in input().split()]

    mydict=defaultdict(list)
    ans=[]
    for i in range(n):
        mydict[s[i]].append(i+1)
    possible=True
    for i in mydict.keys():
        if len(mydict[i]) <2:
            possible =False
            break
        ans.append(mydict[i][-1])
        ans.extend(mydict[i][:-1])
        
       
    print(*ans) if possible else print(-1)
