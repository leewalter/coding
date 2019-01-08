# based on https://github.com/hpreston/python_networking
# https://docs.python.org/3.7/library/csv.html

# Import the csv library
import csv

# Open the sample csv file and print it to screen
with open("csv_example.csv") as f:
    print(f.read())

# Open the sample csv file, and create a csv.reader object
with open("csv_example.csv") as f:
    csv_python = csv.reader(f)
    # Loop over each row in csv and leverage the data in code
    for row in csv_python:
        print("{device} is in {location} " \
              "and has IP {ip}.".format(
                  device = row[0],
                  location = row[2],
                  ip = row[1]
                  )
                )
'''
(base) D:\github\walter-repo\python_networking\data_manipulation\csv>python csv_example.py
"router1","10.1.0.1","New York"
"router2","10.2.0.1","Denver"
"router3","10.3.0.1","Austin"

router1 is in New York and has IP 10.1.0.1.
router2 is in Denver and has IP 10.2.0.1.
router3 is in Austin  and has IP 10.3.0.1.
'''
