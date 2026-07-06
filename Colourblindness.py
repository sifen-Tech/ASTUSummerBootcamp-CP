t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    a =input()
    s=s.replace('G','B')
    a=a.replace('G','B')
    if s == a:
        print("YES")
    else:
        print("NO")
    
