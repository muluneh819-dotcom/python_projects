import os
import shutil
path = r'C:\Users\Rinatoh\Desktop\intro-to-python-2025-muluneh23'
directories = {
    '.jpg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.pdf': 'Documents',
    '.txt': 'Documents',
    '.py':  'Python Scripts',
    '.md':  'Documents'
}
list_of_files = os.listdir(path)
print(f"Scanning: {list_of_files}")

for filename in list_of_files:
    name, extension = os.path.splitext(filename)
    if extension == "":
        continue
    folder_name = directories.get(extension, "Others")

    new_folder_path = os.path.join(path, folder_name)
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
    source_path = os.path.join(path, filename)
    destination_path = os.path.join(new_folder_path, filename)
    try:
        shutil.move(source_path, destination_path)
        print(f"Moved {filename} -> {folder_name}")
    except Exception as e:
        print(f"Skipped {filename}: An error occurred ({e})")  
