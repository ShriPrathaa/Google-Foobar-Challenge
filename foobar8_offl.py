import math
def solution(dimensions, your_position, guard_position, distance):
    x=distance//dimensions[0]
    y=distance//dimensions[1]
    pts=[ref(your_position,x,y,dimensions),ref(guard_position,x,y,dimensions)]
    final = set()
    dist = {}
    for i in range(2):
        for j in pts[i][0]:
            for k in pts[i][1]:
                beam = math.atan2((your_position[1]-k), (your_position[0]-j))
                l = math.sqrt((your_position[0]-j)**2 + (your_position[1]-k)**2)
                if [j, k] != your_position and distance >= l:
                    if((beam in dist and dist[beam] > l) or beam not in dist):
                        if i == 0:
                            dist[beam] = l
                        else:
                            dist[beam] = l
                            final.add(beam)
    return len(final)
def ref(pos,x,y,dim):
    x_coords=[]
    for i in range(-x-1,x+2):
        res=mirror(pos[0],dim[0],x,i)
        x_coords.append(res)
    y_coords=[]
    mir_y=[]
    for i in range(-y-1,y+2):
        r=mirror(pos[1],dim[1],y,i)
        y_coords.append(r)
    return [x_coords,y_coords]
def mirror(pos,dim,x,i):
    mir_x=[2*pos,2*(dim-pos)]
    res=pos
    if(i < 0):
        for j in range(i, 0):
            res -= mir_x[(j+1) % 2]
    else:
        for j in range(i, 0, -1):
            res += mir_x[j % 2]
    return res

