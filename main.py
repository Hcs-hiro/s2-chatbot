import tkinter as tk
from app import Application

def main():
    root = tk.Tk()
    app = Application(root)
    app.mainloop()

if __name__ == "__main__":
    main()
