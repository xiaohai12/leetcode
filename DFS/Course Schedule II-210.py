class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        if not prerequisites:
            return [i for i in range(numCourses)]

        neighbors = {}
        for pair in prerequisites:
            if pair[1] not in neighbors.keys():
                neighbors[pair[1]] = [pair[0]]
            else:
                neighbors[pair[1]].append(pair[0])

        visiting = []
        visited = []
        order = collections.deque()
        for i in range(numCourses):
            if not self.dfs(i, neighbors, visiting, visited, order):
                return []
        return order

    def dfs(self, node, neighbors, visiting, visited, order):
        visiting.append(node)
        if node in visited:
            return True
        if node in neighbors.keys():
            for neigh in neighbors[node]:
                if neigh in visiting:
                    return False
                elif neigh in visited:
                    continue
                if not self.dfs(neigh, neighbors, visiting, visited, order):
                    return False
        visiting.pop()
        visited.append(node)
        order.appendleft(node)
        return True




