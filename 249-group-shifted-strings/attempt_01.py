class Solution:
    def groupStrings(self, strings):
        # group strings according to offset from first char
        helper = {}
        for phrase in strings:
            base = phrase[0]
            base_shift = []
            for char in phrase:
                # handle issues with negative offset
                diff = 0
                if ord(char) < ord(base):
                    diff = (26 - ord(base)) + ord(char)
                else:
                    diff = ord(char) - ord(base)
                base_shift.append(diff)
            # add shift tuple to helper mapping
            base_shift = tuple(base_shift)
            if base_shift in helper:
                helper[base_shift].append(phrase)
            else:
                helper[base_shift] = [phrase]
        # get groupings to return to user / calling function
        res = []
        for key in helper:
            res.append(helper[key])
        return res
