# from prometheus_client import start_http_server, Gauge
# import psutil
# import time

# # Define metrics to be collected
# cpu_usage = Gauge('cpu_usage', 'CPU usage in percentage')
# memory_usage = Gauge('memory_usage', 'Memory usage in percentage')
# disk_usage = Gauge('disk_usage', 'Disk usage in percentage')

# # Function to collect system data
# def collect_metrics():
#     cpu_usage.set(psutil.cpu_percent(interval=1))
#     memory_usage.set(psutil.virtual_memory().percent)
#     disk_usage.set(psutil.disk_usage('/').percent)

# # Start HTTP server for Prometheus to scrape
# start_http_server(8000)

# # Continuously collect and expose metrics
# while True:
#     collect_metrics()
#     time.sleep(10)  # Update every 10 seconds
    


from prometheus_client import Gauge, start_http_server
import psutil
# specify metrics to collect

from time import sleep
start_http_server(8000)
while True:
    memory_usage=Gauge("memory_usage", "Get Memory Information")
    v_m=psutil.virtual_memory()
    used_memory=v_m.total-v_m.used/100
    remaining_memory=100-used_memory
    memory_usage.set(used_memory )
    sleep(50)
