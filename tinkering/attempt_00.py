def main():
    one = []
    two = []
    k = 7

    one.sort(key=lambda x: x[1])
    two.sort(key=lambda x: x[1])

    l = 0
    r = len(two) - 1
    curr = -1
    res = []
    while l < len(one) and r > -1:
        if one[l] + two[r] <= k:
            if one[l] + two[r] == curr:
                res.append([one[0], two[0]])
            if one[l] + two[r] > curr:
                curr = one[l] + two[r]
                res = [[one[0], two[0]]]
            l += 1
        else:
            r -= 1
    return res
