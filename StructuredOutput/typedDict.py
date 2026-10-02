from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person : Person = {'name': 'Pankaj',  'age': 23} #even if age = '23' it will compile
print(new_person)