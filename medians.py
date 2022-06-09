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

if(n%2 == 0):
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2 -1])
    median = (median1 + median2)/2
else: 
    median = float(new_data[n//2])
    print(n)

print("Median is:", str(median))