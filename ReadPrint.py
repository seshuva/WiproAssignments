def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())  # .strip() removes any leading/trailing whitespace
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file_path = 'example.txt'
read_file(file_path)
