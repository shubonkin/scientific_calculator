import tkinter as tk
from tkinter import Menu, messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")

        self.is_scientific = True

        # Menu setup
        self.menu_bar = Menu(self.root)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Standard Calculator", command=self.switch_to_standard)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit Application", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="About Application", command=self.show_about)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        self.root.config(menu=self.menu_bar)

        # Entry field
        self.entry = tk.Entry(self.root, font=("Arial", 18), bd=10, relief=tk.RIDGE, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        # Button layout
        self.create_buttons()

    def create_buttons(self):
        self.clear_buttons()
        
        if self.is_scientific:
            self.add_scientific_buttons()
        else:
            self.add_standard_buttons()

    def clear_buttons(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

    def add_scientific_buttons(self):
        self.add_standard_buttons()
        sci_buttons = [
            ("sin", 1, 0), ("cos", 1, 1), ("tan", 1, 2), ("sqrt", 1, 3), 
            ("log", 2, 0), ("ln", 2, 1), ("^", 2, 2), ("pi", 2, 3)
        ]
        for (text, row, col) in sci_buttons:
            self.add_button(text, row, col)

    def add_standard_buttons(self):
        buttons = [
            ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("/", 3, 3),
            ("4", 4, 0), ("5", 4, 1), ("6", 4, 2), ("*", 4, 3),
            ("1", 5, 0), ("2", 5, 1), ("3", 5, 2), ("-", 5, 3),
            ("0", 6, 0), (".", 6, 1), ("=", 6, 2), ("+", 6, 3),
            ("C", 7, 0)  
        ]
        for (text, row, col) in buttons:
            self.add_button(text, row, col)

    

    def add_button(self, text, row, col):
        button = tk.Button(self.root, text=text, font=("Arial", 14), bd=5, relief=tk.RAISED,
                           command=lambda t=text: self.on_button_click(t))
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        self.root.grid_rowconfigure(row, weight=1)
        self.root.grid_columnconfigure(col, weight=1)

    def on_button_click(self, button_text):
        if button_text == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button_text == "C":
            self.entry.delete(0, tk.END)
        elif button_text in {"sin", "cos", "tan", "sqrt", "log", "ln", "pi", "^"}:
            messagebox.showinfo("Scientific Function", f"Handle '{button_text}' logic here.")
        else:
            self.entry.insert(tk.END, button_text)

    def switch_to_standard(self):
        self.is_scientific = False
        self.root.title("Standard Calculator")
        self.create_buttons()

    def show_about(self):
        messagebox.showinfo("About", "Made by: Ceasar Jay A. Cayanong.")


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
