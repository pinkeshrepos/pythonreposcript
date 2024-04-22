import time
import os

# Specify the log file to monitor
log_file = "/var/log/syslog"

# Function to continuously monitor the log file
def monitor_log():
    try:
        # Check if the log file exists
        if not os.path.exists(log_file):
            print(f"Error: Log file '{log_file}' not found.")
            return
        
        # Open the log file in read mode and continuously monitor for new entries
        with open(log_file, "r") as f:
            # Initialize a dictionary to store keyword counts
            keyword_counts = {}
            while True:
                # Read new lines from the log file
                new_lines = f.readlines()
                # Display new log entries and perform analysis
                for line in new_lines:
                    print(line.strip())
                    # Perform keyword analysis (count occurrences)
                    analyze_log_entry(line, keyword_counts)
                # Generate and display summary report
                generate_summary_report(keyword_counts)
                # Sleep for a short interval before checking for new entries again
                time.sleep(1)
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        print("\nMonitoring interrupted. Exiting.")

