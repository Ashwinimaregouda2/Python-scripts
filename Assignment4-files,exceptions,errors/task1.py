try:
    # Open the file in read mode
    with open('sample.txt', 'r') as file:
        # Read and print the content line by line
        for line in file:
            print(line.strip())  # Using strip() to remove extra whitespace or newline characters
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist. Please ensure the file is in the correct directory.")
