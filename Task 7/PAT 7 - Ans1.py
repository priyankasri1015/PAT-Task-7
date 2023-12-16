import datetime

def create_file_with_timestamp():
    # Get the current timestamp
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create a text file with the current timestamp
    file_name = f"timestamp_file_{current_timestamp}.txt"

    # Write the timestamp content to the file
    with open(file_name, 'w') as file:
        file.write(f"File created at: {current_timestamp}")

    return file_name

# Example usage:
created_file = create_file_with_timestamp()
print(f"File '{created_file}' has been created with the current timestamp.")
