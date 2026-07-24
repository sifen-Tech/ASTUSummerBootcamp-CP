t = int(input())

for i in range(t):
    n = int(input())

    first = input().split()
    second = input().split()
    third = input().split()

    words = {}
                            
    for i in first:   
        if i in words:
            words[i] += 1
        else:
            words[i] = 1

    for i in second:    #word=for
        if i in words:  
            words[i] += 1
        else:
            words[i] = 1

    for i in third:        #word=ces
        if i in words:
            words[i] += 1
        else:
            words[i] = 1

    score1 = 0
    score2 = 0
    score3 = 0



    for i in first:   
        if words[i] == 1:   
            score1 += 3
        elif words[i] == 2:
            score1 += 1

    for i in second:
        if words[i] == 1:   
            score2 += 3 
        elif words[i] == 2:
            score2 += 1

    for i in third:       
        if words[i] == 1:    
            score3 += 3
        elif words[i] == 2:
            score3 += 1

    print(score1, score2, score3)
