import tkinter as tk
from tkinter import messagebox
import os

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("9x9 Tic Tac Toe")
        self.root.geometry("600x600")
        self.root.configure(bg='lightblue')  # Set the background color of the main window

        # 9x9 board
        self.board = [['' for _ in range(9)] for _ in range(9)]
        self.current_player = "🦋"  # X starts

        # Add label above the buttons
        self.instruction_label = tk.Label(self.root, text="5 in a row!", font=("Arial", 20), bg='blue')
        self.instruction_label.grid(row=0, column=0, columnspan=9)

        # Create 9x9 grid of buttons
        self.buttons = [
            [tk.Button(self.root, text='', font='Arial 14', width=4, height=2,
                       bg='lightblue', activebackground='blue',
                       command=lambda row=row, col=col: self.on_button_click(row, col))
             for col in range(9)] for row in range(9)
        ]

        for row in range(9):
            for col in range(9):
                self.buttons[row][col].grid(row=row + 1, column=col)  # Adjusted row to start from 1

        # Restart Button
        self.restart_button = tk.Button(self.root, text="Restart", command=self.reset_board, font=("Arial", 14),
                                        bg='lightblue', activebackground='skyblue')
        self.restart_button.grid(row=10, column=0, columnspan=9)

        # Home Button
        self.home_button = tk.Button(self.root, text="Home", command=self.go_home, font=("Arial", 14),
                                     bg='lightblue', activebackground='skyblue')
        self.home_button.grid(row=11, column=0, columnspan=9)

    def on_button_click(self, row, col):
        """Handle button click event"""
        if self.board[row][col] == '':  # Only make a move if the cell is empty
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            # Check for winner after the move
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif all(self.board[r][c] != '' for r in range(9) for c in range(9)):  # Check for draw
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                # Switch player turn
                self.current_player = "🐣" if self.current_player == "🦋" else "🦋"

    def check_winner(self):
        """Check if the current player has won"""
        # Check rows, columns, and diagonals for a winning line of 5
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == self.current_player:
                    # Check horizontal
                    if j + 4 < 9 and all(self.board[i][j + k] == self.current_player for k in range(5)):
                        return True
                    # Check vertical
                    if i + 4 < 9 and all(self.board[i + k][j] == self.current_player for k in range(5)):
                        return True
                    # Check diagonal (top-left to bottom-right)
                    if i + 4 < 9 and j + 4 < 9 and all(self.board[i + k][j + k] == self.current_player for k in range(5)):
                        return True
                    # Check diagonal (top-right to bottom-left)
                    if i + 4 < 9 and j - 4 >= 0 and all(self.board[i + k][j - k] == self.current_player for k in range(5)):
                        return True
        return False

    def reset_board(self):
        """Reset the game board"""
        self.board = [['' for _ in range(9)] for _ in range(9)]
        for row in range(9):
            for col in range(9):
                self.buttons[row][col].config(text='')
        self.current_player = "🦋"  # X starts

    def go_home(self):
        """Redirect to home.py"""
        self.root.quit()  # Close the current Tkinter window
        os.system('python players.py')  # Execute home.py script (ensure home.py is in the same directory)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
