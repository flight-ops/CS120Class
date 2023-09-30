#Number 9
#create a few variables with a few data types
my_list = [1, 2, 3, 4]
my_set = {1, 2, 3, 4}
my_dict = {'apples' : 5, 'oranges' : 10, 'bananas' : 15 }
my_tuple = (1, 2, 2, 3, 4)

#print stored data to console
print("these are the original values \n")
print(my_list)
print(my_set)
print(my_dict)
print(my_tuple)

#modify the mutable types
my_list.append(5)
my_set.add(10)
my_dict.update({'apples' : 5, 'oranges' : 10, 'bananas' : 15, 'pears':20})
print("\n data changed \n")

print("these are the new values \n")
print(my_list)
print(my_set)
print(my_dict)
print ("I have" , my_dict.get('apples'), "apples.")
print(my_tuple.count(2))