import math
import csv
with open('data.csv',newline='') as c:
    reader = csv.reader(c)
    prov_data = list(reader)

data = prov_data[0]

def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += float(x)
    
    mean = total/n
    print('MEAN OR AVERAGE OF THE DATA -> ' + str(mean))
    return mean

squared_list = []
for number in data:
    a = int(number) - mean(data)
    a = a**2
    squared_list.append(a)

sum = 0 
for y in squared_list:
   sum = sum+y


result= sum/(len(data)-1)

standard_deviation = math.sqrt(result)
print( standard_deviation)