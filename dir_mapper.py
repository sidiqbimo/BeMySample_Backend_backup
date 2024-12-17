import os

def list_directories(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        print(f'Directory: {dirpath}')
        for dirname in dirnames:
            print(f'  Subdirectory: {os.path.join(dirpath, dirname)}')

# Replace '/path/to/your/folder' with the path to the folder you want to map
root_directory = 'c:/Users/sani2/Downloads/BeMySample_Backend/'
list_directories(root_directory)