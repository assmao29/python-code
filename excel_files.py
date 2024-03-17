import csv

with open("week23.csv", 'w') as f:
    pen = csv.writer(f)
    header = ["Name", "Cell Phone", "city"]
    pen.writerow(header)
    pen.writerow(header)
    entry1 = ["mao", "333 333 3456", "La Vista"]
    pen.writerow(entry1)
    f.close