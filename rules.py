import tkinter as tk
from tkinter import messagebox
import os


class RulesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe Rules")
        self.root.geometry("400x400")

        # Display rules in a message box
        rules_text = (
            "Tic Tac Toe Rules\n\n"
            "Game Overview:\n"
            "Tic Tac Toe is a two-player game where one player uses \"X\" (or in your case, the symbol \"🐵\") "
            "and the other uses \"O\" (symbol \"🐻‍❄️\"). The objective is to be the first player to get three of their symbols in a row.\n\n"
            "Game Setup:\n"
            "The game is played on a 3x3 grid.\n"
            "Players take turns placing their symbol in an empty square on the grid.\n\n"
            "Winning the Game:\n"
            "A player wins if they can place three of their symbols in a row. This can be done in several ways:\n"
            "- Horizontally (e.g., in a row).\n"
            "- Vertically (e.g., in a column).\n"
            "- Diagonally (from one corner of the grid to the opposite corner).\n"
            "The game can end when one player has won or when all squares on the grid are filled.\n\n"
            "Draw Condition:\n"
            "If all squares are filled and no player has three symbols in a row, the game is declared a draw.\n\n"
            "Player Turns:\n"
            "Players alternate turns, with one player starting first.\n"
            "Players cannot place their symbol in a square that is already occupied.\n\n"
            "Restarting the Game:\n"
            "Players can choose to restart the game after it ends by clicking the \"Restart\" button.\n\n"
            "Ending the Game:\n"
            "The game ends either when a player wins or when all squares are filled with no winner (draw).\n\n"
            "Starting the Game:\n"
            "The game can be played against an AI opponent or another player, depending on the version of the game."
        )

        messagebox.showinfo("Rules", rules_text)

        # OK Button
        ok_button = tk.Button(self.root, text="OK", command=self.go_home, font=("Arial", 14))
        ok_button.pack(pady=20)

    def go_home(self):
        os.system('python home.py')  # Replace with the actual path to your home.py
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = RulesApp(root)
    root.mainloop()
