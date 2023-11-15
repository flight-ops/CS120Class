#scenario is as follows:
#have three objects

#Teacher - can grade students, can search for students using course IDs,
#and filter students based on grades (A,B,C, or otherwise)

#Student - can view grades and search for course ID given teacher name,
# or search for a teacher name given a course ID.

#SchoolRecord - holds a record of the changes made 

#some teachers may teach multiple courses, some students take multiple classes

#assume there are 10 courses, 20 students, and 5 teachers


class school:
    def __init__(self):
        pass

    #method to hire a teacher given a name and a list of courses
    def hire_teacher(self, teacher_name, courses_list):
        new_teacher = teacher(teacher_name=teacher_name,teacher_dict=teacher_dict)
        teacher_dict.append(new_teacher)

    def enroll_student(self, student_name, report_dict):
        new_student = student(student_name=student_name,student_dict=student_dict)
        student_dict.append(new_student)

class school_record:
    def __init__(self,record):
        self.record = record

    

class teacher:
    def __init__(self, teacher_name, course_IDs) -> None:
        self.teacher_name = teacher_name
        self.course_IDs = course_IDs

    def change_grade(self, student_dict):
        pass

class student:
    def __init__(self, student_name, report_dict) -> None:
        self.student_name = student_name
        self.student_report = report_dict




def write_to_log():
    pass




#search for a student in a certain course
def search_by_course(course_query):
    returnlist = []
    for student in student_dict:
        if course_query in student.student_report:
            returnlist.append(student.student_name)
    print(returnlist)

#search for a 
def search_by_grade(grade_query):
    returnlist = []
    for student in student_dict:
        print (student.student_report)
        for course in student.student_report:
            if student.student_report[course] == grade_query:
                returnlist.append(student.student_name)
    print(returnlist)

def search_by_name(name_query):
    returnlist = []
    for student in student_dict:
        if student.student_name == name_query:
            returnlist.append(student.student_name)

def login():
    login_loop = True
    while login_loop == True:
        credential = input("log in or suffer (or quit, idk)")
        credential = credential.lower()
        if credential == "teacher":
            print("ok you are a teacher now")
            log_action("teacher logged in")
        elif credential == "student":
            print("ok you are a student now")
            log_action("student logged in")
        elif credential == "quit":
            print ("ok quit")
            break
        else:
            print("oops something is wrong")


#while I could create a csv file and write to it, I didn't feel like it. Instead, everything is appended to a gigantic list.
def log_action(action):
    giant_action_log.append(action)

def search_by_course_and_grade(course_query,grade_query):
    returnlist = []

    for student in student_dict:
        #for each student, check if the student is in the specified class
        if course_query in student.student_report:
            #check if that student has the specified grade for the specified class
            if student.student_report[course_query] == grade_query:
                #if so, append to the returnlist
                returnlist.append(student.student_name)

    #if a value exists
    if returnlist != []:
        print(returnlist)
    elif returnlist == []:
        print("Error: no students matching parameters")




# Student initialization
student_1 = student("Timmy",report_dict= {"Course1":"A","Course2":"B"})
student_2 = student("Tommy",report_dict={"Course1":"F","Course2":"C"})
student_3 = student("Tammy",report_dict={"Course3":"A","Course1":"B"})
student_4 = student("Rinny",report_dict={"Course5":"D","Course3":"A"})
student_5 = student("Ronny",report_dict={"Course2":"B","Course3":"B"})

teacher_1 = teacher("Prof. Richards",["Course1","Course2"])
teacher_2 = teacher("Prof. Maharaja",["Course3","Course4"])
teacher_3 = teacher("Prof. Mabsen",["Course5"])
student_dict = [student_1,student_2,student_3,student_4,student_5]
teacher_dict = [teacher_1,teacher_2]

#using a CSV file would be wise, but I don't feel like it
giant_action_log = []




def main():
    search_by_course_and_grade("Course1","B")
    main_loop = True
    while main_loop == True:
        login()
        print(giant_action_log)
    
main()