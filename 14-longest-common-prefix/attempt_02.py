class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # handle edge cases and get min length
        min_len = 201
        for s in strs:
            if not s:
                return ''
            min_len = min(min_len, len(s))
        if len(strs) == 1:
            return strs[0]
        # process through min_len and while prefix condition satisfied
        res = 0
        active_prefix = True
        while active_prefix and res < min_len:
            # use arbitrary string to match substring to
            curr = strs[0][res]
            for s in strs:
                if res == len(s) or s[res] != curr:
                    active_prefix = False
            if active_prefix:
                res += 1
        return strs[0][:res]
