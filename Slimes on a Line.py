t=int(input())
for i in range(t):
    n=int(input())
    array=list(map(int,input().split()))
    array.sort()
    print((array[-1]-array[0]+1)//2)
        
