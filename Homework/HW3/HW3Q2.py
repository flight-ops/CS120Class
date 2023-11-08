#Sports department as static object, create UML and OOP code

#two dynamic objects, Student and Department Manager

#Student can use enroll_in_sport(), switch_to_new_sport(),
#drop_from_current_sport()

#department manager can use get_a_student_in_sport(), #view_all_student_in_sport()

#student can have a maximum of three sports
class Department:
    def __init__(self) -> None:
        pass

class Student:
    def __init__(self, name, sports_enrolled) -> None:
        self.name = name
        self.sports_enrolled = sports_enrolled

    def __str__(self) -> str:
        return self.name
    
    def add_sport(self,sport_to_add):
        
        self.sports_enrolled.append(sport_to_add)

    def switch_sport(self,sport_to_add,sport_to_drop):
        self.sports_enrolled.remove(sport_to_drop)
        self.sports_enrolled.append(sport_to_add)

    def drop_sport(self,sport_to_drop):
        self.sports_enrolled.remove(sport_to_drop)

class Department_Manager:
    def __init__(self) -> None:
        pass
    def get_student_in_sport(self):
        pass
    def view_all_in_sport(self):
        pass
#create a function to limit the number of sports a student can be in
def sport_count_checker(student_object):
    pass

def manager_actions():
    manager_action_request = input("")
def student_actions(student_identity):
    print (student_identity)
    quit_condition = False
    while quit_condition == False:
        student_action_request = input("What would you like to do? Options are: \nadd a sport, switch sports, drop a sport, or quit.\n")
        student_action_request = student_action_request.lower()

        if student_action_request == "add a sport":
            add_request = input("What sport would you like to add?\n")
            student_identity.add_sport(add_request)
            print("Adding sport...")
            print(f"Current student: {str(student_identity)} \nAdded sport: {add_request}")
        elif student_action_request == "quit":
            quit_condition = True
        else:
            print("Unknown input. Try again.")

def identity_checker(student_dict):

    print(student_dict)
    valid_ident = False
    while valid_ident == False:
        user_identity = input("Are you a Student or Department Manager? Alteratively, quit.\n")
        user_identity = user_identity.lower()
        if user_identity == "department manager":
            manager_actions()
            
        elif user_identity == "student":
            student_ident = input("What is your name? (test w/ student1, student2, student3)\n")

            student_actions(student_dict[student_ident])
        elif user_identity == "quit":
            break
        else:
            print("Error. Try again.")

            

    
    

def main():
    student1 = Student("student1",["Basketball"])
    student2 = Student("student2",["Basketball"])
    student3 = Student("student3",["Volleyball"])

    student_dict = {student1.name:student1, student2.name:student2, student3.name:student3}
    identity_checker(student_dict)



main()