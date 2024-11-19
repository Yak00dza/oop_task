from menu import Menu, MenuOption
from clear import clear
import courses

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f'{self.name}: {{self.email}}'

class Student(Person):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id

class Instructor(Person):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.courses = []

    def add_coursee(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def list_courses(self):
        for i in self.courses:
            print(i)

    def list_students(self):
        result = []
        for i in self.courses:
            for j in i.students:
                result.append((j.name, i.name))
        return result

def mock():
    pass

def main():
    clear()
    print('Welcome to the course manager!')
    main_menu = Menu()
    main_menu.add_option(MenuOption(courses.manage, 'Manage courses'))
    main_menu.add_option(MenuOption(mock, 'Manage students'))
    main_menu.add_option(MenuOption(mock, 'Manage instructors'))
    main_menu.add_option(MenuOption(exit, 'Exit the program'))

    main_menu.display()
    choice = main_menu.user_choice()
    choice.action() 

if __name__ == '__main__':
    while True:
        main()
