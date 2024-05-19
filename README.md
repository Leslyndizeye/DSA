# Integer Processing Utility

This Python utility script `process_file.py` is designed to read a file containing integers, process them, and write the unique integers within a certain range to an output file.

## Functionality

The main function `process_file(input_file_path, output_file_path)` performs the following tasks:

1. Reads integers from an input file located at `input_file_path`.
2. Filters out non-integer lines and integers outside the range [-1023, 1023].
3. Writes the unique integers within the range to an output file located at `output_file_path`.
4. Prints a confirmation message upon successful completion.
5. Returns a sorted list of the unique integers.

## Usage

from process_file import process_file

# Example usage
sorted_integers = process_file("small_sample_input_02.txt_result.txt", "small_sample_input_02.txt")
print("Sorted integers:", sorted_integers)

Replace `"small_sample_input_02.txt_result.txt"` and `"small_sample_input_02.txt"` with the actual file paths you want to use.

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to modify it according to your specific project details and preferences!