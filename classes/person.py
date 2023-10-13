from abc import ABC, abstractclassmethod

class Person(ABC):
    def __init__(self, name, age, password, role):
        self.name = name
        self.age = age
        self.password = password
        self.role = role

    @abstractclassmethod
    def all_members(self):
        pass