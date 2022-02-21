import heapq
class Solution:
    def reorderLogFiles(self, logs):
        # remove the letter-logs from array
        h = []
        heapq.heapify(h)
        i = 0
        while i < len(logs):
            if ord(logs[i][-1]) > 57:
                arr = logs[i].split(' ')
                # throw a dummy '1' onto front of filename to make sure that
                # the file name is a secondary sorting measure
                s = ' '.join(arr[1:] + ['1' + arr[0]])
                logs.pop(i)
                heapq.heappush(h, s)
            else:
                i += 1
        letter_res = []
        while h:
            s = heapq.heappop(h)
            arr = s.split(' ')
            letter_res += [' '.join([arr[-1][1:]] + arr[:-1])]
        return letter_res + logs


# looks like the solution wanted us to lean in the direction of defining
# the sort criteria. However, the solution performs well and I see some folks
# that went my direction too.