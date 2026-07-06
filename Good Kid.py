# 2 2 1 2
# 3*2*1*2=12
# 2*3*1*2=12
# 2*2*2*2=16
# 2*2*1*3=12
# t=int(input())
# for i in range(t):
#     n=int(input())
#     array=list(map(int,input().split()))
#     array.sort()
#     array[0]+=1
#     pro=1
#     for i in array: 
#         pro*=i
#     print(pro
# 
import math
t=int(input())
for i in range(t):
    n=int(input())
    array=list(map(int,input().split()))
    array.sort()
    array[0]+=1
    for i in range(n):
        result = math.prod(array)
    print (result)

    
