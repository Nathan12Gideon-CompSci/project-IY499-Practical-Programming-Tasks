import matplotlib.pyplot as plt #one of the required libraries for generating visualizations in the visual component

def generate_attendance_chart(student_dict, threshold):
    #Generates bar chart for current class attendance.
    if not student_dict: #If the student_dict is empty, it means there are no student records to display, 
        return
    
    names = list(student_dict.keys())
    # The following line uses a list comprehension to extract the attendance values for each student from the student_dict. It iterates 
    values = [data['attendance'] for data in student_dict.values()]
     # through the values of the student_dict (which are the individual student records) and retrieves the 'attendance' value for each student, creating a list of attendance percentages that corresponds to the list of student names.  
    plt.figure(figsize=(10, 6))
#setting the size of the chart
    plt.bar(names, values, color='#005eb8') #value of the bars in the chart, with a specific color for visual appeal. 

    plt.axhline(y=threshold, color='r', linestyle='--', label=f'Threshold ({threshold}%)')
# This line adds a horizontal dashed red line to the bar chart at the y-value corresponding to the attendance threshold. 
    plt.xlabel('Student Name')

    plt.ylabel('Attendance %')

    plt.title('Attendance Overview')

    plt.legend()

    plt.show()
