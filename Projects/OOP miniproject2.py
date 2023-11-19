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
    def __init__(self, student_list, teacher_list, school_record):
        self.student_list = student_list
        self.teacher_list = teacher_list
        self.school_record = school_record
    
    #method to hire a teacher given a name and a list of courses
    # def hire_teacher(self, teacher_name, courses_list):
    #     new_teacher = teacher()
    #     teacher_list.append(new_teacher)

    # def enroll_student(self, student_name, report_list):
    #     new_student = student(student_name=student_name,student_list=student_list)
    #     student_list.append(new_student)

class school_record:
    def __init__(self,record):
        self.record = giant_action_log

    
class teacher:
    def __init__(self, teacher_name, course_IDs) -> None:
        self.teacher_name = teacher_name
        self.course_IDs = course_IDs

    def change_grade(self, student_list):
        pass

class student:
    def __init__(self, student_name, report_list) -> None:
        self.student_name = student_name
        self.student_report = report_list




#search for a student in a certain course
def search_by_course(course_query):
    returnlist = []
    for student in student_list:
        if course_query in student.student_report:
            returnlist.append(student.student_name)
    print(returnlist)

#search for a 
def search_by_grade(grade_query):
    returnlist = []
    for student in student_list:
        print (student.student_report)
        for course in student.student_report:
            if student.student_report[course] == grade_query:
                returnlist.append(student.student_name)
    print(returnlist)

def search_by_name(name_query):
    returnlist = []
    for student in student_list:
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

    for student in student_list:
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

def teacher_change_grade(student_list):
    teacher_specify_student = input("Which student's grade would you like to change?\n")
    for student in student_list:
        if teacher_specify_student == student.student_name:
            print("Found student.")
            teacher_specify_course = input("Which course's grade would you like to change?\n")
            teacher_specify_grade = input("What grade would you like to change it to?\n")
            student.student_report[teacher_specify_course] = teacher_specify_grade
            print("Successfully changed grade")
            print(student.student_report[teacher_specify_course])
            # print(f"Student {teacher_specify_student}")
        elif teacher_specify_student not in student_list:
            print("Student does not exist!")
            break
        else:
            break

# path of options a student can take
def student_actions():
    pass
# path of options a teacher can take
def teacher_actions():
    pass


#using a CSV file would be wise, but I don't feel like it
giant_action_log = []

# Student initialization with names, courses, and their associated grades
student_1 = student("Timmy",report_list= {"Course1":"A","Course2":"B"})
student_2 = student("Tommy",report_list={"Course1":"F","Course2":"C"})
student_3 = student("Tammy",report_list={"Course3":"A","Course1":"B"})
student_4 = student("Rinny",report_list={"Course5":"D","Course3":"A"})
student_5 = student("Ronny",report_list={"Course2":"B","Course3":"B"})

# Teacher initialization with names, as well as courses taught
teacher_1 = teacher("Prof. Richards",["Course1","Course2"])
teacher_2 = teacher("Prof. Maharaja",["Course3","Course4"])
teacher_3 = teacher("Prof. Mabsen",["Course5"])


# object actualization
#create a list for the students
student_list = [student_1,student_2,student_3,student_4,student_5]
#create a list for the teachers
teacher_list = [teacher_1,teacher_2]
#create school record object
my_school_record = school_record(record=giant_action_log)
#create school system object that contains the above lists/objects
my_school_system = school(teacher_list=teacher_list,student_list=student_list,school_record=my_school_record)




def main():
    # search_by_course_and_grade("Course1","B")
    # print (student_1.student_report["Course1"])
    # main_loop = True
    # while main_loop == True:
    #     login()
    #     print(giant_action_log)
    teacher_change_grade(student_list)
    
    
main()