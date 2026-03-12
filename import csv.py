import csv
import os
import tkinter as tk
from tkinter import filedialog, messagebox

class LearningRecommendationSystem:
    def __init__(self, filename="student_progress.csv"):
        self.filename = filename
        self.subjects = {}
        self.load_progress()
    
    def load_progress(self):
        """Load existing progress from file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    subject = row['Subject']
                    self.subjects[subject] = {
                        'mark': int(row['Mark']),
                        'status': row['Status']
                    }
    
    def validate_mark(self, mark):
        """Validate mark input (0-100)"""
        try:
            mark = int(mark)
            return 0 <= mark <= 100
        except ValueError:
            return False
    
    def add_subject(self, subject, mark):
        """Add or update subject marks"""
        if not self.validate_mark(mark):
            raise ValueError("Mark must be between 0 and 100")
        
        mark = int(mark)
        status = "Weak" if mark < 60 else "Average" if mark < 80 else "Strong"
        self.subjects[subject] = {'mark': mark, 'status': status}
    
    def get_weak_topics(self):
        """Return list of weak topics"""
        return [s for s, data in self.subjects.items() if data['status'] == 'Weak']
    
    def search_subject(self, subject):
        """Search for specific subject"""
        return self.subjects.get(subject.capitalize(), None)
    
    def get_sorted_subjects(self):
        """Sort subjects by marks (ascending)"""
        return sorted(self.subjects.items(), key=lambda x: x[1]['mark'])
    
    def save_progress(self):
        """Save progress to CSV file"""
        with open(self.filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Subject', 'Mark', 'Status'])
            writer.writeheader()
            for subject, data in self.subjects.items():
                writer.writerow({
                    'Subject': subject,
                    'Mark': data['mark'],
                    'Status': data['status']
                })
    
    def get_recommendations(self):
        """Generate revision recommendations"""
        weak = self.get_weak_topics()
        if weak:
            return f"Focus on: {', '.join(weak)}"
        return "Good job! Keep practicing."


# GUI Setup
def main_gui():
    root = tk.Tk()
    root.title("Smart Learning Recommendation System")
    system = LearningRecommendationSystem()
    
    def add_mark():
        subject = subject_entry.get().strip()
        mark = mark_entry.get().strip()
        
        if not subject or not mark:
            messagebox.showerror("Error", "Please fill all fields")
            return
        
        try:
            system.add_subject(subject, mark)
            system.save_progress()
            messagebox.showinfo("Success", f"Added {subject}: {mark}")
            subject_entry.delete(0, tk.END)
            mark_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def show_recommendations():
        recommendations = system.get_recommendations()
        messagebox.showinfo("Recommendations", recommendations)
    
    def search_subject_gui():
        subject = subject_entry.get().strip()
        result = system.search_subject(subject)
        if result:
            messagebox.showinfo("Search Result", f"{subject}: {result['mark']} ({result['status']})")
        else:
            messagebox.showwarning("Not Found", "Subject not found")
    
    tk.Label(root, text="Subject:").pack()
    subject_entry = tk.Entry(root)
    subject_entry.pack()
    
    tk.Label(root, text="Mark (0-100):").pack()
    mark_entry = tk.Entry(root)
    mark_entry.pack()
    
    tk.Button(root, text="Add Mark", command=add_mark).pack()
    tk.Button(root, text="Get Recommendations", command=show_recommendations).pack()
    tk.Button(root, text="Search Subject", command=search_subject_gui).pack()
    
    root.mainloop()


if __name__ == "__main__":
    main_gui()