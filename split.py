import os

# Ask user to input file name
input_file = input("Enter input file name: ")

# Set the delimiter
delimiter = input("Enter delimiter: ")

# Open the input file
with open(input_file, "r") as f:
    # Initialize the title and output file variables
    title = ""
    output_file = None
    # Loop through each line in the input file
    for line in f:
        # Check if the line starts with the delimiter
        if line.startswith(delimiter):
            # Get the title without the delimiter and whitespace
            title = line[len(delimiter):].strip()
            # Create the output file name
            output_file = title + ".txt"
            # Open the output file
            with open(output_file, "w") as out:
                pass  # Create empty file
            # Print the file name of the output file
            print(f"Created file: {output_file}")
        elif output_file is not None:
            # Write the line to the output file
            with open(output_file, "a") as out:
                out.write(line)

# Remove delimiter lines from the output files
for output_file in os.listdir():
    if output_file.endswith(".txt"):
        with open(output_file, "r+") as out:
            lines = out.readlines()
            out.seek(0, 0)
            out.truncate()
            for line in lines:
                if not line.startswith(delimiter):
                    out.write(line)

