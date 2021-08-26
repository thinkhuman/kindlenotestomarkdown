# A utility to convert saved notes from Kindle books (HTML) to markdown.
# Note headings (page number references) are contained in the 'noteHeading' class.
# The notes are contained in the 'noteText' class. This is what we want.

# Use the BeautifulSoup library to parse the html
from bs4 import BeautifulSoup

# Use pathlib to verify if the input file exists
import pathlib

notes = [] # A list to hold each note

# Get an input file to parse, and make sure it exists
while True:
    input_file = input("Please enter a file name: ")
    path = pathlib.Path(input_file)

    # Make sure the input file exists
    if path.is_file():
        break
    else:
        print("Sorry, that file doesn't exist.")
        continue

# Open an html file to parse
with open(input_file) as htmlnotes:
#     # parse the file
    soup = BeautifulSoup(htmlnotes, 'html.parser')
#     # grab (only) the note text
    for note in soup.find_all("div", class_="noteText"):
        notes.append(note.get_text())
    print("HTML file successfully converted to markdown.")

# Specify an output file name.
while True:
    output_file = input("Please enter a file name to save the results: ")
    path = pathlib.Path(output_file)

    # Make sure the output file doesn't already exist
    if path.is_file():
        print("Sorry, that file already exists.")
        continue
    else:
        break


# Save the parsed text to a file as a markdown list.
with open(output_file, 'a', newline='') as markdown:
    for note in notes:
        markdown.write("\n* " + note.strip() + '\n')

