def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
        return None

# Example usage
filename = "example.txt"
file_content = read_file(filename)
if file_content is not None:
    print(file_content)
