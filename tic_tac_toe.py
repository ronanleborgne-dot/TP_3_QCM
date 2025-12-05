import numpy as np 

class TicTacToe():

    def __init__(self) :
        self.board = np.zeros((3,3), dtype=int)
        self.current_player = 1  # Player 1 starts

    def play(self, row, col):
        if row < 0 or row > 2 or col < 0 or col > 2:
            raise ValueError("Row and column must be between 0 and 2.")
        if self.board[row, col] != 0:
            raise ValueError("Cell is already occupied.")
        self.board[row, col] = self.current_player
        if not self.check_winner():
            self.cuurrent_player = 1-self.current_player

    def check_winner(self):
        for i in range(3):
            if np.all(self.board[i, :] == self.current_player) or np.all(self.board[:, i] == self.current_player):
                return True
        if np.all(np.diag(self.board) == self.current_player) or np.all(np.diag(np.fliplr(self.board)) == self.current_player):
            return True
        return False
    
    def is_draw(self):
        return np.all(self.board != 0) and not self.check_winner()
    
    

    
