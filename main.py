import tkinter as tk

class Mycalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x300")
        self.root.title("Calculator ngub")

        self.label = tk.Label(self.root, text="Hello DIP01", font= ("Arial", 18))
        self.label.pack()

        self.button = tk.Button(self.root, text="AC")
        self.button.place(x=20, y=50)

        self.button = tk.Button(self.root, text="+/-")
        self.button.place(x=50, y=50)

        self.button = tk.Button(self.root, text="%")
        self.button.place(x=80, y=50)

        self.button = tk.Button(self.root, text="7")
        self.button.place(x=20, y=80)

        self.button = tk.Button(self.root, text="8")
        self.button.place(x=50, y=80)

        self.button = tk.Button(self.root, text="9")
        self.button.place(x=80, y=80)


        self.root.mainloop()

Mycalculator()