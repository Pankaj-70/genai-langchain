from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
class Dog:
    # Class attribute
    species = "Canine"

    # Constructor
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Method
    def bark(self):
        return f"{self.name} says woof!"

# Creating an object (instance)
my_dog = Dog("Buddy", 3)
print(my_dog.bark())  # Output: Buddy says woof!   
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=0
)

result = splitter.split_text(text)

print(result)