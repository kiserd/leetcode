class Solution:
    def asteroidCollision(self, asteroids):
        s = []
        for astd in asteroids:
            stable = False
            while not stable:
                if not s or astd > 0:
                    s.append(astd)
                    stable = True
                else:
                    last = s[len(s) - 1]
                    if last < 0:
                        s.append(astd)
                        stable = True
                    elif last + astd == 0:
                        s.pop()
                        stable = True
                    elif last + astd > 0:
                        stable = True
                    else:
                        s.pop()
        return s
