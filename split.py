import os
import concurrent.futures
from collections import defaultdict
import unicodedata
import re

def normalize_line(line):
    return unicodedata.normalize('NFD', re.sub(r'[\x00-\x1F\x7F-\x9F]', '', line))

def process_file(input_file, delimiter):
    if not os.path.isfile(input_file):
        print(f"File not found: {input_file}")
        return

    output_files = defaultdict(set)
    current_output_file = None

    def process_line(line):
        nonlocal current_output_file
        if line.startswith(delimiter):
            title = line[len(delimiter):].strip()
            current_output_file = title + ".txt"
            output_files[current_output_file].add(title)
        elif current_output_file:
            output_files[current_output_file].add(line.strip())

    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.readlines()
        content = [line.strip() for line in content]
        for line in content:
            process_line(line)

    for output_file, content in output_files.items():
        with open(output_file, "w", encoding='utf-8') as out:
            final_content = "\n".join(normalize_line(line) for line in content)
            out.write(final_content)

    return f"Processed {input_file}"

input_file_names = input("Enter input file names separated by space: ").split()
delimiter = input("Enter delimiter: ")

not_found_files = [file for file in input_file_names if not os.path.isfile(file)]
if not_found_files:
    print("The following input files were not found:")
    for file in not_found_files:
        print(file)
else:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(process_file, input_file_names, [delimiter] * len(input_file_names)))

    for result in results:
        print(result)

    print("Press any key to continue...")
    input("")