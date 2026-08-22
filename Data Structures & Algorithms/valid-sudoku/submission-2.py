class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sub_boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                char = board[r][c]
                if char == ".":
                    continue
                if char in rows[r]:
                    return False
                rows[r].add(char)
                if char in cols[c]:
                    return False
                cols[c].add(char)
                if char in sub_boxes[(r // 3, c // 3)]:
                    return False
                sub_boxes[(r // 3, c // 3)].add(char)
        
        return True