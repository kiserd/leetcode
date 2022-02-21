import heapq
class Solution:
    def kClosest(self, points, k: int):
        dists = []
        for x, y in points:
            dist = (x**2 + y**2) ** (0.5)
            dists.append((dist, x, y))
        smallest = heapq.nsmallest(k, dists)
        return [[x, y] for _, x, y in smallest]
        