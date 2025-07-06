import random
from faker import Faker

from src.model.student import Student

fake = Faker()

class StudentUpdateBuilder:
    def __init__(self, original: Student):
        self.original = original
        self.updated = self._generate_updated_student()

    def _generate_updated_student(self) -> Student:
        # Меняем first_name
        while True:
            first_name = fake.first_name()
            if first_name != self.original.first_name:
                break

        # Меняем last_name
        while True:
            last_name = fake.last_name()
            if last_name != self.original.last_name:
                break

        # Меняем age
        while True:
            age = random.randint(18, 30)
            if age != self.original.age:
                break

        # Меняем email
        while True:
            email = fake.email()
            if email != self.original.email:
                break

        # Меняем major
        majors = ["Computer Science", "Data Science", "Math", "Physics"]
        majors = [m for m in majors if m != self.original.major]
        major = random.choice(majors)

        # Инвертируем enrolled
        enrolled = not self.original.enrolled

        return Student(
            first_name=first_name,
            last_name=last_name,
            age=age,
            email=email,
            enrolled=enrolled,
            major=major
        )

    def build(self) -> Student:
        return self.updated

    def to_dict(self) -> dict:
        return self.updated.to_dict()