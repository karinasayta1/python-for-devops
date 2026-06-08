import argparse
import json

def take_inputs():
    analyzer = argparse.ArgumentParser(prog="log_analyzer_cli",description="Analyze log files and generate a report.",
                                       usage="python log_analyzer_cli.py <log_file> [--out <output_file>]")
    analyzer.add_argument("file",help="Path to the log file to be analyzed.(Required)")
    analyzer.add_argument("--out", help="Path to save the analysis report.")
    args =analyzer.parse_args()
    return args

def analyze_logs(args):
    log_file= args.file
    counts={"ERROR": 0, "WARNING": 0, "INFO": 0}
    try:
        with open(log_file,"r") as f:
            lines=f.readlines()
            if not lines:
                print("The log file is empty.")
                exit()
            for lines in lines:
                if "ERROR" in lines:
                    counts["ERROR"] += 1
                elif "WARNING" in lines:
                    counts["WARNING"] += 1
                elif "INFO" in lines:
                    counts["INFO"] += 1
    except FileNotFoundError:
        print(f"Log file '{log_file}' not found.")
    return counts
    
def main():
    args = take_inputs()
    counts = analyze_logs(args)
    print(f"Log Analysis Report:\nErrors: {counts['ERROR']}\nWarnings: {counts['WARNING']}\nInfo: {counts['INFO']}")
    if args.out:
        try:
            with open(args.out,"w") as f:
                json.dump(counts,f,indent=2)
        except Exception as e:
            print(f"Error writing to file: {e}")

if __name__ == "__main__":
    main()