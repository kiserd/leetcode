class Solution:
    def findItinerary(self, tickets):
        # handle edge case
        if len(tickets) == 1: return tickets[0]
        # build adjacency mapping
        adjs = {}
        for st, ed in tickets:
            if not adjs.get(st, False):
                adjs[st] = {ed: 1}
            elif not adjs.get(st, False).get(ed, False):
                adjs[st][ed] = 1
            else:
                adjs[st][ed] += 1
        # define recursive function
        def dfs(path):
            # handle successful base case
            if len(path) == len(tickets) + 1:
                return path
            # handle unsuccessful base case(s)
            st = path[len(path) - 1]
            if not adjs.get(st, False):
                return False
            # handle recursive exploration
            eds = sorted(list(adjs[st]))
            eds.sort()
            for ed in eds:
                if adjs[st][ed] > 0:
                    adjs[st][ed] -= 1
                    path.append(ed)
                    res = dfs(path)
                    if res:
                        return res
                    path.pop()
                    adjs[st][ed] += 1
        # kick off recursive function
        return dfs(['JFK'])
        
                

        