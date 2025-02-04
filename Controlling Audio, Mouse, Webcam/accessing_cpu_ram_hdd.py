import psutil

# return number of CPU cores
print(psutil.cpu_count())

# return number of Physical CPU cores
print(psutil.cpu_count(logical=False))

# Current CPU usage
print(psutil.cpu_percent(interval=1))

# CPU stats
print(psutil.cpu_stats())

# CPU frequency
print(psutil.cpu_freq())

# RAM statistics
print(psutil.virtual_memory())
print(psutil.swap_memory())


# HDD stats
print(psutil.disk_usage('/'))

# HDD Partitions
print(psutil.disk_partitions())