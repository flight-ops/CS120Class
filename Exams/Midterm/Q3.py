
#function for owner to load movies
def owner_load():

    #create flag for loop
    load_condition = False
    while load_condition == False:
        load_number = int(input("How many movies would you like to load?"))
        #create empty list
        available_movie_list =[]
        #check if user's input is valid
        if load_number >3:
            print("error: max 3")
        else:
            #allow user to add an item the specified number of times
            for i in range (load_number):
                print("Movie number",i+1,":")
                available_movie_list.append(input("What is the movie you'd like to add?\n"))
                print(available_movie_list)
                load_condition = True
            #when loop ends, return movie list to main, which the user can then view and choose from.
            return available_movie_list
        
#allow user to choose a movie and watch it
def viewer_request(available_movie_list):
    #display available movies to user
    print("The current available movies are:",available_movie_list)
    user_request = input("Which movie would you like to watch?")

    #if the movie is added by the owner, the viewer can watch it, else it yields an error message
    if user_request in available_movie_list:

        print("Now playing:", user_request)
    
    else:
        print("Error: requested movie is not available / does not exist")

def main():
    #create flag for loop
    program_end_condition = False
    while program_end_condition == False:
        user_identity = ""
        #have user input identity
        user_identity = input("Type o if you are the owner, or v if you are the viewer.")
        #run appropriate functions
        if user_identity == "o":
            available_movie_list_main = owner_load()

        if user_identity == "v":
            viewer_request(available_movie_list=available_movie_list_main)


main()