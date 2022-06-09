import csv

with open("C:/Users/91982/OneDrive/Desktop/Python/Project/P104 Mean,Median Mode/Height-Weight.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []
length = len(file_data)

for i in range(length):
    a = file_data[i][2]
    new_data.append(float(a))

n = len(new_data)
total = 0

for x in new_data:
    total += x

mean = total/n

print("Mean is:", str(mean))

    

