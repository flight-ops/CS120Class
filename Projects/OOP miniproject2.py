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
    
    # method to hire a teacher given a name and a list of courses
    def hire_teacher(self):
        hire_name = input("What is the name of the teacher to be hired?\n")
        hire_course = input("What course do they teach? (Additional courses may be added later)\n")
        new_teacher = teacher(hire_name,[hire_course])
        teacher_list.append(new_teacher)

    def enroll_student(self, student_name, report_list):
        new_student = student(student_name=student_name,student_list=student_list)
        student_list.append(new_student)

class school_record:
    def __init__(self,record):
        self.record = record

class teacher:
    def __init__(self, teacher_name, course_IDs) -> None:
        self.teacher_name = teacher_name
        self.course_IDs = course_IDs

    def teacher_change_grade(self,student_list):
        teacher_specify_student = input("Which student's grade would you like to change?\n")
        for student in student_list:
            if teacher_specify_student == student.student_name:
                print("Found student.")
                teacher_specify_course = input("Which course's grade would you like to change?\n")
                teacher_specify_grade = input("What grade would you like to change it to?\n")
                student.student_report[teacher_specify_course] = teacher_specify_grade
                print("Successfully changed grade")
                
                print(f"Student {teacher_specify_student}'s grade in {teacher_specify_course} to {teacher_specify_grade}.")
            elif teacher_specify_student not in student_list:
                print("Student does not exist!")
                break
            else:
                break

    # search for a student with matching course and grades
    def teacher_search_by_course_and_grade(self, course_query,grade_query):
        returnlist = []

        for student in student_list:
            #for each student, check if the student is in the specified class
            if course_query in student.student_report:
                #check if that student has the specified grade for the specified class
                if student.student_report[course_query] == grade_query:
                    #if so, append to the returnlist
                    returnlist.append(student.student_name)

        # only return a list if non-null
        if returnlist != []:
            print(returnlist)
        elif returnlist == []:
            print("Error: no students matching parameters")

    # search for a student / students with matching name(s)
    def teacher_search_by_name(name_query):
        returnlist = []
        for student in student_list:
            if student.student_name == name_query:
                returnlist.append(student.student_name)

        # only return a list if non-null
        if returnlist != []:
            print(returnlist)
        elif returnlist == []:
            print("Error: no students matching parameters")

class student:
    def __init__(self, student_name, report_list) -> None:
        self.student_name = student_name
        self.student_report = report_list

    def student_search_teacher_by_name(parameter_list):
        student_search_query = input("What is the name of the teacher you'd like to search for?\n")
        if student_search_query not in teacher_list:
            print("Error: There are no teachers with that name.")
            return
        for teacher in teacher_list:
            if student_search_query == teacher.teacher_name:
                print(f"Found teacher. Courses offered: {teacher.course_IDs}")


    def student_search_teacher_by_course(teacher_list):
        returnlist = []
        student_search_query = input("What class are you looking for?\n")
        for teacher in teacher_list:
            if student_search_query in teacher.course_IDs:
                returnlist.append(teacher.teacher_name)
        if returnlist == []:
            print("Error: No teachers offer that course")
        else:
            print(f"The following teachers offer this course: {returnlist}")
        
                

#login or suffer
def login():
    login_loop = True
    while login_loop == True:
        credential = input("log in, suffer, or quit")
        credential = credential.lower()
        if credential == "teacher":
            print("ok you are a teacher now")
            teacher_actions()
            log_action("teacher logged in")
        elif credential == "student":
            print("ok you are a student now")
            student_actions()
            log_action("student logged in")
        elif credential == "administrator":
            print("ok you are an administrator now")
            admin_actions()
            log_action("admin logged in")
        elif credential == "quit":
            print ("ok quit")
            break
        else:
            print("oops something is wrong")



# path of options a student can take
def student_actions():
    pass
# path of options a teacher can take
def teacher_actions():
    pass
def admin_actions():
    admin_action_request = input("What would you like to do?")

    admin_action_request = admin_action_request.lower()

    if admin_action_request == "view school log":
        print(my_school_record.school_record)
    elif admin_action_request == "hire teacher":
        pass
    elif admin_action_request == "enroll student":
        my_school_system.enroll_student(student_name="",report_list="")
    pass
    
#while I could create a csv file and write to it, I didn't feel like it. Instead, everything is appended to a gigantic list.
def log_action(action):
    giant_action_log.append(action)



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
teacher_list = [teacher_1,teacher_2,teacher_3]
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
    
    my_school_system.hire_teacher()
    for teacher in my_school_system.teacher_list:
        print(teacher.teacher_name,teacher.course_IDs)
main()