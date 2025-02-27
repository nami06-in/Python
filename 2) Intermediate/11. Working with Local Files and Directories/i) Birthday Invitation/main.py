"""
    In a new terminal type -> pip install python-dotenv
    create a .env file and mention the path for the following-
        - invited_names.txt
        - starting_letter.txt
        - ReasyToSend folder 
    And store these path as-
        - NAMES_FILE_PATH
        - STARTING_LETTER_PATH
        - OUTPUT_BASE_PATH

"""

import os
from dotenv import load_dotenv

load_dotenv()

BASE_PATH = os.getenv("OUTPUT_BASE_PATH")

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"

with open(os.getenv("NAMES_FILE_PATH")) as names_file:
    names = names_file.readlines()

with open(os.getenv("STARTING_LETTER_PATH")) as letter_file:
    letter_content = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        
        OUTPUT_LETTER_PATH = f"{BASE_PATH}/letter_for_{stripped_name}.txt"
        with open(OUTPUT_LETTER_PATH, "w") as completed_letter:
            completed_letter.write(new_letter)
