class Solution:
    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        # attempt to return early if src == dst
        if source == destination:
            return True
        # get adjacencies in more digestable form
        adjs = {i: [] for i in range(n)}
        for i, j in edges:
            adjs[i].append(j)
            adjs[j].append(i)
        # work through DFS using stack
        s = [source]
        visited = {source}
        while s:
            curr = s.pop()
            for node in adjs[curr]:
                if node not in visited:
                    if node == destination:
                        return True
                    visited.add(node)
                    s.append(node)
        # DFS failed to discover destination, indicate to calling function
        return False
