import csv
import psutil

header = ['ID', 'CPU_UTIL', 'Total_Memory', 'Avaiable_Memory', 'Usage_Memory', 'Percent_Memory_Used']

# open the file in the write mo
with open("system_health.csv", "a") as csv_file:
    writer = csv.writer(csv_file)
    # write the header
    writer.writerow(header)
