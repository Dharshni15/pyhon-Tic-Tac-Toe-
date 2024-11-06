import tkinter as tk
from tkinter import messagebox
import os


class UltimateTicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultimate 5x5 Tic Tac Toe")
        self.root.geometry("600x600")
        self.root.configure(bg='lightblue')  # Set the background color of the window

        # 5x5 board
        self.board = [['' for _ in range(5)] for _ in range(5)]
        self.current_player = "🦋"

        # Create 5x5 grid of buttons
        self.buttons = [
            [tk.Button(root, text='', font='Arial 20', width=5, height=2,
                       command=lambda row=row, col=col: self.on_button_click(row, col))
             for col in range(5)] for row in range(5)
        ]

        for row in range(5):
            for col in range(5):
                self.buttons[row][col].grid(row=row, column=col)

        # Restart Button
        self.restart_button = tk.Button(root, text="Restart", command=self.reset_board, font=("Arial", 14),
                                        bg='lightblue', activebackground='skyblue')
        self.restart_button.grid(row=5, column=0, columnspan=5)

        # Home Button
        self.home_button = tk.Button(root, text="Home", command=self.go_home, font=("Arial", 14),
                                     bg='lightblue', activebackground='skyblue')
        self.home_button.grid(row=6, column=0, columnspan=5)

    def on_button_click(self, row, col):
        """Handle button click event"""
        if self.board[row][col] == '':  # Only make a move if the cell is empty
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            # Check for winner
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif all(self.board[r][c] != '' for r in range(5) for c in range(5)):  # Check for draw
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                # Switch player turn
                self.current_player = "🐣" if self.current_player == "🦋" else "🦋"

    def check_winner(self):
        """Check if the current player has won"""
        # Check rows and columns
        for i in range(5):
            if all(self.board[i][j] == self.current_player for j in range(5)) or \
                    all(self.board[j][i] == self.current_player for j in range(5)):
                return True
        # Check diagonals
        if all(self.board[i][i] == self.current_player for i in range(5)) or \
                all(self.board[i][4 - i] == self.current_player for i in range(5)):
            return True
        return False

    def reset_board(self):
        """Reset the game board"""
        self.board = [['' for _ in range(5)] for _ in range(5)]
        for row in range(5):
            for col in range(5):
                self.buttons[row][col].config(text='')
        self.current_player = "🦋"  # X starts

    def go_home(self):
        """Redirect to home.py"""
        self.root.quit()  # Close the current Tkinter window
        os.system('python players.py')  # Execute home.py script (ensure home.py is in the same directory)


if __name__ == "__main__":
    root = tk.Tk()
    game = UltimateTicTacToe(root)
    root.mainloop()
