from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def get_gender(self):
        pass


class Male(Person):
    def get_gender(self):
        return "Male"


class Female(Person):
    def get_gender(self):
        return "Female"


try:
    person = Person()  
except Exception as e:
    print(e)


male = Male()
female = Female()

print(male.get_gender())  
print(female.get_gender())  
