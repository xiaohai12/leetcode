class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []
        n, m = len(matrix), len(matrix[0])
        operation = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        flag = [[False for i in range(m)] for j in range(n)]
        i, j = 0, -1
        ret = []
        direct = 0
        cur_step = m
        pre_step = n
        step = m
        ## find the rule that step sequence is  [m,n-1,m-1,n-2,m-2.....]
        while cur_step != 0:
            i += operation[direct][0]
            j += operation[direct][1]
            ret.append(matrix[i][j])
            cur_step -= 1
            if cur_step == 0:
                cur_step = pre_step - 1
                pre_step = step
                step = cur_step
                direct = (direct + 1) % 4
        return ret
