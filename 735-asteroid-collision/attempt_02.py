from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for a in asteroids:
            curr = a
            if not s:
                s.append(a)
            else:
                while s and curr is not None:
                    if curr < 0 and s and s[-1] > 0:
                        if abs(s[-1]) == abs(a):
                            s.pop()
                            curr = None
                        elif abs(s[-1]) < abs(a):
                            s.pop()
                        else:
                            curr = s.pop()
                    else:
                        s.append(curr)
                        curr = None
                if curr is not None:
                    s.append(curr)
        return s
