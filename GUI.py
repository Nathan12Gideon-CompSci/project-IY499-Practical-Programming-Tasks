import tkinter as tk #Primary library for building the GUI.
from tkinter import messagebox # Displaying error and success messages to the user in a pop-up format.
import File_Handler as file_handler # Custom module for handling file operations related to student records and configuration settings. 
import Logic as logic # same here, the import module is quite a neat tool to modulaize code.
import Visual as visual

class TrackerApp:
    def __init__(self, root): #Initializes the main application window and sets up the initial state of the GUI. 
        self.root = root 
        self.root.title("IY499 Student Tracker")
        self.root.geometry("600x650") 
        
        # UI Styles [cite: 91]
        self.blue_bg = "#005eb8"
        self.white_fg = "#ffffff"
        self.thresholds = file_handler.load_thresholds()
        
        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)
        self.show_login()

    def clear(self):
        for w in self.container.winfo_children(): w.destroy()

    # --- LOGIN ---
    def show_login(self):
        self.clear()
        tk.Label(self.container, text="Student Tracker Login", font=("Arial", 16, "bold")).pack(pady=40)
        
        tk.Label(self.container, text="Username:").pack()
        self.u_entry = tk.Entry(self.container, font=("Arial", 14), width=25)
        self.u_entry.pack(pady=10)

        tk.Label(self.container, text="Password:").pack()
        self.p_entry = tk.Entry(self.container, show="*", font=("Arial", 14), width=25)
        self.p_entry.pack(pady=10)

        tk.Button(self.container, text="Login", bg=self.blue_bg, fg=self.white_fg, 
                  width=13, height=2, font=("Arial", 10, "bold"),
                  command=self.handle_login).pack(pady=20)

    def handle_login(self):
        if self.u_entry.get() == "admin" and self.p_entry.get() == "york2026":
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid Credentials")

    # --- MAIN MENU ---
    def show_main_menu(self):
        self.clear()
        tk.Label(self.container, text="Main Menu", font=("Arial", 18, "bold")).pack(pady=30)
        
        row = tk.Frame(self.container)
        row.pack(pady=20)
        
        btns = [("Change Threshold", self.show_threshold_menu), 
                ("Add Details", self.show_add_name), 
                ("View Students", self.show_view_students)]
        
        for text, cmd in btns:
            tk.Button(row, text=text, width=15, height=2, command=cmd).pack(side="left", padx=10)

        tk.Button(self.container, text="Log out", bg=self.blue_bg, fg=self.white_fg, 
                  width=13, height=2, command=self.show_login).pack(pady=50)

    # --- THRESHOLD WINDOWS ---
    def show_threshold_menu(self):
        self.clear()
        tk.Label(self.container, text="Threshold Settings", font=("Arial", 14, "bold")).pack(pady=20)
        tk.Button(self.container, text="Change Grade Threshold", width=25, height=2, command=lambda: self.show_slider("grade")).pack(pady=5)
        tk.Button(self.container, text="Change Attendance Threshold", width=25, height=2, command=lambda: self.show_slider("attendance")).pack(pady=5)
        tk.Button(self.container, text="Back", bg=self.blue_bg, fg=self.white_fg, width=13, height=2, command=self.show_main_menu).pack(pady=30)

    def show_slider(self, mode):
        self.clear()
        tk.Label(self.container, text=f"Change {mode.capitalize()} Threshold", font=("Arial", 12, "bold")).pack(pady=10)
        
        val_label = tk.Label(self.container, text=f"Value: {self.thresholds[mode]}%", font=("Arial", 12))
        val_label.pack()

        s = tk.Scale(self.container, from_=100, to=0, orient="vertical", length=300, tickinterval=10,
                     command=lambda v: val_label.config(text=f"Value: {v}%"))
        s.set(self.thresholds[mode])
        s.pack(pady=10)

        def save():
            self.thresholds[mode] = int(s.get())
            file_handler.save_thresholds(self.thresholds)
            messagebox.showinfo("Success", "Threshold changed")
            self.show_main_menu()

        tk.Button(self.container, text="Enter", width=13, height=2, command=save).pack()
        tk.Button(self.container, text="Back", bg=self.blue_bg, fg=self.white_fg, width=13, height=2, command=self.show_threshold_menu).pack(pady=5)

    # --- ADD DETAILS FLOW ---
    def show_add_name(self):
        self.clear()
        tk.Label(self.container, text="Enter the name of student (Text Only):").pack(pady=20)
        e = tk.Entry(self.container, font=("Arial", 14), width=25)
        e.pack(pady=10)

        def go_next():
            name = e.get().strip()
            if name.replace(" ","").isalpha() and name: self.show_student_options(name)
            else: messagebox.showerror("Error", "Names must only contain characters.")

        tk.Button(self.container, text="Enter", width=13, height=2, command=go_next).pack()
        tk.Button(self.container, text="Back", bg=self.blue_bg, fg=self.white_fg, width=13, height=2, command=self.show_main_menu).pack(pady=5)

    def show_student_options(self, name):
        self.clear()
        tk.Label(self.container, text=f"Editing: {name}", font=("Arial", 14, "bold")).pack(pady=20)
        tk.Button(self.container, text="Add Grade", width=25, height=2, command=lambda: self.show_grade_input(name)).pack(pady=5)
        tk.Button(self.container, text="Add Attendance", width=25, height=2, command=lambda: self.show_att_input(name)).pack(pady=5)
        tk.Button(self.container, text="Back", bg=self.blue_bg, fg=self.white_fg, width=13, height=2, command=self.show_add_name).pack(pady=20)

    def show_grade_input(self, name):
        self.clear()
        tk.Label(self.container, text="Subject (Text Only):").pack()
        s_e = tk.Entry(self.container)
        s_e.pack()
        tk.Label(self.container, text="Grade (0-100):").pack()
        g_e = tk.Entry(self.container)
        g_e.pack()

        def save():
            sub, grd = s_e.get(), g_e.get()
            if not sub.isalpha(): return messagebox.showerror("Error", "Letters only for subject.")
            try:
                val = float(grd)
                if 0 <= val <= 100:
                    file_handler.update_student_data(name, "grade", {"subject": sub, "score": val})
                    messagebox.showinfo("Success", "Grade Added")
                    self.show_student_options(name)
                else: raise ValueError
            except: messagebox.showerror("Error", "Enter a number 0-100.")

        tk.Button(self.container, text="Enter", width=13, height=2, command=save).pack(pady=10)
        tk.Button(self.container, text="Back", bg=self.blue_bg, fg=self.white_fg, width=13, height=2, command=lambda: self.show_student_options(name)).pack()

    def show_att_input(self, name):
        self.clear()
        tk.Label(self.container, text="Attendance Selection").pack(pady=10)
        s = tk.Scale(self.container, from_=0, to=100, orient="horizontal", length=300)
        s.pack()
        def save():
            file_handler.update_student_data(name, "attendance", s.get())
            messagebox.showinfo("Success", "Attendance Updated")
            self.show_student_options(name)
        tk.Button(self.container, text="Enter", width=13, height=2, command=save).pack(pady=10)
        tk.Button(self.container, text="Back", bg=self.blue_bg, fg=self.white_fg, width=13, height=2, command=lambda: self.show_student_options(name)).pack()

    def show_view_students(self):
        self.clear()
        data = file_handler.load_records()
        sorted_names = logic.bubble_sort_students(data)
        
        tk.Label(self.container, text="Full Student Records", font=("Arial", 16, "bold")).pack(pady=10)

        # 1. Create a container for the Canvas and Scrollbar
        scroll_container = tk.Frame(self.container)
        scroll_container.pack(fill="both", expand=True, padx=10)

        # 2. Create the Canvas and Scrollbar
        canvas = tk.Canvas(scroll_container)
        scrollbar = tk.Scrollbar(scroll_container, orient="vertical", command=canvas.yview)
        
        # 3. Create the frame that will actually hold the student labels
        scrollable_frame = tk.Frame(canvas)

        # 4. Configure the canvas to update the scroll area whenever the frame size changes
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        # 5. Place the frame inside the canvas window
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Pack the canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # 6. Populate the scrollable_frame with student data
        grade_thresh = self.thresholds.get('grade', 40)
        att_thresh = self.thresholds.get('attendance', 80)

        for name in sorted_names:
            student = data[name]
            avg = logic.calculate_average(student['grades'])
            att = student.get('attendance', 0)
            
            # Formatting logic for "At-Risk" students
            header_text = f"Student: {name.upper()} | Avg: {avg:.1f}% | Att: {att}%"
            color = "red" if avg < grade_thresh or att < att_thresh else "black"
            
            tk.Label(scrollable_frame, text=header_text, font=("Arial", 11, "bold"), fg=color).pack(anchor="w", pady=(10, 0))
            
            if student['grades']:
                details = []
                for g in student['grades']:
                    if isinstance(g, dict):
                        details.append(f"{g['subject']}: {g['score']}")
                    else:
                        details.append(f"Grade: {g}")
                
                tk.Label(scrollable_frame, text=f"   Details: {', '.join(details)}", font=("Arial", 9), fg="gray").pack(anchor="w")

        # Control Buttons at the bottom
        bottom_frame = tk.Frame(self.container)
        bottom_frame.pack(pady=10)

        tk.Button(bottom_frame, text="Show Attendance Chart", width=20, 
                  command=lambda: visual.generate_attendance_chart(data, att_thresh)).pack(side="left", padx=5)
        
        tk.Button(bottom_frame, text="Back", bg=self.blue_bg, fg=self.white_fg, 
                  width=10, font=("Arial", 10, "bold"), command=self.show_main_menu).pack(side="left", padx=5)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = TrackerApp(root)
    root.mainloop()
