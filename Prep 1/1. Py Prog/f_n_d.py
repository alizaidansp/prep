import os
import shutil

def archive_logs(log_dir, archive_dir):
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    for file_name in os.listdir(log_dir):
        if file_name.endswith(".log"):
            full_path = os.path.join(log_dir, file_name)
            shutil.move(full_path, os.path.join(archive_dir, file_name))
            print(f"Archived: {file_name}")

if __name__ == "__main__":
    log_directory = "./logs"
    archive_directory = "./archive"
    archive_logs(log_directory, archive_directory)
