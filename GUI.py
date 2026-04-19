import tkinter as tk #GUI library for Python, used to create the application interface
from tkinter import messagebox #Used for displaying pop-up messages to the user (e.g., error or success notifications)

class TrackerApp: #Main application class that manages the GUI and user interactions

    def __init__(self, root):#Initializes the application, sets up the main window, and defines standard thresholds and color palette for a professional look.
        self.root = root
        self.root.title("IY499 Student Attendance & Grade Tracker")
        self.root.geometry("600x500")
        
        # Standards and thresholds 
        self.grade_threshold = 40
        self.attendance_threshold = 80
        
        # Color palette for professional look
        self.blue_bg = "#005eb8"
        self.white_fg = "#ffffff"
        
        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)
        
        self.show_login()

    def clear_screen(self):
        """Clears current frame widgets to allow for a new menu."""
        for widget in self.container.winfo_children():
            widget.destroy()

    # --- LOGIN MENU ---
    def show_login(self):
        self.clear_screen()
        tk.Label(self.container, text="University of York - Login", font=("Arial", 16, "bold")).pack(pady=30)
        
        # Enlarged inputs for better accessibility 
        tk.Label(self.container, text="Username:", font=("Arial", 12)).pack()
        self.user_entry = tk.Entry(self.container, font=("Arial", 14), width=25)
        self.user_entry.pack(pady=10)

        tk.Label(self.container, text="Password:", font=("Arial", 12)).pack()
        self.pass_entry = tk.Entry(self.container, show="*", font=("Arial", 14), width=25)
        self.pass_entry.pack(pady=10)

        # Large Blue Button with White Text
        login_btn = tk.Button(
            self.container, text="Login", font=("Arial", 12, "bold"),
            bg=self.blue_bg, fg=self.white_fg, width=15, height=2,
            command=self.handle_login
        )
        login_btn.pack(pady=20)

    def handle_login(self):
        """Simple validation check."""
        if self.user_entry.get() == "admin" and self.pass_entry.get() == "york2026":
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid Credentials")

    # --- MAIN MENU ---
    def show_main_menu(self):
        self.clear_screen()
        tk.Label(self.container, text="Main Menu", font=("Arial", 16, "bold")).pack(pady=20)
        
        # Horizontal button line
        btn_frame = tk.Frame(self.container)
        btn_frame.pack(pady=40)
        
        tk.Button(btn_frame, text="Change Threshold", width=15, command=self.show_threshold_menu).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Add Details", width=15).pack(side="left", padx=10)
        tk.Button(btn_frame, text="View Student", width=15).pack(side="left", padx=10)

        # Logout button centered below middle button
        logout_btn = tk.Button(
            self.container, text="Log out", font=("Arial", 10, "bold"),
            bg=self.blue_bg, fg=self.white_fg, width=15, command=self.show_login
        )
        logout_btn.pack(pady=10)

    # --- THRESHOLD MENU ---
    def show_threshold_menu(self):
        self.clear_screen()
        tk.Label(self.container, text="Threshold Settings", font=("Arial", 14, "bold")).pack(pady=20)
        
        tk.Button(self.container, text="Change Grade Threshold", width=25, 
                  command=lambda: self.show_slider_page("Grade")).pack(pady=10)
        tk.Button(self.container, text="Change Attendance Threshold", width=25, 
                  command=lambda: self.show_slider_page("Attendance")).pack(pady=10)
        
        # Back button at the bottom 
        tk.Button(self.container, text="Back", bg=self.blue_bg, fg=self.white_fg, 
                  width=15, command=self.show_main_menu).pack(pady=30)

    # --- SLIDER PAGE (Unified for both Grade & Attendance) ---
    def show_slider_page(self, mode):
        self.clear_screen()
        title_text = f"{mode} Threshold"
        tk.Label(self.container, text=title_text, font=("Arial", 14, "bold")).pack(pady=10)

        # Vertical Slider setup 
        current_val = self.grade_threshold if mode == "Grade" else self.attendance_threshold
        
        # Label to display current result besides slider
        val_label = tk.Label(self.container, text=f"Current: {current_val}%", font=("Arial", 12))
        val_label.pack()

        slider = tk.Scale(
            self.container, from_=100, to=0, orient="vertical", 
            length=300, tickinterval=10, resolution=1,
            command=lambda v: val_label.config(text=f"Selection: {v}%")
        )
        slider.set(current_val)
        slider.pack(side="left", padx=100)

        # Control Buttons
        btn_container = tk.Frame(self.container)
        btn_container.pack(side="right", padx=50)

        tk.Button(btn_container, text="Enter", width=10, 
                  command=lambda: self.confirm_threshold(mode, slider.get())).pack(pady=5)
        tk.Button(btn_container, text="Back", bg=self.blue_bg, fg=self.white_fg, 
                  width=10, command=self.show_threshold_menu).pack(pady=5)

    def confirm_threshold(self, mode, value):
        """Saves change and returns to main menu[cite: 16, 53]."""
        if mode == "Grade":
            self.grade_threshold = value
        else:
            self.attendance_threshold = value
            
        messagebox.showinfo("Success", "Threshold changed")
        self.show_main_menu()

if __name__ == "__main__": #Entry point of the application, creates the main window and starts the GUI event loop.
    root = tk.Tk()
    app = TrackerApp(root)
    root.mainloop()                          
