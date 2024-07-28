import tkinter as tk

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inné Sports App")
        self.geometry("600x400")
        
        self.label1 = tk.Label(self, text="Welcome to Inné Sports App")  # Welcome label
        self.label1.pack()
        
        self.button1 = tk.Button(self, text="Open Second Window", command=self.open_second_window)
        self.button1.pack()
        
        self.exit_button = tk.Button(self, text="Exit", command=self.exit_app)
        self.exit_button.pack()

    def open_second_window(self):
        # Opens a new window when the button is clicked
        self.new_window = tk.Toplevel(self)
        self.app = SecondWindow(self.new_window)

    def exit_app(self):
        self.destroy()

class SecondWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Second Window")
        self.master.geometry("400x300")
        
        self.label2 = tk.Label(self.master, text="This is the second window")  # Label in the second window
        self.label2.pack()
        
        self.button2 = tk.Button(self.master, text="Close", command=self.master.destroy)
        self.button2.pack()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
