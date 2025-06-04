import csv

with open('../../quantium-repo/data/daily_sales_data_0.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row[2:5])}')
            line_count += 1
        else:
            if row[0] == 'pink morsel':
                print(f'\t{row[2]} {row[3]} {row[4]}')
                line_count += 1