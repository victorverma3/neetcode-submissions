class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num == ".":
                    continue

                if num in col[i]:
                    return False
                else:
                    col[i].add(num)
                
                if num in row[j]:
                    return False
                else:
                    row[j].add(num)

                if num in square[(j // 3, i // 3)]:
                    return False
                else:
                    square[(j // 3, i // 3)].add(num)
        
        return True
                
