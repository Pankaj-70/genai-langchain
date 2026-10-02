#'\n\n', '\n', '_', '.'

from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
My name is Rahul.
I am 20 years old.

Go to Mumbai, marine drive.
The pawan there is astonishing enough to stupefy your thoughts.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0
)

result = splitter.split_text(text)

print(result)