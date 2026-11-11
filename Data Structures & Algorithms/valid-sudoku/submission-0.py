from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_map = defaultdict(set)
        columns_map = defaultdict(set)
        squares_map = defaultdict(set)

        for row in range(9):
            for col in range(9):
                square_num = (row//3)*3 + col//3

                element = board[row][col]

                if element == ".":
                    continue
                
                if element in rows_map[row] or element in columns_map[col] or element in  squares_map[square_num]:
                    return False
                
                rows_map[row].add(element)
                columns_map[col].add(element)
                squares_map[square_num].add(element)

        return True
