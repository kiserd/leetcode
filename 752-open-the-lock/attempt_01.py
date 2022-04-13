from collections import deque
class Solution:
    def openLock(self, deadends, target: str) -> int:
        # attempt to return early on edge case
        if '0000' in deadends:
            return -1
        # define function to produce adjacent
        def get_adj(s):
            """ returns adjacent combinations """
            res = set()
            helper = '901234567890'
            for i in range(len(s)):
                # get adjacent chars
                num = int(s[i])
                adjs = helper[num] + helper[num + 2]
                for adj in adjs:
                    res.add(s[:i] + adj + s[i+1:])
            return res
        # initialize queue and begin looping
        # did not think to hashify deadends on first attempts
        deads = set(deadends)
        q = deque(['0000'])
        turns = 0
        visited = set()
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == target:
                    return turns
                for adj in get_adj(curr):
                    if adj not in deads and adj not in visited:
                        visited.add(adj)
                        q.append(adj)
            # increment turns after each "batch" of BFS
            turns += 1
        # search failed, indicate to calling function / user
        return -1
