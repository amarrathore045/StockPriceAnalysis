import csv

data = []
with open('ticker.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

data_new = data[0]

with open('ticker_list.txt', 'w') as f:
    for i in data_new:
        f.write("'" + i.strip() + "',")
