# [n, m] =[3,10]
# store = [2,5,3]
# val = [2,1,3]
# Min = min(store)
# left = m
# if left < min(val):
#     print(Min)
# else:
#     while Min:
#         Min += 1
#         for i in range(n):
#             if store[i] < Min:
#                 left -= (Min - store[i]) * val[i]
#         if left < 0:
#             break
#
#     print(Min - 1)

def helper(row, col, end, area, size):
    if [row, col] == end and area[row][col]==1:
        return True

    if row<0 or row==size[0] or col<0 or col==size[1]:
        return
    area[row][col] -= 1
    for i in range(4):
        if i == 0:
            Area = area.copy()
            # left
            if col==0:
                continue
            elif area[row][col-1] <= 0:
                continue
            else:
                return helper(row,col-1, end, Area, size)
        elif i == 1:
            #right
            Area = area.copy()
            if col==size[1]-1:
                continue
            elif area[row][col+1] <= 0:
                continue
            else:
                return helper(row, col + 1, end, Area, size)
        elif i == 2:
            #down
            Area = area.copy()
            if row == 0:
                continue
            elif area[row- 1][col] <= 0:
                continue
            else:
                return helper(row-1, col, end, Area, size)
        elif i == 3:
            #up
            Area = area.copy()
            if row == size[0]-1:
                continue
            elif area[row+1][col] <= 0:
                continue
            else:
                return helper(row+1, col, end, Area, size)
    return False

import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    area = []
    for i in range(n):
        size = list(map(int, sys.stdin.readline().split()))
        for j in range(size[0]):
            real = []
            tmp = sys.stdin.readline()
            for i in range(size[1]):
                if tmp[i]=='.':
                    real.append(2)
                else:
                    real.append(1)
            area.append(real)
        start = list(map(int, sys.stdin.readline().split()))
        end =  list(map(int, sys.stdin.readline().split()))
        if helper(start[0]-1,start[1]-1,[end[0]-1,end[1]-1],area,size):
            print('YES')
        else:
            print('NO')










