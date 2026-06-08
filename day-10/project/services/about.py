import psutil
import getpass
import datetime

def get_info():
    u_name =getpass.getuser()
    boot_time_timestamp = psutil.boot_time()
    boot_time = datetime.datetime.fromtimestamp(boot_time_timestamp)
    uptime = datetime.datetime.now() - boot_time
    
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            info = proc.info
            processes.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        
    dict_info={
        "Logged In User": u_name,
        "System Boot Time": boot_time.strftime("%Y-%m-%d %H:%M:%S"),
        "System Uptime": str(uptime).split('.')[0],
        "Processes": processes
    }
    return dict_info

#print(get_info())