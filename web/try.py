


class Student:

    count = 0

    def __init__(self,name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"


print(Student.get_count())