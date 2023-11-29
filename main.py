import tkinter as tkinter

class Mycalculator:
    def __init__(self):

        self.root = tk.Tk()

         self.root.geometry("300x300")
        self.root.title("Calculator ngub")

        self.label = tk.Label(self.root, text="Hello DIP01", font= ("Arial", 18))
        self.label.pack()

        self.button = tk.Button(self.root, text="Click here")
        self.button.place(x=20, y=50)

        self.root.mainloop()

MyCalculator()