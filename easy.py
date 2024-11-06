import tkinter as tk
from tkinter import messagebox
import random
import os

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("500x500")
        self.board = [''] * 9
        self.current_player = "🐵"
        self.ai_player = "🐻‍❄️"

        self.buttons = [tk.Button(root, text='', font='Arial 20', width=5, height=2,
                                   bg='lightblue', activebackground='skyblue',
                                   command=lambda i=i: self.on_button_click(i)) for i in range(9)]

        for i, button in enumerate(self.buttons):
            button.grid(row=i // 3, column=i % 3)

        self.restart_button = tk.Button(root, text="Restart", command=self.reset_board, font=("Arial", 14))
        self.restart_button.grid(row=3, column=0)

        self.home_button = tk.Button(root, text="Home", command=self.go_home, font=("Arial", 14))
        self.home_button.grid(row=3, column=2)

    def on_button_click(self, index):
        if self.board[index] == '':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif '' not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = self.ai_player
                self.ai_move()

    def ai_move(self):
        available_moves = [i for i in range(9) if self.board[i] == '']
        if available_moves:
            move = random.choice(available_moves)
            self.board[move] = self.ai_player
            self.buttons[move].config(text=self.ai_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.ai_player} wins!")
                self.reset_board()
            elif '' not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "🐵"

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                                (0, 4, 8), (2, 4, 6)]  # Diagonals

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != '':
                return True
        return False

    def reset_board(self):
        self.board = [''] * 9
        for button in self.buttons:
            button.config(text='')
        self.current_player = "🐵"

    def go_home(self):
        os.system('python players.py')
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
