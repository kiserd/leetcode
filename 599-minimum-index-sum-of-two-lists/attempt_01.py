class Solution:
    def findRestaurant(self, list1, list2):
        # init a couple helper vars and data structs
        min_ind_sum = 2001
        l1_map = {}
        l2_map = {}
        res = []
        # process first list
        for idx, name in enumerate(list1):
            l1_map[name] = idx
        # process second list in search of min index sum(s)
        for idx, name in enumerate(list2):
            if name in l1_map:
                if idx + l1_map[name] < min_ind_sum:
                    min_ind_sum = idx + l1_map[name]
                    res = [name]
                elif idx + l1_map[name] == min_ind_sum:
                    res.append(name)
        return res
