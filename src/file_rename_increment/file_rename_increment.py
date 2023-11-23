import os


def file_rename_increment(folder_path):
    # Check if the given path is a dir
    if not os.path.isdir(folder_path):
        print("Error: The provided path is not a directory")
        return

    # Sort files by last modification time
    # To sort by creation time instead, use getctime
    files = sorted(
        os.listdir(folder_path),
        key=lambda f_name: os.path.getmtime(os.path.join(folder_path, f_name)),
    )

    for i, file_name in enumerate(files, start=1):
        # Get current file's file path
        file_path = os.path.join(folder_path, file_name)

        # Check if the current file is a file, if not the script will skip it
        if os.path.isfile(file_path):
            # Create a new file name
            new_file_name = f"Skärmbild ({i}).png"

            # Create the new file path
            new_file_path = os.path.join(folder_path, new_file_name)

            # Rename file
            os.rename(file_path, new_file_path)
            print(f'Renamed: "{file_path}"\nto: "{new_file_path}"')


# Path to the folder containing files to be renamed
folder_path = r""

file_rename_increment(folder_path)
