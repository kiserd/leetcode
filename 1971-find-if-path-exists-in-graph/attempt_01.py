# assignment spec explicitly requests for solution using dfs
# utilize stack
class Solution:
    def validPath(self, n: int, edges, start: int, end: int) -> bool:
        # handle edge case of start == end
        if start == end:
            return True
        # initialize a couple variables to help with processing
        stack = [start]
        visited = []
        adj = [[] for i in range(n)]
        # populate adjacency list
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        # process using dfs
        while len(stack) != 0:
            v = stack.pop()
            # handle case of end reached
            if v == end or end in adj[v]:
                return True
            if v not in visited:
                visited.append(v)
                for vertex in adj[v]:
                    if vertex not in visited:
                        stack.append(vertex)
        # all paths processed and failed, return False
        return False
