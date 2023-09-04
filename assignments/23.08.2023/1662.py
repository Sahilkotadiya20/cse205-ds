class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        x = ""
        y = ""

        for word in word1:
            x += word

        for word in word2:
            y += word

        return x==y