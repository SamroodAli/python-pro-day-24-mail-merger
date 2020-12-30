"""Main project file"""
with open("../Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("../Input/Letters/starting_letter.docx") as starting_letter:
    content = starting_letter.read()
