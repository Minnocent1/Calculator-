import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # create the display widget
        self.display = tk.Entry(master, width=25, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, pady=10)

        # create the buttons
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("=", 4, 2)
        self.create_button("+", 4, 3)

        self.create_button("C", 5, 0, columnspan=2)
        self.create_button("AC", 5, 2, columnspan=2)

    def create_button(self, text, row, column, columnspan=1, pady=10):
        button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 16),
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan, pady=pady)

    def button_click(self, text):
        if text == "C":
            self.display.delete(len(self.display.get())-1)
        elif text == "AC":
            self.display.delete(0, tk.END)
        elif text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, text)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
