class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        boxes = defaultdict(set)
        for i in range(9):
            counted_row = set()
            counted_column = set()
            for j in range(9):
                row_item = board[i][j]
                if row_item != ".":
                    if row_item in counted_row:
                        return False
                    else:
                        counted_row.add(row_item)
                column_item = board[j][i]
                if column_item != ".":
                    if column_item in counted_column:
                        return False
                    else:
                        counted_column.add(column_item)
                box_key = (i // 3, j // 3)
                item = board[i][j]
                if item != ".":
                    if item in boxes[box_key]:
                        return False
                    else:
                        boxes[box_key].add(item)
        return True
