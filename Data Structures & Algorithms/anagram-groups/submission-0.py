class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            a = [0] * 26
            for char in word:
                a[ord(char) - ord("a")] += 1
            anagrams[tuple(a)].append(word)

        res = [val for val in anagrams.values()]
        return res