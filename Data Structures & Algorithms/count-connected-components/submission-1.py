class Solution:

    def dfs(self, node, graph, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, graph, visited)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
        visited = set()
        count = 0
        for node in graph:
            if node not in visited:
                self.dfs(node, graph, visited)
                count += 1
        return count

