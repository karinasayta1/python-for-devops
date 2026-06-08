#fun open file and read from file
#identify info,warning,error messages and count them
#print the summary and write it to a file
import json
count = {"INFO":0, "WARNING":0, "ERROR":0}

def open_file(file_name):
    try:
        with open(file_name, 'r') as file:
            if file.readlines() == []:
                print("The log file is empty.")
                exit()
            else:
                file.seek(0)  
                return file.readlines()
    except Exception as e:
        print(f"Error opening file: {e}")
        exit()
        return []

def analyze_logs(file_data):
    global count
    for line in file_data:
        if str.find(line, "INFO") != -1:
            count["INFO"] += 1
        elif str.find(line, "WARNING") != -1:
            count["WARNING"] += 1
        elif str.find(line, "ERROR") != -1:
            count["ERROR"] += 1

def wrtie_output():
    try:
        with open("log_summary.json","w") as f:
            json.dump(count,f,indent=2)
    except Exception as e:
        print(f"Error writing to file: {e}")

f_name=input("Enter log file name: ")
file_data=open_file(f_name)
analyze_logs(file_data)
print(f"Total INFO : {count['INFO']}\nTotal WARNINGS : {count['WARNING']}\nTotal ERRORS : {count['ERROR']}")
wrtie_output()

