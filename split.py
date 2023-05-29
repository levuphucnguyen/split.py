import os
from collections import defaultdict
import unicodedata

def process_file(input_file, delimiter):
    output_files = defaultdict(list)

    with open(input_file, "r", encoding='utf-8') as f:
        current_output_file = None
        for line in f:
            if line.startswith(delimiter):
                title = line[len(delimiter):].strip()
                current_output_file = title + ".txt"
                output_files[current_output_file] = []
            elif current_output_file:
                output_files[current_output_file].append(line.strip())

    for output_file, content in output_files.items():
        with open(output_file, "w", encoding='utf-8') as out:
            final_content = "\n".join(unicodedata.normalize('NFD', line.strip()) for line in content)
            out.write(final_content)

    print("Press any key to continue...")
    input("")

input_file = input("Enter input file name: ")
delimiter = input("Enter delimiter: ")

process_file(input_file, delimiter)
