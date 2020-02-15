import psutil
import datetime

# CPU
def cpu_info():

    #cpu_times()
    print("CPU - information\n")
    print("cpu_times() - Return system CPU times as a named tuple. Every attribute represents the seconds the CPU has spent in the given mode. The attributes availability varies depending on the platform")
    print(psutil.cpu_times())

    #cpu_percent()
    print("\ncpu_percent() - Return a float representing the current system-wide CPU utilization as a percentage")
    print(f'CPU utilization - {psutil.cpu_percent(0.5)}%')

#Memory
def memory_info():

    #virtal_memory()
    print("\nMemory - information\n")
    print("virtal_memory() - Return statistics about system memory usage as a named tuple including the following fields, expressed in bytes")
    print(f'{psutil.virtual_memory().percent}% virtual memory is available\nMore Info - ')
    print(f'{psutil.virtual_memory()}')

    #swap_memory()
    print("\nswap_memory() - Return system swap memory statistics as a named tuple")
    print(f'{psutil.swap_memory().percent}% swap memory is available\nMore Info - ')
    print(psutil.swap_memory())

    #disk_partitions()
    print("\ndisk_partitions() - Return all mounted disk partitions as a list of named tuples including device, mount point and filesystem type ")
    print(f'C: drive - {psutil.disk_partitions()[0]}')
    print(f'D: drive - {psutil.disk_partitions()[1]}')
    print(f'E: drive - {psutil.disk_partitions()[2]}')

    #disk_usage()
    print("\ndisk_usage() - Return disk usage statistics about the partition")
    print(f'C: drive {psutil.disk_usage("c:").percent}% available - {psutil.disk_usage("c:")}')
    print(f'D: drive {psutil.disk_usage("d:").percent}% available - {psutil.disk_usage("d:")}')
    print(f'E: drive {psutil.disk_usage("e:").percent}% available - {psutil.disk_usage("e:")}')

#Network
def network_info():
    print("\nNetwork - Information\n")
    #net_connections()
    print("net_connections() - Return system-wide socket connections as a list of named tuples")
    print(f'IPV4 and IPV6 - {psutil.net_connections("inet")}')

    #boot_time
    print("\nBoot Time Analysis")
    print(f'Boot Time - {datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%d-%m-%Y %H:%M:%S")}')


cpu_info()
memory_info()
network_info()