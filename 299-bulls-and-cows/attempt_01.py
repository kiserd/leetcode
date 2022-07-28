class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s_counts = [0] * 10
        s_map = {str(i): set() for i in range(10)}
        g_counts = [0] * 10
        g_map = {str(i): set() for i in range(10)}
        for idx in range(len(guess)):
            s_counts[int(secret[idx])] += 1
            s_map.get(secret[idx]).add(idx)
            g_counts[int(guess[idx])] += 1
            g_map.get(guess[idx]).add(idx)
        # iterate through counts
        cows = 0
        bulls = 0
        for i in range(len(s_counts)):
            if s_counts[i] and g_counts[i]:
                curr_bulls = len(s_map[str(i)].intersection(g_map[str(i)]))
                cows += (min(s_counts[i], g_counts[i]) - curr_bulls)
                bulls += curr_bulls
        return str(bulls) + 'A' + str(cows) + 'B'
