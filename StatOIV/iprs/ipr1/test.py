
import csv

with open('ИПР1 - filtered_df (копия).csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    count_good, count = 0, 0
    for row in spamreader:
        count += 1
        if row[1] == '1' and row[7]=="TRUE" or row[1]=='0' and row[7]=="FALSE":
            print(row)
            count_good += 1

    print(count, count_good, count_good/count*100)

