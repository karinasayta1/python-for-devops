class LogAnalyzer:
    def __init__(self, file_name):
        self.file_name = file_name
        self.counts= {"INFO":0, "WARNING":0, "ERROR":0}

    def read_file(self):
        try:
            with open(self.file_name, "r") as file:
                return file.readlines()
        except Exception as e:
            print(f"Error opening file: {e}")
            return []

    def analyze_logs(self,lines):
        for line in lines:
            if "INFO" in line:
                self.counts["INFO"] += 1
            elif "WARNING" in line:
                self.counts["WARNING"] += 1
            elif "ERROR" in line:
                self.counts["ERROR"] += 1
    
    
def main():
    f_name=input("Enter log file name: ")
    analyzer= LogAnalyzer(f_name)
    lines=analyzer.read_file()
    if not lines:
        print("The log file is empty.")
        return
    analyzer.analyze_logs(lines)
    print(f"Total INFO : {analyzer.counts['INFO']}\nTotal WARNINGS : {analyzer.counts['WARNING']}\nTotal ERRORS : {analyzer.counts['ERROR']}")

if __name__ == "__main__":
    main()
    