import csv

with open('findsdataset.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

h = ['0', '0', '0', '0', '0', '0']

for i in your_list:
    print(i)
    if i[-1] == "TRUE":
        j = 0
        for x in i:
            if x != "TRUE":
                if x != h[j] and h[j] == '0':
                    h[j] = x
                elif x != h[j] and h[j] != '0':
                    h[j] = '?'
                else:
                    pass
            j = j + 1
print("A Maximally Specific hypothesis is")
print(h)
