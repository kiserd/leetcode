class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        in_deg = [0] * numCourses
        out = {}
        start = {i for i in range(numCourses)}
        for ed, st in prerequisites:
            if out.get(st, False):
                out[st].append(ed)
            else:
                out[st] = [ed]
            in_deg[ed] += 1
            if ed in start:
                start.remove(ed)
        visited = {}
        q = list(start)
        next = 0
        while next != len(q):
            curr = q[next]
            next += 1
            visited[curr] = None
            for ed in out.get(curr, []):
                if ed not in visited:
                    in_deg[ed] -= 1
                    if in_deg[ed] == 0:
                        q.append(ed)
        return len(visited) == numCourses
