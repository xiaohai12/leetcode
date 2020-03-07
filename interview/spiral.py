

def spiral(n):
    up = (0,1)
    down = (0,-1)
    left = (-1,0)
    right  = (1,0)
    opts  = [up,right,down,left]
    pre = 2
    now =2
    opt_ind = 0
    pt = [0,0]
    for i in range(n):
        pt[0] +=opts[opt_ind][0]
        pt[1] +=opts[opt_ind][1]
        now -=1
        if now == pre/2:
            opt_ind = (opt_ind+1)%4
        if now ==0:
            now = pre+2
            pre = now
            opt_ind = (opt_ind + 1) % 4
    return pt

print(spiral(10))


