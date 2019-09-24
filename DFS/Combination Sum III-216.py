class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        if k == 0:
            return None
        if n <= 0:
            return None
        bools = [True for i in range(9)]
        results = []
        self.dfs([], k, n, results, bools, -1)
        return results

    def dfs(self, tmp, k, target, results, bools, ind):
        if k == 0:
            Sum = sum(tmp)
            if Sum == target:
                if tmp not in results:
                    results.append(tmp.copy())
            elif Sum > target:
                return

        for i in range(ind + 1, 9):
            if bools[i] == False:
                continue
            else:
                tmp.append(i + 1)
                bools[i] = False
                self.dfs(tmp, k - 1, target, results, bools, i)
                tmp.pop()
                bools[i] = True

