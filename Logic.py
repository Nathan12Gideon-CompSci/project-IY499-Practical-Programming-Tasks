
#this code is for a student management system that includes functions to calculate average grades, identify at-risk students based on their grades and attendance, and sort students by their names using a simple Bubble Sort algorithm. The code demonstrates the use of functions, loops, conditionals, and data structures to manage student information effectively.

def calculate_average(grades): #we define a function to calculate the average grade for a student. 
    #It takes a list of grades as input and returns the average.
    if not grades:
        return 0 # If there are no grades, it returns 0 to avoid division by zero errors.
    return sum(grades) / len(grades)

def identify_at_risk(students, grade_threshold=40, attendance_threshold=80): #This function identifies students who are at risk of failing based on their average grades and attendance.
    #students is a list of dictionaries, where each dictionary contains information about a student, including their grades and attendance. 
     
    at_risk = [] # we initialize an empty list to store the at-risk students.

    for student in students: #by looping through the list of students, we calculate the average grade for each student using the calculate_average function.
        avg_grade = calculate_average(student['grades']) 
        if avg_grade < grade_threshold or student['attendance'] < attendance_threshold: #for each student, check average grade and attendance against the specified thresholds. If either the average grade is below the grade_threshold or the attendance is below the attendance_threshold, we consider the student at risk.
            at_risk.append(student) #if conditions are met, we add the student to the at_risk list.
    return at_risk

def sort_students_by_name(students): #This function sorts the list of students by their names using a simple Bubble Sort algorithm.

    n = len(students)#we get the number of students in the list to determine how many iterations are needed for the sorting process.

    for i in range(n): #we use a nested loop to compare each student's name with the next student's name. 
        #The outer loop runs n times, while the inner loop runs n - i - 1 times to avoid comparing already sorted elements.

        for j in range(0, n - i - 1): 

            if students[j]['name'].lower() > students[j+1]['name'].lower(): #we compare the names of the students in a case-insensitive manner. 
                #If the name of the current student is greater than the name of the next student, we swap their positions in the list.

                students[j], students[j+1] = students[j+1], students[j] #we perform the swap by assigning the next student to the current position and the current student to the next position.
    return students