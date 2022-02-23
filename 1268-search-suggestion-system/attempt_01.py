class Solution:
    def suggestedProducts(self, products, searchWord: str):
        # sort products to facilitate binary search
        products.sort()
        # use binary search to find beginning of prefix
        i = 0
        key = ''
        res = []
        while i < len(searchWord):
            if not products:
                res.append([])
            else:
                key += searchWord[i]
                products = self.getBeg(products, key)
                products = self.getEnd(products, key)
                res.append(products[0:min(len(products), 3)])
            i += 1
        return res

    def getBeg(self, products, key):
        lo = 0
        hi = len(products) - 1
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if products[mi][0:len(key)] > key:
                hi = mi - 1
            elif products[mi][0:len(key)] < key:
                lo = mi + 1
            else:
                if mi == 0 or products[mi - 1][0:len(key)] < products[mi][0:len(key)]:
                    lo = hi = mi
                else:
                    hi = mi - 1
        if products[hi][0:len(key)] != key:
            return []
        return products[hi:]

    def getEnd(self, products, key):
        lo = 0
        hi = len(products) - 1
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if products[mi][0:len(key)] > key:
                hi = mi - 1
            elif products[mi][0:len(key)] < key:
                lo = mi + 1
            else:
                if mi == len(products) - 1 or products[mi + 1][0:len(key)] > products[mi][0:len(key)]:
                    lo = hi = mi
                else:
                    lo = mi + 1
        return products[0:lo + 1]
