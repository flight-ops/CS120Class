import math



#create a function that calculates distance

#prompt user for input for at least two points


def create_tuple():
    x_coord_local = input("\nWhat is your point's x-value?\n")
    y_coord_local = input("\nWhat is your point's y-value?\n")

    new_tuple_local = (int(x_coord_local),int(y_coord_local))
    return new_tuple_local

#get point 1
#create tuple


#get point 2
#create tuple







def main():
    print("Please input point 1.")
    user_point_tuple_1_main = create_tuple()
    print (user_point_tuple_1_main)
    print("\nPlease input point 2.")
    user_point_tuple_2_main = create_tuple()
    print (user_point_tuple_2_main)
    
   #sum x-vals and square them
    sum_of_x_squared = (float(user_point_tuple_1_main[0])+float(user_point_tuple_2_main[1]))**2
    #sum y-vals and square them
    sum_of_y_squared = (float(user_point_tuple_1_main[0])+float(user_point_tuple_2_main[1]))**2
    distance_main = (sum_of_x_squared+sum_of_y_squared) ** (1/2)
    print(distance_main)

main()