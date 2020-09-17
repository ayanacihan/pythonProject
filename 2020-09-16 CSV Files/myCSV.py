#How to read from a csv file using the csv module of python
import csv

with open('iris.csv','rt')as file: #the file should be in the same folder with the python file.
    csv_rows = csv.reader(file)
    for row in csv_rows:
        print(row)