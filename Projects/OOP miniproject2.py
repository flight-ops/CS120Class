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
        pass

    def enroll_student(self, student_name, report_dict):
        pass

class school_record:
    def __init__(self):
        pass

    

class teacher:
    def __init__(self, teacher_name, course_IDs) -> None:
        self.teacher_name = teacher_name
        self.course_IDs = course_IDs

class student:
    def __init__(self, student_name, report_dict) -> None:
        self.student_name = student_name
        self.student_report = report_dict



def write_to_log():
    pass

student_1 = student("Timmy",report_dict= {"Course1":"A","Course2":"B"})
student_2 = student("Tommy",report_dict={"Course1":"F","Course2":"C"})
student_3 = student("Tammy",report_dict={"Course3":"A","Course1":"B"})
student_dict = [student_1,student_2,student_3]

#search for a student in a certain course
def search_by_course(course_query):
    returnlist = []
    for student in student_dict:
        if course_query in student.student_report:
            returnlist.append(student.student_name)
    print(returnlist)

def search_by_grade(grade_query):
    returnlist = []
    for student in student_dict:
        print (student.student_report)
        for course in student.student_report:
            if student.student_report[course] == grade_query:
                returnlist.append(student.student_name)
    print(returnlist)



                

def search_by_course_and_grade(course_query,grade_query):
    returnlist = []

    for student in student_dict:
        #for each student, check if the student is in the specified class
        if course_query in student.student_report:
            print(student.student_name)
            #check if that student has the specified grade for the specified class
            if student.student_report[course_query] == grade_query:
                returnlist.append(student.student_name)

    #if a value exists
    if returnlist != []:
        print(returnlist)
    elif returnlist == []:
        print("Error: no students matching parameters")

def main():
    search_by_course_and_grade("Course1","B")
main()