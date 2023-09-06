#9.2.23
#data type experiments

my_numbers = [11, 65, 100, 255]
my_binaries = [1101, 1000, 101011]

for i in my_numbers:
    print(bin(i))

for i in my_binaries:
    print(int(str(i),2))