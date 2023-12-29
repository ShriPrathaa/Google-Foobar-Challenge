def solution(s):
    index=1
    c=s[0]
    l=len(s)
    while((len(c)+index)<=l):
        a=s[index:len(c)+index]
        if(c!=a):
            c+=s[index]
            index+=1            
        elif (c==a):
            if(l%len(c)==0):
                lina=(l//len(c))
                if(s==c*lina):
                    return lina
                else:
                    c+=s[index]
                    index+=1                      
            else:
                c+=s[index]
                index+=1
    return 1

