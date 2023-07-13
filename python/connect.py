class ConnectGame:
    def __init__(self, board):
        self.board = [row.replace(" ", "") for row in board.splitlines()]
          

    def get_winner(self):
        for player in ['O', 'X']:
            board = self.board if player == 'O' else [
                [self.board[row][col] for row in range(len(self.board))]
                for col in range(len(self.board[0]))]
            positions = [(0, col) for col, pos in enumerate(board[0]) if pos == player]
            checked = set(positions)
            while positions != []:
                row, col = positions.pop()
                if row == len(board) - 1:
                    return player
                for i, j in [(-1, 1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)]:
                    r = row + i
                    c = col + j
                    if 0 <= r < len(board) and 0 <= c < len(board[0]) \
                            and board[r][c] == player and (r, c) not in checked:
                        positions.append((r, c))
                        checked.add((r, c))
        return ''
