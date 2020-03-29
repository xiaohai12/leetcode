class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        operation = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ret = [[0 for i in range(n)] for j in range(n)]
        curStep = n
        preStep = n
        step = n
        i = 0
        j = -1
        direct = 0
        x = 0
        while curStep != 0:
            x += 1
            i += operation[direct][0]
            j += operation[direct][1]
            ret[i][j] = x
            curStep -= 1
            if curStep == 0:
                direct = (direct + 1) % 4
                curStep = preStep - 1
                preStep = step
                step = curStep
        return ret

