class Student:
    first_name: str
    last_name: str
    age: int
    email: str
    enrolled: bool
    major: str

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 age: int,
                 email: str,
                 enrolled: bool,
                 major: str,

    ):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._email = email
        self._enrolled = enrolled
        self._major = major




    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise ValueError("First name must be a string.")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Last name must be a string.")
        self._last_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("Age must be a integer.")
        self._age = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise ValueError("Email must be a string.")
        self._email = value

    @property
    def enrolled(self):
        return self._enrolled

    @enrolled.setter
    def enrolled(self, value):
        if not isinstance(value, bool):
            raise ValueError("Enrolled must be a boolean.")
        self._enrolled = value

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, value):
        if not isinstance(value, str):
            raise ValueError("Major must be a string.")
        self._major = value


    def to_dict(self):
        return {
            "first_name": self._first_name,
            "last_name": self._last_name,
            "age": self._age,
            "email": self._email,
            "enrolled": self._enrolled,
            "major": self._major
        }