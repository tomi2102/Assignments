class Student:
    def __init__(student, student_id, student_name,student_class ):
        student.id = student_id
        student.name = student_name
        student.classes = student_class
    def __str__(student):
        return student.id, student.name, student.classes


