import json #one of the required libraries for handling JSON data in the file handler component, already preinstalled in Python. Allows for easy reading and writing of student records and configuration settings in JSON format. 
import os #also a standard library in Python, used for file path operations and checking if files exist. This is essential for the file handler to manage student records and configuration files effectively.

DATA_FILE = "students.json" #Defines the filename for storing student records. This file will contain a JSON representation of the student data, including their grades and attendance. The file handler will read from and write to this file to persist student information across sessions.
CONFIG_FILE = "config.json"#Defines the filename for storing configuration settings, such as grade and attendance thresholds. This allows the application to remember user-defined settings even after it is closed and reopened. The file handler will manage this file to ensure that threshold settings are saved and loaded correctly.

# Using the json config, it allows for the application to persist user-defined thresholds for grades and attendance across sessions. 
# This means that if a user sets specific thresholds for what constitutes passing grades or acceptable attendance, those settings will be saved in the config.json file. 
# When the application is restarted, it can read these settings from the file and apply them, ensuring a consistent user experience without requiring the user to reconfigure their preferences each time they use the application.
def load_records():
#Loads up a previously saved file, if not found, returns nothing. This function checks if the DATA_FILE exists, and if it does, it attempts to read and parse the JSON data from the file. If the file does not exist or if there is an error in decoding the JSON (such as if the file is empty or contains invalid JSON), it returns an empty dictionary. This ensures that the application can handle cases where there are no existing records gracefully, without crashing or throwing an error.
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f) #coursety of Robbins (2022), who provided a helpful example of how to implement JSON file handling in Python, which I adapted for my student records management. 
            #The json.load() function reads the JSON data from the file and converts it into a Python dictionary, which can then be used by the application to manage student records.
    except (json.JSONDecodeError, FileNotFoundError): #error handling. use of a json.JSONDecodeError to catch cases where the file exists but contains invalid JSON, and FileNotFoundError to catch cases where the file does not exist. In either case, it returns an empty dictionary, allowing the application to continue functioning without crashing due to missing or malformed data.
        return {}

def save_records(records): #function, takes a dictionary of student records as input and saves it to the DATA_FILE in JSON format. 
    #The json.dump() function is used to write the dictionary to the file, with an indentation of 4 spaces for better readability. 
    # This allows the application to persist student data across sessions, ensuring that any changes made to the records are saved and can be accessed the next time the application is run.
    """Saves student dictionary to JSON."""
    with open(DATA_FILE, 'w') as f:#opens the DATA_FILE in write mode, which will create the file if it does not exist or overwrite it if it does. The function then uses json.dump() to write the records dictionary to the file in JSON format, with an indentation of 4 spaces for better readability. This ensures that the student records are saved persistently and can be easily read and modified in future sessions.
        json.dump(records, f, indent=4) #(W3schools, n.d.)

def load_thresholds(): #standard function to load threshold settings from the CONFIG_FILE. If the file does not exist, it returns default threshold values for grades and attendance. This allows the application to have predefined thresholds while also enabling users to customize them as needed. The function checks for the existence of the CONFIG_FILE, and if it exists, it reads and parses the JSON data to retrieve the threshold settings. If the file is missing or cannot be read, it falls back to default values, ensuring that the application can still function with reasonable defaults.
    """Persists threshold settings across sessions."""
    if not os.path.exists(CONFIG_FILE):
        return {"grade": 40.0, "attendance": 80.0}
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)
#the point of the config file is to allow the application to remember user-defined settings for grade and attendance thresholds, ensuring a consistent experience across sessions. By loading these settings from the CONFIG_FILE, the application can apply the user's preferences each time it is run, without requiring them to reconfigure their thresholds every time they use the application.

def save_thresholds(thresholds): #when in the progam, the user updates the grade or attendance thresholds, this function is called to save those new settings to the CONFIG_FILE. It takes a dictionary of threshold values as input and writes it to the file in JSON format. This ensures that any changes made by the user to the thresholds are persisted and will be applied the next time the application is run, providing a seamless and personalized user experience.
    with open(CONFIG_FILE, 'w') as f:
        json.dump(thresholds, f, indent=4)

def update_student_data(name, data_type, new_data):
    """Updates specific student attributes."""
    records = load_records() #This function is designed to update specific attributes of a student's record, such as their grades or attendance. It first loads the existing student records using the load_records() function. Then, it checks if the specified student name exists in the records. If the student does not exist, it initializes a new record for that student with an empty list of grades and a default attendance of 100%. Depending on the data_type parameter, it either appends a new grade to the student's grades list or updates their attendance percentage. Finally, it saves the updated records back to the file using the save_records() function, ensuring that all changes are persisted.
    if name not in records:
        records[name] = {"grades": [], "attendance": 100} #If the student name does not exist in the records, it creates a new entry for that student with an empty list of grades and a default attendance of 100%. This allows the application to handle new students seamlessly, ensuring that they can be added to the records without any issues.
    
    if data_type == "grade":
        records[name]["grades"].append(new_data) #If the data_type is "grade", it appends the new grade to the student's existing list of grades. This allows the application to keep track of all grades for each student, enabling features like calculating averages and displaying grade histories.
    elif data_type == "attendance":
        records[name]["attendance"] = new_data #If the data_type is "attendance", it updates the student's attendance percentage with the new value provided. This allows the application to maintain accurate attendance records for each student, which can be used for generating reports and visualizations.
        
    save_records(records) #After updating the student's record with the new grade or attendance information, it calls the save_records() function to write the updated records back to the DATA_FILE. This ensures that all changes made to the student data are persisted and will be available the next time the application is run.
