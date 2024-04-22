import logging
import time
import random

# Configure logging to log messages to the console
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to generate and log messages at different levels
def generate_log_messages():
    try:
        while True:
            # Randomly select a log level
            log_level = random.choice([logging.INFO, logging.DEBUG, logging.ERROR])
            # Log the message
            if log_level == logging.INFO:
                logging.info("This is an INFO message")
            elif log_level == logging.DEBUG:
                logging.debug("This is a DEBUG message")
            elif log_level == logging.ERROR:
                logging.error("This is an ERROR message")

            # Sleep for a short interval
            time.sleep(1)
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        print("\nLogging interrupted. Exiting.")

# Main function
def main():
    print("Starting log monitoring and message generation...")
    generate_log_messages()

if __name__ == "__main__":
    main()

