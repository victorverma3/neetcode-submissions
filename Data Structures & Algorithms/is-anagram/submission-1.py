class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for s_i, t_i in zip(s, t):
            d1[s_i] += 1
            d2[t_i] += 1
        
        return d1 == d2