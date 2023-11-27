#Sports department as static object, create UML and OOP code

#two dynamic objects, Student and Department Manager

#Student can use enroll_in_sport(), switch_to_new_sport(),
#drop_from_current_sport()

#department manager can use get_a_student_in_sport(), #view_all_student_in_sport()

#student can have a maximum of three sports

import random

class Department:
    def __init__(self, student_dict) -> None:
        self.student_dict = student_dict

class Student:
    def __init__(self, name, sports_enrolled) -> None:
        self.name = name
        self.sports_enrolled = sports_enrolled

    def __str__(self) -> str:
        return self.name
    
    def add_sport(self,sport_to_add):
        #append a sport to student's sports list
        self.sports_enrolled.append(sport_to_add)
     
    def switch_sport(self,sport_to_add,sport_to_drop):
        #grab index of sport that will be removed
        swap_index = self.sports_enrolled.index(sport_to_drop)
        #remove sport
        self.sports_enrolled.remove(sport_to_drop)
        #insert new sport using the saved index
        self.sports_enrolled.insert(swap_index, sport_to_add)

    def drop_sport(self,sport_to_drop):
        self.sports_enrolled.remove(sport_to_drop)

class Department_Manager:
    def __init__(self,name) -> None:
        self.name = name
    def get_student_in_sport(self,student_dict,sport_query):
        get_rand_student_in_sport(student_dict,sport_query)
    def get_all_in_sport(self,student_dict,sport_query):
        get_all_student_in_sport(student_dict,sport_query)


def manager_actions(student_dict):
    quit_condition = False
    while quit_condition == False:
        
        manager_action_request = input("What would you like to do? Options are: \nget a student in sport (will be a random one), get all students in a sport, or quit.\n")
        manager_action_request = manager_action_request.lower()
        

        if manager_action_request == "get a student in sport":
            case_sensitive_reminder()
            sport_query = input("What sport do you want to search with?\n")
            get_rand_student_in_sport(student_dict,sport_query)
        if manager_action_request == "get all students in a sport":
            case_sensitive_reminder()
            sport_query = input("What sport do you want to search with?\n")
            get_all_student_in_sport(student_dict,sport_query)
        #let the user quit
        elif manager_action_request == "quit":
            quit_condition = True
        else:
            print("Unknown input. Try again.")

    
def student_actions(student_identity):
    print (student_identity)
    quit_condition = False
    while quit_condition == False:
        print(f"Current sports: {student_identity.sports_enrolled}")
        student_action_request = input("What would you like to do? Options are: \nadd a sport, switch a sport, drop a sport, or quit.\n")
        student_action_request = student_action_request.lower()
        #let the user add a sport
        if student_action_request == "add a sport":
            sport_count = 0
            #count the sports in student attribute
            for i in student_identity.sports_enrolled:
                sport_count+=1

            #if less than max, let user add another sport
            if sport_count <3:
                case_sensitive_reminder()
                add_request = input("What sport would you like to add?\n")
                print("Adding sport...")
                student_identity.add_sport(add_request)
                print(f"Current student: {str(student_identity)} \nAdded sport: {add_request}")

                #three sport max condition
            else:
                print("\nError: student can only have maximum of three sports. try switching or removing a sport.\n")
        #let the user drop a sport
        elif student_action_request == "drop a sport":
            case_sensitive_reminder()
            drop_request = input("What sport would you like to drop?")
            print("Dropping sport...")
            student_identity.drop_sport(drop_request)
            print(f"Current student: {str(student_identity)} \nDropped sport: {drop_request}")
        #let the user switch a sport
        elif student_action_request == "switch a sport":
            case_sensitive_reminder()
            drop_request = input("What sport would you like to switch out?\n")
            add_request = input("What sport would you like to switch in?\n")
            print("Switching sports.")
            student_identity.switch_sport(add_request,drop_request)
            print(f"Current student: {str(student_identity)} \nSwitched {drop_request} with {add_request}.")
        #let the user quit
        elif student_action_request == "quit":
            quit_condition = True
        else:
            print("Unknown input. Try again.")

def identity_checker(student_dict):

    valid_ident = False
    while valid_ident == False:
        user_identity = input("Are you a Student or Department Manager? Alteratively, quit.\n")
        user_identity = user_identity.lower()
        if user_identity == "department manager":
            manager_actions(student_dict)
            
        elif user_identity == "student":
            student_ident = input("What is your name? (test w/ student1, student2, student3)\n")

            student_actions(student_dict[student_ident])
        elif user_identity == "quit":
            break
        else:
            print("Error. Try again.")

def get_rand_student_in_sport(student_dict,sport_query):
    return_list = []
    for student in student_dict:
        for student in student_dict:
            if sport_query in student_dict[student].sports_enrolled:
                return_list.append(student)
    rand_student = return_list[random.randint(0,len(return_list)-1)]
    print (f"{rand_student} is in {sport_query}")

def get_all_student_in_sport(student_dict,sport_query):
    return_list = []
    for student in student_dict:
        if sport_query in student_dict[student].sports_enrolled:
            return_list.append(student)
    print (f"List of all students in sport: {return_list}")

    
def case_sensitive_reminder():
    print(" --- important ---")
    print (" --- sport names are case sensitive ---")

def main():
    
    student1 = Student("student1",["Basketball","Baseball","Volleyball"])
    student2 = Student("student2",["Basketball","Badminton"])
    student3 = Student("student3",["Volleyball","Track and Field"])
    student4 = Student("student4",["Pickleball"])

    student_dict = {student1.name:student1, student2.name:student2, student3.name:student3, student4.name:student4}

    school_dept = Department(student_dict=student_dict)
    case_sensitive_reminder()
    identity_checker(school_dept.student_dict)
    



main()