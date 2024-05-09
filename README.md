# CVGA Ingest Script
This script automates the process of copying folders from one location to another in customizeable batches. It uses Python's built-in modules for file management.

## Usage
1. **Python Installation:** Ensure you have Python installed on your system (version 3.6 or higher).
2. **Package Installation:** Install the required package using pip install bagit.
3. **Configuration:** Customize the script variables *(source_directory, destination_directory, batch_size, copied_txt_file)* to match your file paths and preferences.
4. **Execution:** Run the script by entering python CVGA_INGEST.py in your command line interface.

## Script Overview
**write_copied_folders:** Records the names of copied folders in a text file.

**copy_folders:** Transfers folders from the source directory to the destination directory in batches.

**source_directory:** Path to the folder containing items to be copied.

**destination_directory:** Path to the folder where items will be copied.

**batch_size:** Number of items to copy in each batch.

**copied_txt_file:** Path to the text file for logging copied items.

## Notes
**Permissions:** Ensure that you have the necessary permissions to read from the source directory and write to the destination directory.

**Error Handling:** Handle any errors that may occur during the copying process to prevent interruptions.

# CVGA Bag Validator Script
This script checks the validity of BagIt bags in a specified directory and its subdirectories. It relies on Python's native modules and the bagit package for validation.

## Usage
1. **Python Installation:** Make sure Python is installed on your system (version 3.6 or higher).
2. **Package Installation:** Install the required package with pip install bagit.
3. **Configuration:** Adjust the bag_directory variable to point to your directory containing BagIt bags.
4. **Execution:** Run the script using python CVGA_bag_validator.py.

## Script Overview
**validate_bags_in_directory:** Validates BagIt bags within the specified directory and its subdirectories.

**Output:** Writes the names of failed bags to a file named validation_fails.txt.

**directory:** Path to the directory containing BagIt bags.

## Notes
**Package Dependency:** The script relies on the bagit package for bag validation. Install it using pip install bagit.

**BagIt Compliance:** Ensure that your BagIt bags adhere to the BagIt specifications for accurate validation results.

**Result Analysis:** Review the validation_fails.txt file after script execution to identify any bags that failed validation.
