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


#perform math operations on values inside the tuples

def calculate_distance(point1,point2):
    #sum x-vals and square them
    sum_of_x_squared = (point1[1]+point2[1])**2
    #sum y-vals and square them
    sum_of_y_squared = (point1(2)+point2[2])**2


    distance_local_cd = (sum_of_x_squared+sum_of_y_squared) ** (1/2)

    return distance_local_cd




def main():
    print("Please input point 1.")
    user_point_tuple_1_main = create_tuple()
    print (user_point_tuple_1_main)
    print("\nPlease input point 2.")
    user_point_tuple_2_main = create_tuple()
    print (user_point_tuple_2_main)
    
    print(calculate_distance(user_point_tuple_1_main,user_point_tuple_2_main))


main()