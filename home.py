import tkinter as tk
import subprocess


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("500x500")
        self.root.configure(bg='lightblue')

        # Directly show level selection options
        self.show_buttons()

    def show_buttons(self):
        self.level_label = tk.Label(self.root, text="Select the level you like to play", font='Arial 20',
                                    bg='lightblue')
        self.level_label.pack(pady=20)

        # Simple Button (Easy level)
        self.simple_button = tk.Button(self.root, text="Simple🤩", font='Arial 14', width=10,
                                       bg='deepskyblue', activebackground='dodgerblue',
                                       command=self.run_simple)
        self.simple_button.pack(pady=10)

        # Complex Button (Medium level)
        self.complex_button = tk.Button(self.root, text="Complex🤯", font='Arial 14', width=10,
                                        bg='deepskyblue', activebackground='dodgerblue',
                                        command=self.run_complex)
        self.complex_button.pack(pady=10)

        # Show Rules Button


    def run_simple(self):
        """Run the 'easy.py' game"""
        subprocess.run(["python", "easy.py"])

    def run_complex(self):
        """Run the 'medium.py' game"""
        subprocess.run(["python", "medium.py"])



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
