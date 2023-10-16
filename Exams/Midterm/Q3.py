

def owner_load():
    
    #available_movie_list = input("What would you like to load?")


    load_condition = False
    while load_condition == False:
        load_number = int(input("How many movies would you like to load?"))
        available_movie_list =[]
        if load_number >3:
            print("error: max 3")
        else:
            for i in range (load_number):
                print("Movie number",i+1,":")
                available_movie_list.append(input("What is the movie you'd like to add?"))
                print(available_movie_list)
            return available_movie_list

def viewer_request(available_movie_list):
    print("The current available movies are:",available_movie_list)
    user_request = input("Which movie would you like to watch?")
    if user_request in available_movie_list:

        print("Now playing:", user_request)
    
    else:
        print("Error: requested movie does is not available")

def main():
    program_end_condition = False
    while program_end_condition == False:

        user_identity = ""
        user_identity = input("Type o if you are the owner, or v if you are the viewer.")
        if user_identity == "o":
            available_movie_list_main = owner_load()

        if user_identity == "v":
            viewer_request(available_movie_list=available_movie_list_main)


main()