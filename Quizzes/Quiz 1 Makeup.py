#running the program repeatedly without inputting anything will cause ValueErrors
#i.e., there is no defined error-state to handle empty inputs
looper = 0
#Program start
def main():
    name_list = []
    pass_list = []
    score_list = []
    
    people_number = int(input("How many scores would you like to enter? Max. 4\n"))
    
    if (people_number <=4):
    #prompt user input and append to list, then return list to global
        for i in range(people_number):
            print ("Score number:",i+1)
            name_input = input("What is your name?")
            name_list.append(name_input)
            #take user password and append to temporary list
            pass_input = input("What is your password?")
            pass_list.append(pass_input)
            #take user score and assign it to list
            score_input = input("What is your score?")
            score_list.append(float(score_input))
    else:
        print("no, follow the instructions")
        return
    
    pass_tuple = tuple(pass_list)

    #calculate average
    def calculate_average():
        running_sum = 0
        for i in range (people_number):
            running_sum = running_sum + score_list[i]
            average_score = float(running_sum) / people_number
            return average_score
        
    #print outputs and summary to user
    def print_summary():
        print("The names provided are:", name_list)
        print("The average score is:",average_score_output,"points.")
        
    #adjust grammar if user input one or multiple scores in
    
    if people_number == 1:
        #keep it in a variable because it gives me peace of mind
        average_score_output = calculate_average()
        print("The average score was calculated from 1 person.")
        print_summary()

    elif(people_number >1 and people_number < 4):
        average_score_output = calculate_average()
        print("The average score was calculated from",people_number,"people")
        print_summary()


        
#run repeatedly until user is satisfied.
while looper == 0:
    main()