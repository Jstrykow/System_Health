import csv
import psutil

header = ['ID', 'Percent_CPU_UTIL', 'Total_Memory_GB', 'Avaiable_Memory_GB', 'Usage_Memory_GB', 'Percent_Memory_Used']

# open the file in the write mo
with open("system_health.csv", "a") as csv_file:
    writer = csv.writer(csv_file)
    # write the header
    writer.writerow(header)
