#scenario is as follows:
#have three objects

#Teacher - can grade students, can searche for students using course IDs,
#and filter students based on grades (A,B,C, or otherwise)

#Student - can view grades and search for course ID given teacher name,
# or search for a teacher name given a course ID.

#SchoolRecord - holds a record of the changes made 

#some teachers may teach multiple courses, some students take multiple classes

#assume there are 10 courses, 20 students, and 5 teachers

class teacher:
    def __init__(teacher, teacher_name, course_ID) -> None:#insert data structure here
        pass

class student:
    def __init__(student, student_name, course_ID, course_grades) -> None:
        pass