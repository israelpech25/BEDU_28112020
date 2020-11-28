#Utilizando modulo csv para lectura de arcivos extensión csv

import csv

filename = 'employees.csv'

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)