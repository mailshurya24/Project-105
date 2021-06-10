import math
import csv

with open("data.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(df):
    n = len(df)
    total = 0

    for x in df:
        total += int(x)
    
    mean =  total/n
    return mean

square_list = []

for number in data:
    a = int(number) - mean(data)
    a = a**2
    square_list.append(a)

sum = 0

for i in square_list:
    sum += i
    
result = sum/(len(data) - 1)
sd = math.sqrt(result)

print(sd)