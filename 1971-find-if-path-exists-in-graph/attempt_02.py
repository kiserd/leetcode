# assignment spec explicitly requests for solution using dfs
class Solution:
    def validPath(self, n: int, edges, start: int, end: int) -> bool:
        # handle edge case of start == end
        if start == end:
            return True
        # initialize a couple variables to help with processing
        visited = []
        adj = [[] for i in range(n)]
        # populate adjacency list
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        # define recursive function
        def dfs(start, end, adj):
            # handle base cases
            if start in visited:
                return False
            if start == end or end in adj[start]:
                return True
            # add current node to visited
            visited.append(start)
            end_found = False
            for edge in adj[start]:
                if edge not in visited:
                    # only update end_found if a True base case is hit
                    if dfs(edge, end, adj):
                        end_found = True
            return end_found
        # process using recursive dfs
        return dfs(start, end, adj)
