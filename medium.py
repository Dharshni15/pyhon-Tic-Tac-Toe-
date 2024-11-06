import tkinter as tk
from tkinter import messagebox
from enum import Enum
import os

class Symbol(Enum):
    PLAYER = "❤️"
    AI = "🩵"
    EMPTY = " "

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe - Single Player")
        self.master.geometry("500x500")

        self.board = [Symbol.EMPTY] * 9
        self.buttons = [None] * 9
        self.current_player = Symbol.PLAYER

        self.create_buttons()
        self.status_label = tk.Label(master, text="Your turn (❤️)", font=("Arial", 16))
        self.status_label.grid(row=3, column=0, columnspan=3)

        self.restart_button = tk.Button(master, text="Restart", command=self.restart_game, font=("Arial", 14))
        self.restart_button.grid(row=4, column=0)

        self.home_button = tk.Button(master, text="Home", command=self.go_home, font=("Arial", 14))
        self.home_button.grid(row=4, column=2)

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.master, text=" ", font=("Arial", 20), width=5, height=2,
                               command=lambda idx=i: self.player_move(idx))
            button.grid(row=i // 3, column=i % 3)
            self.buttons[i] = button

    def player_move(self, idx):
        if self.board[idx] == Symbol.EMPTY:
            self.board[idx] = Symbol.PLAYER
            self.buttons[idx].config(text=Symbol.PLAYER.value)
            if self.check_winner(Symbol.PLAYER):
                self.end_game("You win!")
            elif self.is_draw():
                self.end_game("It's a draw!")
            else:
                self.current_player = Symbol.AI
                self.status_label.config(text="AI's turn (🩵)")
                self.ai_move()

    def ai_move(self):
        best_move = self.minimax(self.board, Symbol.AI)[1]
        if best_move is not None:
            self.board[best_move] = Symbol.AI
            self.buttons[best_move].config(text=Symbol.AI.value)
            if self.check_winner(Symbol.AI):
                self.end_game("AI wins!")
            elif self.is_draw():
                self.end_game("It's a draw!")
            else:
                self.current_player = Symbol.PLAYER
                self.status_label.config(text="Your turn (❤️)")

    def minimax(self, board, player):
        winner = self.check_winner(Symbol.PLAYER)
        if winner:
            return -1, None
        winner = self.check_winner(Symbol.AI)
        if winner:
            return 1, None
        if self.is_draw():
            return 0, None

        moves = []
        for i in range(9):
            if board[i] == Symbol.EMPTY:
                board[i] = player
                score = self.minimax(board, Symbol.PLAYER if player == Symbol.AI else Symbol.AI)[0]
                board[i] = Symbol.EMPTY
                moves.append((score, i))

        if player == Symbol.AI:
            best_move = max(moves, key=lambda x: x[0])
        else:
            best_move = min(moves, key=lambda x: x[0])

        return best_move

    def check_winner(self, symbol):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)  # Diagonals
        ]
        for combo in winning_combinations:
            if all(self.board[i] == symbol for i in combo):
                return True
        return False

    def is_draw(self):
        return all(square != Symbol.EMPTY for square in self.board)

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.disable_buttons()

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)

    def restart_game(self):
        self.board = [Symbol.EMPTY] * 9
        self.current_player = Symbol.PLAYER
        self.status_label.config(text="Your turn (❤️)")
        for button in self.buttons:
            button.config(text=" ", state=tk.NORMAL)

    def go_home(self):
        os.system('python players.py')
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
