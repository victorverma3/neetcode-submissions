class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        left = 0
        while left < len(s):
            curr = left
            while s[curr] != "#":
                curr += 1
            length = int(s[left:curr])
            decoded.append(s[curr+1:curr+1+length])
            left = curr+1+length

        return decoded