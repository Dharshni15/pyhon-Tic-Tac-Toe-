import tkinter as tk
import os


class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Main Menu")
        self.root.geometry("400x300")  # Set window size
        self.root.configure(bg='lightblue')  # Set the background color to light blue

        # Title label
        self.title_label = tk.Label(self.root, text="Choose a Tic Tac Toe Grid", font=("Arial", 20), bg='lightblue')
        self.title_label.pack(pady=20)

        # Button for 3x3 Grid
        self.button_3x3 = tk.Button(self.root, text="3x3 Grid", font=("Arial", 14), width=20, height=2,
                                    bg='lightblue', activebackground='skyblue', command=self.open_3x3)
        self.button_3x3.pack(pady=10)

        # Button for 5x5 Grid
        self.button_5x5 = tk.Button(self.root, text="5x5 Grid", font=("Arial", 14), width=20, height=2,
                                    bg='lightblue', activebackground='skyblue', command=self.open_5x5)
        self.button_5x5.pack(pady=10)

        # Button for 9x9 Grid
        self.button_9x9 = tk.Button(self.root, text="9x9 Grid", font=("Arial", 14), width=20, height=2,
                                    bg='lightblue', activebackground='skyblue', command=self.open_9x9)
        self.button_9x9.pack(pady=10)

    def open_3x3(self):
        """Open the easy.py page (3x3 Tic Tac Toe)"""
        self.root.quit()  # Close the current window
        os.system('python 3.py')  # Run the easy.py script

    def open_5x5(self):
        """Open the 5.py page (5x5 Tic Tac Toe)"""
        self.root.quit()  # Close the current window
        os.system('python 5.py')  # Run the 5.py script

    def open_9x9(self):
        """Open the 9.py page (9x9 Tic Tac Toe)"""
        self.root.quit()  # Close the current window
        os.system('python 9.py')  # Run the 9.py script


if __name__ == "__main__":
    root = tk.Tk()
    menu = MainMenu(root)
    root.mainloop()
