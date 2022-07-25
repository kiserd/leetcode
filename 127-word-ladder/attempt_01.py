from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        # prepare some helper vars / structs
        wordList.append(beginWord)
        n = len(wordList)
        m = len(beginWord)
        adjs = {}
        # define function to get transformed wildcard strings
        def get_trans(s: str):
            res = []
            for idx in range(len(s)):
                res.append(s[:idx] + '_' + s[idx+1:])
            return res
        # prepare adjacency mapping
        for i in range(n):
            word = wordList[i]
            for trans in get_trans(word):
                if trans in adjs:
                    adjs[trans].add(word)
                else:
                    adjs[trans] = {word}
        # use BFS to determine shortest path
        to_visit = set(wordList)
        q = deque()
        q.append(beginWord)
        count = 1
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr in to_visit:
                    to_visit.remove(curr)
                    # build and process set of adjacencies
                    neighbors = set()
                    for trans in get_trans(curr):
                        for adj in adjs[trans]:
                            neighbors.add(adj)
                    for adj in neighbors:
                        # check if endWord is found
                        if adj == endWord:
                            return count + 1
                        if adj in to_visit:
                            q.append(adj)
            # increment count for next "level" of BFS
            count += 1
        # endWord not found, indicate to calling function
        return 0
