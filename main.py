"""Main project file"""

PLACEHOLDER = "[name]"
with open("Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("Input/Letters/starting_letter.docx") as starting_letter:
    sample_content = starting_letter.read()
    for name in names_list:
        name = name.replace("\n", "")
        stripped_name = name.strip()
        with open(f"Output/ReadyToSend/letter_for_{name}.docx", mode="w") as letter:
            letter_content = sample_content.replace(PLACEHOLDER, stripped_name)
            letter.write(letter_content)
