import os # Importing the os module to interact with the operating system

def list_files_in_folder(folder_path): # Function to list files in a given folder
    try: # Attempt to list files 
        files = os.listdir(folder_path) # List all files in the specified folder
        return files, None # Return the list of files and None for error message
    except FileNotFoundError: # Handle the case where the folder does not exist
        return None, "Folder not found" # Return None for files and an error message
    except PermissionError: # Handle the case where permission is denied
        return None, "Permission denied" # Return None for files and an error message

def main(): # Main function to execute the script
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split() # Get user input and split into a list of folder paths
    
    for folder_path in folder_paths: # Iterate over each folder path
        files, error_message = list_files_in_folder(folder_path) # Call the function to list files
        if files: # If files are found
            print(f"Files in {folder_path}:") # Print the folder path
            for file in files: # Iterate over each file
                print(file) # Print the file name
        else: # If there was an error
            print(f"Error in {folder_path}: {error_message}") # Print the error message

if __name__ == "__main__": # Check if the script is being run directly
    main() # Call the main function to execute the script.