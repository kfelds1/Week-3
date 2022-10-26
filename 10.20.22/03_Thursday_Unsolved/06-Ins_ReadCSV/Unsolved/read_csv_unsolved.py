# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Next, import module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'accounting.csv')

# Reading CSV File using CSV module
with open(csvpath) as csvfile:

    # TODO: CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    # TODO: Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)