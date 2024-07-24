import tkinter as tk

class MyCalculator :
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x300")
        self.root.title("My Calculator")
        self.root.mainloop()

MyCalculator()