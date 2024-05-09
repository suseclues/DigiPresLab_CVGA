import os
import shutil

def write_copied_folders(filename, folder_name):
    """Writes the list of copied folders to a text file"""
    with open(filename, 'a+') as fileout:
        fileout.write(folder_name + '\n')

def copy_folders(source_directory, destination_directory, batch_size, copied_txt_file):
    folder_names = [f.name for f in os.scandir(source_directory) if f.is_dir()]
    total_folders = len(folder_names)
    folders_copied = 0

    while folders_copied < total_folders:
        batch_count = folders_copied // batch_size + 1
        batch = folder_names[folders_copied : folders_copied + batch_size]
        batch_dir = os.path.join(destination_directory, f"Batch{batch_count}")

        os.makedirs(batch_dir, exist_ok=True)
        for folder_name in batch:
            try:
                shutil.copytree(os.path.join(source_directory, folder_name), os.path.join(batch_dir, folder_name))
                write_copied_folders(copied_txt_file, folder_name)
                folders_copied += 1
            except Exception as e:
                print(f"Error occurred copying {folder_name}: {e}")

    print(f"All {total_folders} folders copied, sent to {destination_directory}")

if __name__ == "__main__":
    try:
        source_directory = "E:\\Bagged"
        destination_directory = "P:\\path\\to\\CVGA\\Autotransfer"
        batch_size = 30
        copied_txt_file = "C:\\path\\to\\txt\\file"

        copy_folders(source_directory, destination_directory, batch_size, copied_txt_file)
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
