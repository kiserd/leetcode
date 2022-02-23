class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        # format data for easy sorting by timestamp
        tups = [(timestamp[i], username[i], website[i]) for i in range(len(timestamp))]
        tups.sort(key=lambda x: x[0])
        # get website lists by user
        lists = {}
        for _, user, site in tups:
            if user in lists:
                lists[user].append(site)
            else:
                lists[user] = [site]
        # get counts for patterns
        max_count = 0
        patterns = {}
        for user in lists:
            arr = lists[user]
            staging = set()
            if len(arr) > 2:
                for i in range(len(arr) - 2):
                    for j in range(i + 1, len(arr) - 1):
                        for k in range(j + 1, len(arr)):
                            tup = tuple([arr[i]] + [arr[j]] + [arr[k]])
                            staging.add(tup)
            for tup in staging:
                count = patterns.get(tup, 0)
                patterns[tup] = count + 1
                max_count = max(max_count, count + 1)
        max_list = [[s1, s2, s3] for (s1, s2, s3), v in patterns.items() if v == max_count]
        return min(max_list)        