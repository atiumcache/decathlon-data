import csv

seen = []

unique_contestants = 0

with open('decathlon_results.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    ro1 = next(reader)

    for row in reader:
        if row[2] in seen:
            continue
        else:
            seen.append(row[2])
            unique_contestants += 1

print(unique_contestants)