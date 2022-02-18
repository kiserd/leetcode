from collections import OrderedDict
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        # little housekeeping to tally in/out degrees
        deg = {i: {'in': 0, 'out': []} for i in range(numCourses)}
        starts = {i for i in range(numCourses)}
        for ed, st in prerequisites:
            deg[st]['out'].append(ed)
            deg[ed]['in'] += 1
            if ed in starts:
                starts.remove(ed)
        # work through Kahn's algo via queue
        q = list(starts)
        next = 0
        visited = OrderedDict()
        while next != len(q):
            curr = q[next]
            next += 1
            visited[curr] = None
            for ed in deg[curr]['out']:
                if ed not in visited:
                    deg[ed]['in'] -= 1
                    if deg[ed]['in'] == 0:
                        q.append(ed)
        if len(visited) == numCourses:
            return list(visited)
        else:
            return []
