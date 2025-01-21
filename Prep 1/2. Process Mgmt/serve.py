import os

# systemctl list-units --type=service

def start_service(service_name):
    os.system(f"sudo systemctl start {service_name}")

def stop_service(service_name):
    os.system(f"sudo systemctl stop {service_name}")
    
def restart_service(service_name):
    os.system(f"sudo systemctl restart {service_name}")
    
def status_service(service_name):
    os.system(f"sudo systemctl status {service_name}")
    
def enable_service(service_name):
    os.system(f"sudo systemctl enable {service_name}")
    
def disable_service(service_name):
    os.system(f"sudo systemctl disable {service_name}")

if __name__ == "__main__":
    service_name = input("Enter the service name: ")
    action = input("Enter the action (start/stop/restart/status/enable/disable): ")
    if action == "start":
        start_service(service_name)
    elif action == "stop":
        stop_service(service_name)
    elif action == "restart":
        restart_service(service_name)
    elif action == "status":
        status_service(service_name)
    elif action == "enable":
        enable_service(service_name)
    elif action == "disable":
        disable_service(service_name)
    else:
        print("Invalid action")
    os.system("systemctl list-units --type=service")