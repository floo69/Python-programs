# Create two threads where in one will print grade of a student and another will print name of student

import threading

def grade(grade):
    print(f"The grade is {grade}")

def name(name):
    print(f"The name is {name}")

s_name="abc"
s_grade="a"

name_t = threading.Thread(target=name, args=(s_name,))
grade_t = threading.Thread(target=grade, args=(s_grade,))

name_t.start()
grade_t.start()

name_t.join()
grade_t.join()