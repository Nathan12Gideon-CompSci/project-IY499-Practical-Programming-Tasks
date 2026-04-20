# Practical Programming Assignment - Student Attendence And Grade Tracker 

**Name : Nathan Gideon**

**Student ID : 303066116**

**Exam ID : Y3963473**

**Module Code :**  *Y2025-019055[IPC00014C-T1-2-A] IYO: Introduction to Programming (AT1) Sep 2025* 

**Teacher Name :** ***Dena Sarhang Yehuda Nuuman***

### I confirm that this assignment is my own work. Where I have referred to online sources, I have provided comments detailing the reference and included a link to the source.

The **Student Attendance And Grade Tracker** is a modular Python program designed to streamline the management of academic records and attendance monitoring. The program offers a simple design using the python GUI and the use of user heuristics.

The application follows a strict line of modular programming across four main modules: Gui.py (User Interface), Logic.py (Calculations and Algorithms), File_Handler.py (Persistent Storage), and Visual.py (Data Visualization).  In this format, the program achieves a login system to protect sensitive student data. User-defined benchmarks for grades and attendance that persist across sessions via JSON configuration which can support complex, nested data structures where students can have multiple subject-specific grades. This in turn allows a view that utilizes a custom Bubble Sort algorithm to organize students and automatically highlights "at-risk" individuals in red based on current thresholds. At which the use of Matplotlib to generate professional-grade attendance charts for class-wide analysis.


###Libraries and Packages Used:

tkinter
matplotlib
json
OS
contourpy
cycler
fonttools
kiwisolver
matplotlib
numpy
packaging
pillow
pyparsing
python-dateutil
six

###Installation Process

1. Ensure that the program that you are running python is on version 3.14 (64 bit) for Windows 11. 

2. From the .zip folder, download all four .py files, two .json files and the requirement.txt, they must remain in the same folder, do not change anything yet.

3. Once you have downloaded all requirements, open Gui.py, do not start or activate any function. Go to the terminal in your system, and then carefully enter this code:

 pip install -r requirement.txt

This will enter all needed packages and install them, this will take some time to download.


4. ONLY TO CHECK: Go back to the terminal, and insert the code:
 
 pip freeze > check.txt

This should write a check.txt file, which must match the requirement.txt content. 

###Running the Application:

Firstly, The Gui.py file is the important file here, open the file in the code editor.

Secondly, run the Gui file in the selected code editor; this will open a login page. 

Username : admin

Password : york2026

Note: you can adjust the thresholds of the program, and when viewing students, any student marked in red is “at-risk”. 




