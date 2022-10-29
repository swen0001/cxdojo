import csv


with open('test_task.csv') as f:

    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i == 0:
            pass
        else:
            if row[0] == '' or row[1] == '' or row[2] == '':
                pass
            else:
                print(f'{row[0]} {row[1]} {row[2]}')
