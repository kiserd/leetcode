class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        # handle ..kinda edge case (hacky)
        n = len(letters)
        first = ord(letters[0])
        last = ord(letters[n - 1])
        if target >= letters[n - 1] or target < letters[0]:
            return letters[0]
        lo = 0
        hi = len(letters) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if letters[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return letters[hi]
