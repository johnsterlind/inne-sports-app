import tkinter as tk
from tkinter import messagebox

class InneApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inné Community Sports Engagement App")
        self.create_main_window()

    def create_main_window(self):
        # Main window layout
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=20)

        welcome_label = tk.Label(self.main_frame, text="Welcome to Inné Sports Engagement App")
        welcome_label.pack(pady=10)

        create_event_button = tk.Button(self.main_frame, text="Create Event", command=self.open_create_event_window)
        create_event_button.pack(pady=5)

        join_event_button = tk.Button(self.main_frame, text="Join Event", command=self.open_join_event_window)
        join_event_button.pack(pady=5)

        book_amenity_button = tk.Button(self.main_frame, text="Book Amenity", command=self.open_book_amenity_window)
        book_amenity_button.pack(pady=5)

        view_top_players_button = tk.Button(self.main_frame, text="View Top Players", command=self.open_view_top_players_window)
        view_top_players_button.pack(pady=5)

        exit_button = tk.Button(self.main_frame, text="Exit", command=self.root.quit)
        exit_button.pack(pady=5)

    def open_create_event_window(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Create Event")

        create_event_label = tk.Label(self.new_window, text="Create a New Sports Event")
        create_event_label.pack(pady=10)

        tk.Label(self.new_window, text="Event Name:").pack(pady=5)
        self.event_name_entry = tk.Entry(self.new_window)
        self.event_name_entry.pack(pady=5)

        tk.Label(self.new_window, text="Date:").pack(pady=5)
        self.event_date_entry = tk.Entry(self.new_window)
        self.event_date_entry.pack(pady=5)

        tk.Label(self.new_window, text="Time:").pack(pady=5)
        self.event_time_entry = tk.Entry(self.new_window)
        self.event_time_entry.pack(pady=5)

        tk.Label(self.new_window, text="Location:").pack(pady=5)
        self.event_location_entry = tk.Entry(self.new_window)
        self.event_location_entry.pack(pady=5)

        submit_button = tk.Button(self.new_window, text="Submit", command=self.submit_event)
        submit_button.pack(pady=5)

        cancel_button = tk.Button(self.new_window, text="Cancel", command=self.new_window.destroy)
        cancel_button.pack(pady=5)

    def submit_event(self):
        name = self.event_name_entry.get()
        date = self.event_date_entry.get()
        time = self.event_time_entry.get()
        location = self.event_location_entry.get()
        if not name or not date or not time or not location:
            messagebox.showerror("Error", "All fields are required!")
        else:
            messagebox.showinfo("Success", f"Event '{name}' created successfully!")
            self.new_window.destroy()

    def open_join_event_window(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Join Event")

        join_event_label = tk.Label(self.new_window, text="Join an Existing Sports Event")
        join_event_label.pack(pady=10)

        self.event_listbox = tk.Listbox(self.new_window)
        self.event_listbox.pack(pady=5)

        # Dummy data for available events
        events = ["Soccer Match", "Basketball Game", "Tennis Tournament"]
        for event in events:
            self.event_listbox.insert(tk.END, event)

        join_button = tk.Button(self.new_window, text="Join", command=self.join_event)
        join_button.pack(pady=5)

        cancel_button = tk.Button(self.new_window, text="Cancel", command=self.new_window.destroy)
        cancel_button.pack(pady=5)

    def join_event(self):
        selected_event = self.event_listbox.get(tk.ACTIVE)
        if selected_event:
            messagebox.showinfo("Success", f"You have joined the event: {selected_event}")
            self.new_window.destroy()
        else:
            messagebox.showerror("Error", "Please select an event to join.")

    def open_book_amenity_window(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Book Amenity")

        book_amenity_label = tk.Label(self.new_window, text="Book a Sports Amenity")
        book_amenity_label.pack(pady=10)

        tk.Label(self.new_window, text="Amenity Type:").pack(pady=5)
        self.amenity_type_entry = tk.Entry(self.new_window)
        self.amenity_type_entry.pack(pady=5)

        tk.Label(self.new_window, text="Date:").pack(pady=5)
        self.amenity_date_entry = tk.Entry(self.new_window)
        self.amenity_date_entry.pack(pady=5)

        tk.Label(self.new_window, text="Time:").pack(pady=5)
        self.amenity_time_entry = tk.Entry(self.new_window)
        self.amenity_time_entry.pack(pady=5)

        book_button = tk.Button(self.new_window, text="Book", command=self.book_amenity)
        book_button.pack(pady=5)

        cancel_button = tk.Button(self.new_window, text="Cancel", command=self.new_window.destroy)
        cancel_button.pack(pady=5)

    def book_amenity(self):
        amenity_type = self.amenity_type_entry.get()
        date = self.amenity_date_entry.get()
        time = self.amenity_time_entry.get()
        if not amenity_type or not date or not time:
            messagebox.showerror("Error", "All fields are required!")
        else:
            messagebox.showinfo("Success", f"Amenity '{amenity_type}' booked successfully!")
            self.new_window.destroy()

    def open_view_top_players_window(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Top Players")

        view_top_players_label = tk.Label(self.new_window, text="Top Players in the Community")
        view_top_players_label.pack(pady=10)

        self.top_players_listbox = tk.Listbox(self.new_window)
        self.top_players_listbox.pack(pady=5)

        # Dummy data for top players
        players = ["Player1", "Player2", "Player3"]
        for player in players:
            self.top_players_listbox.insert(tk.END, player)

        tip_button = tk.Button(self.new_window, text="Tip Player", command=self.tip_player)
        tip_button.pack(pady=5)

        back_button = tk.Button(self.new_window, text="Back", command=self.new_window.destroy)
        back_button.pack(pady=5)

    def tip_player(self):
        selected_player = self.top_players_listbox.get(tk.ACTIVE)
        if selected_player:
            messagebox.showinfo("Success", f"You have tipped: {selected_player}")
            self.new_window.destroy()
        else:
            messagebox.showerror("Error", "Please select a player to tip.")

if __name__ == "__main__":
    root = tk.Tk()
    app = InneApp(root)
    root.mainloop()
