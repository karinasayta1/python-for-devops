#fun open file and read from file
#identify info,warning,error messages and count them
#print the summary and write it to a file
import json

def analyze_logs(file_data):
    count = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for line in file_data:
        if str.find(line, "INFO") != -1:
            count["INFO"] += 1
        elif str.find(line, "WARNING") != -1:
            count["WARNING"] += 1
        elif str.find(line, "ERROR") != -1:
            count["ERROR"] += 1
    return count
