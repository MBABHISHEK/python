import zipfile
import os

def zip_folder(folder_name):
    # Generate a unique name for the ZIP file based on the folder name
    zip_filename = folder_name + ".zip"
    
    try:
        # Create a ZIP archive
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Iterate through all files in the folder and add them to the ZIP archive
            for folder, subfolders, files in os.walk(folder_name):
                for file in files:
                    file_path = os.path.join(folder, file)
                    zipf.write(file_path, os.path.relpath(file_path, folder_name))

        print(f"Successfully created the ZIP file '{zip_filename}' containing the folder '{folder_name}'.")
    except FileNotFoundError:
        print("Folder not found. Please enter a valid folder name.")
folder_name = input("Enter the name of the folder to zip: ")
zip_folder(folder_name)