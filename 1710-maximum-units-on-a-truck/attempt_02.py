class Solution:
    def maximumUnits(self, boxTypes, truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        units = 0
        i = 0
        while i < len(boxTypes) and truckSize:
            num_boxes = min(boxTypes[i][0], truckSize)
            units += (num_boxes * boxTypes[i][1])
            truckSize -= num_boxes
            i += 1
        return units
