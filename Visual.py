import matplotlib.pyplot as plt

def generate_attendance_chart(students):
    """Creates a bar chart showing attendance percentages."""
    names = [s['name'] for s in students]
    attendance = [s['attendance'] for s in students]

    plt.figure(figsize=(10, 6))
    plt.bar(names, attendance, color='skyblue')
    plt.axhline(y=80, color='r', linestyle='--', label='At-Risk Threshold')
    plt.xlabel('Student Name')
    plt.ylabel('Attendance (%)')
    plt.title('Class Attendance Overview')
    plt.legend()
    plt.show()