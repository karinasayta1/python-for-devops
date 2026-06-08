What is the problem?
 - Problem is logs. 
 - In devops world logs are the first step towards debugging.
 - Diagonise issues using log patterns.
 - Analyzing logs automatically saves time and effort.

What input does it need?
 - It needs a log file to be analyzed.

What ouput should it give?
 - Identifies and counts the logs based on levels.
 - INFO, WARNING, ERROR it saves the count of each.
 
What steps are involved?
 - First I am going to use OOPS concept to make code more cleaner and structured.
 - Create member functions :
    - init to intialize member variables ()
    - read_file to read the file given by user
    - analyze_logs identifies and counts INFO, WRNING, ERROR
    - Prints a summary to the terminal