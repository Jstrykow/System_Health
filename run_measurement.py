import csv
from time import time, sleep
import psutil

# get id in existing file
with open("system_health.csv", 'r') as fp:
    for id, line in enumerate(fp):
        pass
id = id + 1 #enumerate need increament

number_of_second_to_run = 5
time_between_measurements = 1
for x in range(number_of_second_to_run):
    sleep(time_between_measurements)
    virtual_memory = psutil.virtual_memory()
    data = [ id, psutil.cpu_percent(), round(virtual_memory.total / (1024.0 ** 3), 3), round(virtual_memory.available / (1024.0 ** 3), 3) , round(virtual_memory.used / (1024.0 ** 3), 3), virtual_memory.percent ]
    with open("system_health.csv", "a") as csv_file:
        writer = csv.writer(csv_file)
        # write the header
        writer.writerow(data)
    id = id + 1
