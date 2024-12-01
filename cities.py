import pandas as pd
import time

import csv

with open('worldcities.csv', newline='') as csvfile:

    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    for row in spamreader:

        print(', '.join(row))