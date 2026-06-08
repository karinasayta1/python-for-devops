
import psutil

def get_metrics():
    cpu=psutil.cpu_percent(interval=1)
    memory=psutil.virtual_memory().percent
    disk=psutil.disk_usage('/').percent
    return {
        "CPU Usage": f"{cpu}%",
        "Memory Usage": f"{memory}%",
        "Disk Usage": f"{disk}%"
    }