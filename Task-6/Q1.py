
#Q1
import re,csv
fh = open('onelinefile.txt')
for i in fh:
        r = re.findall(r'[+-]?[0-9]+\.[0-9]+', i)
        q = re.findall(r'[a-zA-Z]+', i)
        j = 0
        for p in range(len(r)):
            with open('onelinefile.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([str(p+1), q[j],r[p],q[j+1]])
            j += 2

with open('onelinefile.csv', 'r',) as file:
    reader = csv.reader(file)
    for row in reader:
        print(','.join(row))





        
