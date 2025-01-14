import boto3
import psutil
import time

# Initialize CloudWatch client
cloudwatch = boto3.client('cloudwatch')

def send_metrics_to_cloudwatch(cpu_usage, memory_usage, disk_usage):
    cloudwatch.put_metric_data(
        Namespace='MySystemMetrics',
        MetricData=[
            {
                'MetricName': 'CPUUsage',
                'Value': cpu_usage,
                'Unit': 'Percent'
            },
            {
                'MetricName': 'MemoryUsage',
                'Value': memory_usage,
                'Unit': 'Percent'
            },
            {
                'MetricName': 'DiskUsage',
                'Value': disk_usage,
                'Unit': 'Percent'
            }
        ]
    )

# Continuously monitor and send metrics to CloudWatch
while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    send_metrics_to_cloudwatch(cpu, memory, disk)
    time.sleep(60)  # Send data every 60 seconds
