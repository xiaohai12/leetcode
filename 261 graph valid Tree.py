class Solution:
    ## find and union algorithms
    def validTree(self, n, edges):
        parent = [i for i in range(n)]

        def find(x):
            return x if parent[x] == x else find(parent[x])

        for e in edges:
            x, y = map(find, e)
            if x == y:
                return False
            parent[x] = y
        return len(edges) == n - 1
