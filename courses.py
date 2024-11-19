from menu import Menu, MenuOption
from uinp import get_user_input
from clear import clear
import pickle
import os

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def list_students(self):
        for i in self.students:
            print(i)

    def __str__(self):
        return self.name

FILENAME = 'courses.p'

def ensure_file_exists():
    initial_data = [] 

    if not os.path.exists(FILENAME):
        with open(FILENAME, 'wb') as file:
            pickle.dump(initial_data, file)

def fetch_courses():
    ensure_file_exists() 
    with open(FILENAME, 'rb') as file:
        return pickle.load(file)

def save_courses(courses):
    with open(FILENAME, 'wb') as file:
        pickle.dump(courses, file)

def mock():
    pass

def display(courses):
    for i in courses:
        print(i)
    input()

def get_course_by_name(courses, name):
    for i in courses:
        if i.name == name:
            return i

def add(courses):
    name = get_user_input(str, 'Enter the course name: ')
    new_course = Course(name)
    courses.append(new_course)

def remove(courses):
    menu = Menu()
    for i in courses:
        menu.add_option(MenuOption(None, i.name))
    menu.add_option(MenuOption(None, 'Cancel'))

    print('Select a course you want to remove: ')
    menu.display()
    choice = menu.user_choice()
    if choice.title == 'Cancel':
        return
    courses.remove(get_course_by_name(courses, choice.title)) 

def manage(courses):
    menu = Menu()
    menu.add_option(MenuOption(mock, 'Add a student: '))

def manage():
    clear()
    courses = fetch_courses()

    menu = Menu()
    menu.add_option(MenuOption(display, 'Display all courses'))
    menu.add_option(MenuOption(add, 'Add a course'))
    menu.add_option(MenuOption(remove, 'Remove a course'))
    menu.add_option(MenuOption(mock, 'Manage a course'))
    menu.add_option(MenuOption(lambda x: x, 'Return to the main menu'))

    menu.display()
    choice = menu.user_choice()
    clear()
    choice.action(courses)

    save_courses(courses)

    if 'main menu' in choice.title:
        return

    manage()
    
