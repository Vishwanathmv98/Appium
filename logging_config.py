import logging
import os

# Ensure the log directory exists
log_directory = 'logger'
os.makedirs(log_directory, exist_ok=True)

# Define the log file path
log_file_path = os.path.join(log_directory, 'app.log')

# Configure the logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Adjust the level as needed

# Create a file handler that logs debug and higher level messages
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.DEBUG)  # Adjust the level as needed

# Create a console handler for live output (optional)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Adjust the level as needed

# Create a formatter and set it for the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Example usage
if __name__ == "__main__":
    logger.info("Logging setup complete.")
