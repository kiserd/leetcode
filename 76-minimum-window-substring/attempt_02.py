class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # init t char counts
        cts = {}
        for ch in t:
            cts[ch] = cts.get(ch, 0) + 1
        # use two-ptr approach with sliding window
        rem_chars = len(t)
        bg = 0
        ed = -1
        res_len = (10**5) + 1
        res = ''
        while ed < len(s):
            if rem_chars > 0:
                ed += 1
                if ed < len(s) and cts.get(s[ed], None) is not None:
                    if cts[s[ed]] > 0:
                        rem_chars -= 1
                    cts[s[ed]] -= 1
            else:
                if cts.get(s[bg], None) is not None:
                    if cts[s[bg]] >= 0:
                        rem_chars += 1
                    cts[s[bg]] += 1
                bg += 1
            if rem_chars == 0:
                if len(s[bg:ed+1]) < res_len:
                    res_len = len(s[bg:ed+1])
                    res = s[bg:ed+1]
        if res_len > (10**5):
            return ''
        return res
