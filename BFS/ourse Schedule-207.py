
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        neighbor = {}
        for pair in prerequisites:
            if pair[1] not in neighbor.keys():
                neighbor[pair[1]] = [pair[0]]
            else:
                neighbor[pair[1]].append(pair[0])
        visiting = []
        visited = []
        for i in range(numCourses):
            if not self.dfs(neighbor ,i ,visiting ,visited):
                return False
        return True


    def dfs(self ,neighbor ,node ,visiting ,visited):
        if node not in neighbor.keys():
            visited.append(node)
            return True

        if node in visited:
            return True

        visiting.append(node)
        for neigh in neighbor[node]:
            if neigh in visiting or not self.dfs(neighbor ,neigh ,visiting ,visited):
                return False

        visited.append(node)
        visiting.pop()
        return True








