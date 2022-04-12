from collections import deque
class Solution:
    def wallsAndGates(self, rooms) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # create a couple helper variables
        m = len(rooms)
        n = len(rooms[0])
        to_visit = set()
        visited = set()
        q = deque()
        # populate sets
        for i in range(m):
            for j in range(n):
                if rooms[i][j] > 0:
                    to_visit.add((i, j))
                if rooms[i][j] == 0:
                    q.append((i, j))
        # begin BFS with q containing only gates
        dist = 0
        while q:
            # only process nodes from last round of BFS before dist update
            for _ in range(len(q)):
                curr = q.popleft()
                i, j = curr
                # branch logic to avoid processing gates
                if curr in visited:
                    rooms[i][j] = min(dist, rooms[i][j])
                for adj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    # only add node to q if it needs to be visited
                    if adj in to_visit:
                        q.append(adj)
                        to_visit.remove(adj)
                        visited.add(adj)
            # increment distance for next round of BFS
            dist += 1
