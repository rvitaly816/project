from faker import Faker
import random
from src.model.student import Student

fake = Faker()

class StudentBuilder:
    def __init__(self):
        self._student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=random.randint(18, 30),
            email=fake.email(),
            enrolled=True,
            major="Computer Science"
        )

    def with_first_name(self, first_name: str):
        self._student.first_name = first_name
        return self

    def with_last_name(self, last_name: str):
        self._student.last_name = last_name
        return self

    def with_age(self, age: int):
        self._student.age = age
        return self

    def with_email(self, email: str):
        self._student.email = email
        return self

    def with_enrolled(self, enrolled: bool):
        self._student.enrolled = enrolled
        return self

    def with_major(self, major: str):
        self._student.major = major
        return self

    def build(self) -> Student:
        return self._student