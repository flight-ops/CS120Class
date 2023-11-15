#the library system is a static object

#create a UML diagram as well as OOP code

#two dynamic objects, Student and Librarian, each with certain methods

#Students can use check_in_book(), check_out_book, see_all_books()

#Librarians can use count_all_book(), view_all_books_checked_out() (i.e. all the books being used by a student object)
#count status() (shows int number of books on hand, as well as number of books in use)

#create an initial list of books that can be checked out or are already checked out



#challenge: create a program that involves MULTIPLE "library" objects
#say, perhaps an object for each genre?

#initial library states
available_books_library_1 = ["comic book","dictionary"]
checked_out_books_library_1 = ["poetry book"]

available_books_library_2 = ["graphic novel","encyclopedia"]
checked_out_books_library_2 = ["YA novel"]


class Library:
    def __init__(self, name, available_books, checked_out_books) -> None:
        self.name = name
        self.available_books = available_books
        self.checked_out_books = checked_out_books
        


class Student:
    def __init__(self) -> None:
        pass
    #check if the book exists in the current database, and perform a transfer between the lists.
    #first append the book to the "available" list, then remove it from the "checked out" list
    def check_in_book(self,current_available,current_checked_out,transfer_book):
        if transfer_book in current_checked_out:
            print("Checking in book.")
            current_available.append(transfer_book)
            print("Book checked in.")
            current_checked_out.remove(transfer_book)

        elif transfer_book not in current_checked_out:
            print("Could not find the book. Try again.")
        
    #perform the same procedure as the previous method, but instead, in reverse
    def check_out_book(self,current_available,current_checked_out,transfer_book):
        if transfer_book in current_available:
            print("Checking out book.")
            current_checked_out.append(transfer_book)
            print("Book checked out.")
            current_available.remove(transfer_book)

        elif transfer_book not in current_available:
            print("Could not find the book. Try again.")

    def see_all_books(self,current_available):
        print(f"Here are all the books currently available:\n{current_available}")

class Librarian:

    def __init__(self) -> None:
        pass

    def count_all_books(self,current_available,current_checked_out):
        book_count = 0 
        for i in current_available:
            book_count += 1
        for i in current_checked_out:
            book_count +=1
        print(f"There are currently {book_count} books in the current library's system")

    def view_all_checked_out_books(self,current_checked_out):
        print(f"Here are all books currently checked out: {current_checked_out}")

    def view_count_status(self,current_available,current_checked_out):
        available_count = 0
        checked_out_count = 0
        for i in current_available:
            available_count +=1
        print(f"There is/are currently {available_count} book(s) available in the current library's system")
        for i in current_checked_out:
            checked_out_count +=1
        print(f"There is/are currently {checked_out_count} book(s) checked out in the current library's system")

#prompt user for identity then provide them with appropriate actions
def identity_check(Library_System):
    loop_flag = True
    while loop_flag == True:
        identity = None
        identity = input("Are you a Student or Librarian? (Alternatively, quit)\n")
        identity = identity.lower()

        if identity == "student":
            Student_actions(Library_System)
        elif identity == "librarian":
            Librarian_actions(Library_System)
        elif identity == "quit":
            break
        else:
            print("Invalid input, try again")

#actions a student can perform
def Student_actions(Library_System):
    student_break_request = False
    while student_break_request == False:
        student_action_request = input("""What would you like to do? Options are:
check out book, check in book, see all books (you will only see currently available books), or quit\n""")
        
        student_action_request = student_action_request.lower()
        if student_action_request == "check out book":
            Student.check_out_book(Student,Library_System.available_books,Library_System.checked_out_books,input("Which book would you like to check out?\n"))
        elif student_action_request == "check in book":
            Student.check_in_book(Student,Library_System.available_books,Library_System.checked_out_books, input("Which book would you like to check in?\n"))
        elif student_action_request == "see all books":
            Student.see_all_books(Student,Library_System.available_books)
        elif student_action_request == "quit":
            print("Logging out.")
            break

#actions a librarian can perform
def Librarian_actions(Library_System):
    librarian_break_request = False
    while librarian_break_request == False:
        librarian_action_request = input("""What would you like to do? Options are:
count all books, view all books checked out, view count status or quit\n""")
        librarian_action_request = librarian_action_request.lower()
        if librarian_action_request == "count all books":
            print("Counting all books.")
            Librarian.count_all_books(Librarian,Library_System.available_books,Library_System.checked_out_books)
        elif librarian_action_request == "view all books checked out":
            print("Viewing all books checked out")
            Librarian.view_all_checked_out_books(Librarian,Library_System.checked_out_books)
        elif librarian_action_request == "view count status":
            Librarian.view_count_status(Librarian,Library_System.available_books,Library_System.checked_out_books)
        elif librarian_action_request == "quit":
            print("Logging out.")
            break

def location_prompt(Library1,Library2):
    valid_input = False
    while valid_input == False:
        user_location = input("Which library would you like to visit? \nOptions are Library System 1 and Library System 2\n")
        
        if user_location == Library1.name:
            print("Entering Library 1")
            return Library1
        elif user_location == Library2.name:
            print("Entering Library 2")
            return Library2
        else:
            print("Error.")
            continue
    

def main():
    Library1 = Library("Library System 1",available_books_library_1,checked_out_books_library_1)
    Library2 = Library("Library System 2",available_books_library_2,checked_out_books_library_2)

    main_loop = True
    while main_loop == True:
        identity_check(location_prompt(Library1,Library2))

main()


