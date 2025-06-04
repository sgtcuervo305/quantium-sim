import csv

with open('../../quantium-repo/data/daily_sales_data_0.csv', 'r') as csvfile, \
     open('filtered_results.csv', 'w', newline='') as outfile:
    reader = csv.reader(csvfile, delimiter=',')
    writer = csv.writer(outfile)
    line_count = 0
    for row in reader:
        if line_count == 0:
            # Write header for columns 2, 3, 4
            writer.writerow(row[2:5])
            print(f'Column names are {", ".join(row[2:5])}')
            line_count += 1
        else:
            if row[0] == 'pink morsel':
                writer.writerow(row[2:5])
                print(f'\t{row[2]} {row[3]} {row[4]}')
                line_count += 1