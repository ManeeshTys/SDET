import csv

with open('resources\csvDemo.csv') as csvFile:
    csvReader = csv.reader(csvFile,delimiter=',')
    names = []
    status = []
    for row in csvReader:
        names.append(row[0])
        status.append(row[1])
    print(names)
    print(status)
indexNumber = names.index('Tys')
LoanStatus = status[indexNumber]
print('Loan status of tys is '+LoanStatus)
print(csvReader)

with open('resources/csvDemo.csv','a',newline='') as csvF:
    write = csv.writer(csvF)
    write.writerow(['Avatar', 'Approved'])
