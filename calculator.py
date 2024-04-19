import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")

        self.label_instruction = tk.Label(self.master, text="Select operation:")
        self.label_instruction.grid(row=0, column=0, columnspan=2)

        self.button_add = tk.Button(self.master, text="Addition", command=lambda: self.get_operation("+"))
        self.button_add.grid(row=1, column=0, padx=5, pady=5)
        self.button_subtract = tk.Button(self.master, text="Subtraction", command=lambda: self.get_operation("-"))
        self.button_subtract.grid(row=1, column=1, padx=5, pady=5)
        self.button_multiply = tk.Button(self.master, text="Multiplication", command=lambda: self.get_operation("*"))
        self.button_multiply.grid(row=2, column=0, padx=5, pady=5)
        self.button_divide = tk.Button(self.master, text="Division", command=lambda: self.get_operation("/"))
        self.button_divide.grid(row=2, column=1, padx=5, pady=5)

        self.label_num1 = tk.Label(self.master, text="Enter first number:")
        self.label_num1.grid(row=3, column=0, padx=5, pady=5)
        self.entry_num1 = tk.Entry(self.master)
        self.entry_num1.grid(row=3, column=1, padx=5, pady=5)

        self.label_num2 = tk.Label(self.master, text="Enter second number:")
        self.label_num2.grid(row=4, column=0, padx=5, pady=5)
        self.entry_num2 = tk.Entry(self.master)
        self.entry_num2.grid(row=4, column=1, padx=5, pady=5)

        self.label_result = tk.Label(self.master, text="Result:")
        self.label_result.grid(row=5, column=0, padx=5, pady=5)
        self.result_var = tk.StringVar()
        self.label_display_result = tk.Label(self.master, textvariable=self.result_var)
        self.label_display_result.grid(row=5, column=1, padx=5, pady=5)

    def get_operation(self, operator):
        num1 = float(self.entry_num1.get())
        num2 = float(self.entry_num2.get())
        result = self.calculate(num1, num2, operator)
        self.result_var.set(result)

    def calculate(self, x, y, operator):
        if operator == '+':
            return x + y
        elif operator == '-':
            return x - y
        elif operator == '*':
            return x * y
        elif operator == '/':
            if y == 0:
                return "Error! Division by zero!"
            return x / y
        else:
            return "Invalid operation"

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
