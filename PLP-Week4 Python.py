import sys

def process_file_with_error_handling():
    """
    Reads content from a user-specified file, modifies it, and
    writes the new content to a separate output file.
    Includes error handling for missing or unreadable files.
    """
    output_filename = 'modified_output.txt'

    # Get the input filename from the user
    input_filename = input("Please enter the name of the file you want to process: ")

    try:
        # It automatically closes the file, even if errors occur.
        with open(input_filename, 'r') as infile:
            print(f"Reading content from '{input_filename}'...")
            
            # Read the entire content of the file
            content = infile.read()
            
            # Perform a simple modification: convert all text to uppercase
            modified_content = content.upper()

        # Open a new file to write the modified content
        with open(output_filename, 'w') as outfile:
            print(f"Writing modified content to '{output_filename}'...")
            
            # Write the modified string to the new file
            outfile.write(modified_content)

        print("\nSuccess! The file has been processed and saved.")

    except FileNotFoundError:
        # This block runs if the specified input file does not exist.
        print(f"\nError: The file '{input_filename}' was not found.", file=sys.stderr)
        print("Please check the filename and try again.", file=sys.stderr)
   

# Call the main function to run the program
process_file_with_error_handling()
