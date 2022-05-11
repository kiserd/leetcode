class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbrevs = {}
        for word in dictionary:
            abbrev = self.abbreviate(word)
            if abbrev in self.abbrevs:
                self.abbrevs[abbrev].add(word)
            else:
                self.abbrevs[abbrev] = {word}

    def isUnique(self, word: str) -> bool:
        abbrev = self.abbreviate(word)
        if abbrev in self.abbrevs:
            return len(self.abbrevs[abbrev]) < 2 and word in self.abbrevs[abbrev]
        return True

    def abbreviate(self, word: str) -> str:
        if len(word) < 3:
            return word
        else:
            return word[0] + str(len(word[1:-1])) + word[-1]

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
