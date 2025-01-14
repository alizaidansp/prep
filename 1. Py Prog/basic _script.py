# a basic python script to  list all directories in the home directory
import os

# getting directory from user
home_dir = input("Enter the home directory: ")

# getting all directories in the home directory
directories = os.listdir(home_dir)
file_count=0
if len(directories) == 0:
    print("No directories found")
else:
    print("Directories in the home directory:")
    for directory in directories:
        if os.path.isdir(os.path.join(home_dir, directory)==False ):
            file_count+=1
    print(f"{file_count} files found")
