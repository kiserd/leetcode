from typing import List


class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        # build out to_visit set
        to_visit = set()
        for i in range(len(image)):
            for j in range(len(image[0])):
                to_visit.add((i, j))
        # process using DFS via stack
        s = [(sr, sc)]
        to_visit.remove((sr, sc))
        og_color = image[sr][sc]
        while s:
            i, j = s.pop()
            image[i][j] = color
            for adj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if adj in to_visit and image[adj[0]][adj[1]] == og_color:
                    s.append(adj)
                    to_visit.remove(adj)
        return image
