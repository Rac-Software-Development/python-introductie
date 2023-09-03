import json
import random
import string
from pathlib import Path

try:
    from faker import Faker
    import black
except ImportError as e:
    print(
        "Please install the faker and black modules first with the following commands:"
    )
    print("pip install faker black")
    exit(1)


class FakeStudentGenerator:
    scores = ["onvoldoende", "voldoende", "goed", "uitmuntend"]

    def __init__(
        self,
        number_classes,
        max_students_class,
        base_file="students_classrooms",
        class_prefix="SWDVT-",
    ):
        self.number_classes = number_classes
        self.number_students = max_students_class
        self.class_prefix = class_prefix
        self.base_file = base_file

    def generate_fake_file(self, write_as_python=True):
        classes = {}
        for i in range(self.number_classes):
            class_name = f"{self.class_prefix}1{string.ascii_uppercase[i]}"
            students = self.generate_fake_students(self.number_students)
            classes[class_name] = students
        if write_as_python:
            self.write_as_python_file(classes)
        else:
            self.write_as_json_file(classes)

    def write_as_python_file(self, students):
        filename = f"{self.base_file}.py"
        with open(filename, "w") as file:
            file.write(f"students_per_classroom = {students}")
        filepath = Path(filename)
        black.format_file_in_place(
            filepath, fast=True, write_back=black.WriteBack.YES, mode=black.FileMode()
        )
        print(f"File {filename} written")

    def write_as_json_file(self, students):
        with open(f"{self.base_file}.json", "w") as file:
            json.dump(students, indent=4, fp=file, default=str)
        print(f"File {self.base_file}.json written")

    def generate_fake_students(self, amount):
        students = []
        for i in range(amount):
            students.append(self.generate_fake_student())
        return students

    def generate_fake_student(self):
        student = {}
        student["naam"] = self.generate_fake_name()
        student["resultaten"] = self.generate_fake_results()
        return student

    def generate_fake_name(self):
        fake = Faker()
        return fake.name()

    def generate_fake_results(self):
        results = {}
        for i in range(4):
            results[f"WP{i+1}"] = random.choice(self.scores)
        return results


classroom_generator = FakeStudentGenerator(5, 30)
classroom_generator.generate_fake_file()
