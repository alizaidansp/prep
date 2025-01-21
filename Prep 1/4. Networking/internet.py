
# a script to check internet connectivity status
import os
import time
import requests

def check_internet():
        try:
            response = requests.get('https://google.com')
            if response.status_code == 200:
                print("Internet is connected")
            else:
                print("Internet is not connected")
        except Exception as e:
            print(f"Error: {e}")
            
check_internet()
