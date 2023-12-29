def solution(entrances, exits, path):
    n = len(path)
    enter = len(entrances)
    egress = len(exits)
    ins = [0] * n
    list1=[]
    maxi=0
    for i in range(n):
        for j in exits:
            maxi+=path[i][j]
    while True:
        for i in entrances:
            for j in range(n):
                ins[j] += path[i][j]
        for i in range(n):
            for j in range(n):
                if j not in entrances:
                    if ins[i] >= path[i][j]:
                        ins[j] += path[i][j]
                        ins[i] -= path[i][j]
                    else:
                        ins[j] += ins[i]
                        ins[i] = 0
        s=0
        for j in exits:
            s+=ins[j]
        list1+=[s]
        if(maxi<=max(list1)):
            break
        transfer_possible = any(ins[i] > 0 for i in entrances)
        if not transfer_possible:
            break  
    return max(list1)




