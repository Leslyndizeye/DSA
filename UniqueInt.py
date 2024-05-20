def process_file(input_file, output_file):
    # Read integers from input file
    with open(input_file, 'r') as file:
        integers = [int(line.strip()) for line in file]

    # Find unique integers
    unique_integers = list(set(integers))

    # Sort the unique integers
    sorted_integers = sorted(unique_integers)

    # Print the list of sorted unique integers
    print(sorted_integers)

    # Write the sorted unique integers to the output file
    with open(output_file, 'w') as file:
        for integer in sorted_integers:
            file.write(str(integer) + '\n')

# Example usage
process_file("sample_input_for_students/sample_input_for_students/sample_01.txt", "sample_input_for_students/sample_input_for_students/sample_01.txt_result.txt")
