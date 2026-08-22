class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = defaultdict(int)
        t_counts = defaultdict(int)

        if len(s) != len(t):
            return False

        for s_char, t_char in zip(s, t):
            s_counts[s_char] += 1
            t_counts[t_char] += 1
        
        return s_counts == t_counts