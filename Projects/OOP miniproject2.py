#scenario is as follows:
#have three objects

#Teacher - can grade students, can search for students using course IDs,
#and filter students based on grades (A,B,C, or otherwise)

#Student - can view grades and search for course ID given teacher name,
# or search for a teacher name given a course ID.

#SchoolRecord - holds a record of the changes made 

#some teachers may teach multiple courses, some students take multiple classes

#assume there are 10 courses, 20 students, and 5 teachers

class teacher:
    def __init__(self, teacher_name, course_IDs) -> None:#insert data structure here
        self.teacher_name = teacher_name
        self.course_IDs = course_IDs

class student:
    def __init__(self, student_name, course_IDs, course_grades) -> None:
        self.student_name = student_name
        self.course_IDs = course_IDs
        self.course_grades = course_grades


def write_to_log():
    pass

def main():
    pass

main()