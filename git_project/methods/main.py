"""
Main script for running the application.
"""

from git_project.methods.import_students import ImportStudents

PATH = "../lists/student_list.csv"
PATH2 = "lists/student_list.txt"

lista = ImportStudents.csv(PATH, ["Name", "Surname", "ID"])
"""
for student in lista:
    print(student.get("Name"), student.get("Surname"), student.get("ID"))

"""
lista2 = ImportStudents.txt(PATH2, ["Name", "Surname", "ID"])
"""
for student in lista2:
    print(student.get("Name"), student.get("Surname"), student.get("ID"))
"""

# ModifyStudents.add_student_and_export(path, path2, lista)

# for student in lista:
#    print(student.get("Name"), student.get("Surname"), student.get("ID"))

# ModifyStudents.add_student_by_overwriting(path, path2)
# ModifyStudents.modify_student(path, path2, lista)

# ModifyStudents.delete_student(path, path2, lista)
