import heapq
class Solution:
    def maximumUnits(self, boxTypes, truckSize: int) -> int:
        h = [(-j, i) for i, j in boxTypes]
        heapq.heapify(h)
        units = 0
        while h and truckSize:
            units_per, num_boxes = heapq.heappop(h)
            num_boxes = min(num_boxes, truckSize)
            units += -(num_boxes * units_per)
            truckSize -= num_boxes
        return units
