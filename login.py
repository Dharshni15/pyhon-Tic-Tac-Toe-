import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to connect to the database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="",  # Replace with your MySQL password
        database="python"  # Your database name
    )

class SignupPage:
    def __init__(self, master):  # Corrected the constructor name
        self.master = master
        self.master.title("Signup")
        self.master.geometry("500x500")
        self.master.configure(bg="white")

        tk.Label(self.master, text="Username:", bg="pink", font=("Arial", 18)).pack(pady=10)
        self.username_entry = tk.Entry(self.master, font=("Arial", 18))
        self.username_entry.pack(pady=5)

        tk.Label(self.master, text="Password:", bg="pink", font=("Arial", 18)).pack(pady=10)
        self.password_entry = tk.Entry(self.master, show="*", font=("Arial", 18))
        self.password_entry.pack(pady=5)

        tk.Button(self.master, text="Create Account", command=self.signup, bg="#4CAF50", fg="black",
                  font=("Arial", 18)).pack(pady=10)

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if fields are empty
        if not username or not password:
            messagebox.showerror("Error", "Username and password cannot be empty!")
            return

        try:
            connection = connect_to_database()  # Connect to the database
            cursor = connection.cursor()

            # Check if user already exists
            cursor.execute("SELECT * FROM login WHERE username = %s", (username,))
            if cursor.fetchone():
                messagebox.showerror("Error", "User already exists!")
            else:
                # Insert new user
                cursor.execute("INSERT INTO login (username, password) VALUES (%s, %s)", (username, password))
                connection.commit()  # Save changes
                messagebox.showinfo("Success", "Signup successful!")
                self.master.destroy()  # Close the signup window
                self.open_login_page()  # Open the login page

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals():
                connection.close()  # Close the database connection

    def open_login_page(self):
        login_window = tk.Toplevel(self.master)  # Use Toplevel to create a new window
        LoginPage(login_window)  # Pass the new window to the LoginPage

class LoginPage:
    def __init__(self, master):  # Corrected the constructor name
        self.master = master
        self.master.title("Login")
        self.master.geometry("500x500")
        self.master.configure(bg="white")

        tk.Label(self.master, text="Username:", bg="pink", font=("Arial", 18)).pack(pady=10)
        self.username_entry = tk.Entry(self.master, font=("Arial", 18))
        self.username_entry.pack(pady=5)

        tk.Label(self.master, text="Password:", bg="pink", font=("Arial", 18)).pack(pady=10)
        self.password_entry = tk.Entry(self.master, show="*", font=("Arial", 18))
        self.password_entry.pack(pady=5)

        tk.Button(self.master, text="Login", command=self.login, bg="#4CAF50", fg="black", font=("Arial", 18)).pack(
            pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if fields are empty
        if not username or not password:
            messagebox.showerror("Error", "Username and password cannot be empty!")
            return

        try:
            connection = connect_to_database()  # Connect to the database
            cursor = connection.cursor()

            # Check credentials
            cursor.execute("SELECT * FROM login WHERE username = %s AND password = %s", (username, password))
            if cursor.fetchone():
                messagebox.showinfo("Success", "Login successful!")
            else:
                messagebox.showerror("Error", "Invalid username or password.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals():
                connection.close()  # Close the database connection

# Start the application
if __name__ == "__main__":  # Corrected the name check
    root = tk.Tk()
    app = SignupPage(root)  # Start with the signup page
    root.mainloop()