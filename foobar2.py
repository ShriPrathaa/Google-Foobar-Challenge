def solution(l, t):
    sumi=[]
    le=len(l)
    s=0
    sumi.append(s)
    for i in l:
        s+=i
        sumi.append(s)
    i=0
    if(sumi[-1]<t):
            return [-1,-1]
    while(i<le+1):
        for j in range(i,le+1):
            if((sumi[j]-sumi[i])==t):
                return i+1,j
            if((sumi[j]-sumi[i])>t):
                i+=1
                break        
    return [-1,-1]

