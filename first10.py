# alex
import sys
print(sys.argv)

                     
file_name = sys.argv[1]    #file_name = 'first_10.csv'
pricemin = int(sys.argv[2])
pricemax = int(sys.argv[3])

f = open(file_name)
lines = f.readlines()
for line in lines[1:]:
    columns = line.split(',')

    price = int(columns[9])
#    if price >= 100 and price <= 150:
    if price >= pricemin and price <= pricemax:
        print(line)