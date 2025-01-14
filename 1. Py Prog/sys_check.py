import os
import psutil
from datetime import datetime

def check_sys():
    print("Checking system...")
    print("CPU Count: ", psutil.cpu_count())
    print("Memory: ", psutil.virtual_memory().percent)
    print("Disk: ", psutil.disk_usage("/").percent)
    print("Users: ", psutil.users())
    print("System Uptime: ", datetime.fromtimestamp(psutil.boot_time()))
    print(f"Current User: {os.getlogin()}")


check_sys()