import tkinter as tk

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inné Sports App")
        self.geometry("600x400")
        
        # Main menu widgets
        self.label1 = tk.Label(self, text="Welcome to Inné Sports App")
        self.label1.pack(pady=20)
        
        self.create_event_button = tk.Button(self, text="Create Event", command=self.open_create_event_window)
        self.create_event_button.pack(pady=10)
        
        self.join_event_button = tk.Button(self, text="Join Event", command=self.open_join_event_window)
        self.join_event_button.pack(pady=10)
        
        self.view_top_players_button = tk.Button(self, text="View Top Players", command=self.open_top_players_window)
        self.view_top_players_button.pack(pady=10)
        
        self.exit_button = tk.Button(self, text="Exit", command=self.exit_app)
        self.exit_button.pack(pady=20)

    def open_create_event_window(self):
        CreateEventWindow(self)

    def open_join_event_window(self):
        JoinEventWindow(self)

    def open_top_players_window(self):
        TopPlayersWindow(self)

    def exit_app(self):
        self.destroy()

class CreateEventWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Create Event")
        self.geometry("400x300")
        
        self.label = tk.Label(self, text="Create Event")
        self.label.pack(pady=20)
        
        self.event_name_label = tk.Label(self, text="Event Name:")
        self.event_name_label.pack(pady=10)
        
        self.event_name_entry = tk.Entry(self)
        self.event_name_entry.pack(pady=10)
        
        self.create_button = tk.Button(self, text="Create", command=self.create_event)
        self.create_button.pack(pady=10)
        
        self.back_button = tk.Button(self, text="Back to Main Menu", command=self.destroy)
        self.back_button.pack(pady=10)

    def create_event(self):
        event_name = self.event_name_entry.get()
        if event_name:
            print(f"Event '{event_name}' created!")
        else:
            print("Event name cannot be empty.")

class JoinEventWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Join Event")
        self.geometry("400x300")
        
        self.label = tk.Label(self, text="Join Event")
        self.label.pack(pady=20)
        
        self.event_list_label = tk.Label(self, text="Select Event:")
        self.event_list_label.pack(pady=10)
        
        self.event_listbox = tk.Listbox(self)
        self.event_listbox.pack(pady=10)
        # Add example events
        for event in ["Event 1", "Event 2", "Event 3"]:
            self.event_listbox.insert(tk.END, event)
        
        self.join_button = tk.Button(self, text="Join", command=self.join_event)
        self.join_button.pack(pady=10)
        
        self.back_button = tk.Button(self, text="Back to Main Menu", command=self.destroy)
        self.back_button.pack(pady=10)

    def join_event(self):
        selected_event = self.event_listbox.get(tk.ACTIVE)
        if selected_event:
            print(f"Joined '{selected_event}'!")
        else:
            print("Please select an event.")

class TopPlayersWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Top Players")
        self.geometry("400x300")
        
        self.label = tk.Label(self, text="Top Players")
        self.label.pack(pady=20)
        
        self.top_players_listbox = tk.Listbox(self)
        self.top_players_listbox.pack(pady=10)
        # Add example top players
        for player in ["Player 1", "Player 2", "Player 3"]:
            self.top_players_listbox.insert(tk.END, player)
        
        self.back_button = tk.Button(self, text="Back to Main Menu", command=self.destroy)
        self.back_button.pack(pady=10)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
