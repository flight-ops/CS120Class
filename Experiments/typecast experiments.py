# 8.20.23; type casting experiments

print("wow operands")

my_operand_1 = (9, 2, 3, 4) 
my_operand_2 = ",7, 2, 4, 6"
print(type(my_operand_1))

result = str(my_operand_1) + my_operand_2

print(result, type(result))


def add_numbers (a,b):
    a = int(input("what first number"))
    b = int(input("what second number"))
    return (a+b)