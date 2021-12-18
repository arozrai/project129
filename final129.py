import csv

dataset_1 = []
dataset_2 = []

# df = df[df['Mass'].notna()]
# df = df[df['Orbital_period'].notna()]
# df = df[df['Semimajor_axis'].notna()]
# df = df[df['Ecc.'].notna()]

with open("dataset_1.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_1.append(row)

with open("dataset_2_sorted.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_2.append(row)

headers_1 = dataset_1[0]
dwarf_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
dwarf_data_2 = dataset_2[1:]

headers = headers_1 + headers_2
dwarf_data = []
for index, data_row in enumerate(dwarf_data_1):
    dwarf_data.append(dwarf_data_1[index] + dwarf_data_2[index])

with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(dwarf_data)