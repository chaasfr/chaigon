import tkinter as tk
from safe_eval import safe_eval

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.expression = ""
        self.input_text = tk.StringVar()

        # Input field
        self.input_frame = tk.Frame(master, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        self.input_frame.pack(side=tk.TOP)

        self.input_field = tk.Entry(self.input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)

        # Buttons frame
        self.buttons_frame = tk.Frame(master, width=312, height=272.5, bg="grey")
        self.buttons_frame.pack()

        # First row
        self.clear = tk.Button(self.buttons_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: self.clear_all()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
        self.divide = tk.Button(self.buttons_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: self.press("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

        # Second row
        self.seven = tk.Button(self.buttons_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.press("7")).grid(row = 1, column = 0, padx = 1, pady = 1)
        self.eight = tk.Button(self.buttons_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.press("8")).grid(row = 1, column = 1, padx = 1, pady = 1)
        self.nine = tk.Button(self.buttons_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.press("9")).grid(row = 1, column = 2, padx = 1, pady = 1)
        self.multiply = tk.Button(self.buttons_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: self.press("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

        # Third row
        self.four = tk.Button(self.buttons_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.press("4")).grid(row = 2, column = 0, padx = 1, pady = 1)
        self.five = tk.Button(self.buttons_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.press("5")).grid(row = 2, column = 1, padx = 1, pady = 1)
        self.six = tk.Button(self.buttons_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.press("6")).grid(row = 2, column = 2, padx = 1, pady = 1)
        self.subtract = tk.Button(self.buttons_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: self.press("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

        # Fourth row
        self.one = tk.Button(self.buttons_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.press("1")).grid(row = 3, column = 0, padx = 1, pady = 1)
        self.two = tk.Button(self.buttons_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.press("2")).grid(row = 3, column = 1, padx = 1, pady = 1)
        self.three = tk.Button(self.buttons_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.press("3")).grid(row = 3, column = 2, padx = 1, pady = 1)
        self.add = tk.Button(self.buttons_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: self.press("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

        # Fifth row
        self.zero = tk.Button(self.buttons_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.press("0")).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
        self.point = tk.Button(self.buttons_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: self.press(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
        self.equals = tk.Button(self.buttons_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: self.equalpress()).grid(row = 4, column = 3, padx = 1, pady = 1)

    def press(self, num):
        allowed_chars = "0123456789+-*/.()"
        if num in allowed_chars:
            self.expression += str(num)
            self.input_text.set(self.expression)

    def explode(self):
        # Placeholder for explosion animation logic
        print("Explosion!") # In reality, this would trigger the animation
        pass

    def equalpress(self):
        try:
            print(f'Evaluating expression: {self.expression}')
            self.explode()  # Call the explode function *before* displaying result
            total = str(safe_eval(self.expression))
            self.input_text.set(total)
            self.expression = total
        except ValueError as e:
            self.input_text.set(f"Error: {e}")
            self.expression = ""
        except Exception as e:
            self.input_text.set("Error: Invalid Expression")
            self.expression = ""

    def clear_all(self):
        self.expression = ""
        self.input_text.set("")

root = tk.Tk()
calc = Calculator(root)
root.mainloop()
