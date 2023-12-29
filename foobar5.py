def solution(l):
    n=0
    length=len(l)
    c=[0]*length
    for i in range(length):
        for j in range(i):
            if(l[i]%l[j]==0):
                n+=c[j]
                c[i]+=1
    return n

