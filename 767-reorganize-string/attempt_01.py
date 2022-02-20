import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        # handle edge case
        if len(s) == 1: return s
        counts = {}
        for char in s:
            count = counts.get(char, False)
            if count:
                counts[char] += 1
            else:
                counts[char] = 1
        # heapify our list
        h = [(-counts[i], i) for i in counts]
        heapq.heapify(h)
        # determine if no solution exists (cut program short)
        if len(s) % 2 == 0:
            if h[0][0] < -(len(s) // 2):
                return ''
        else:
            if h[0][0] < -(len(s) // 2) - 1:
                return ''
        res = ''
        while h[0][0] < 0:
            fst_cnt, fst_chr = heapq.heappop(h)
            res += fst_chr
            fst_cnt += 1
            if h[0][0] < 0:
               scd_cnt, scd_chr = heapq.heappop(h)
               res += scd_chr
               scd_cnt += 1
               heapq.heappush(h, (scd_cnt, scd_chr))
            heapq.heappush(h, (fst_cnt, fst_chr))
        return res

