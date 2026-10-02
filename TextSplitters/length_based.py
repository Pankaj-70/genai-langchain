from langchain_text_splitters import CharacterTextSplitter

text = """
Over Saudi Arabia, the crew and passengers of Flydubai Flight 1073 (aircraft pictured) avert an attempt to hijack or crash the aircraft.
Flooding in Bangkok and across Thailand leaves at least 23 people dead.
Fatima Ezzahra El Mansouri is appointed the first woman prime minister of Morocco after her party's victory in the general election.
The Chess Olympiad concludes with Uzbekistan winning the Open event and China winning the Women's event.
"""

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_text(text)

print(result)