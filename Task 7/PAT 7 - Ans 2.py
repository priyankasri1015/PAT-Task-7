def read_and_display_file(file_name):
    try:
        # Open the file for reading
        with open(file_name, 'r') as file:
            # Read and display the content
            file_content = file.read()
            print("File Content:")
            print(file_content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
file_to_read = "timestamp_file_2023-12-16_14-30-00.txt"  # Replace with the actual file name
read_and_display_file(file_to_read)