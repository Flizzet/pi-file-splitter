"""
# File splitter application
# Splits files into defined amount of characters each.
# Searches for files based on their contents.
#
# By Pedro Dutra (2017)
# http://www.flizzet.com/
"""

import os
import string
from os import listdir
from os.path import isfile, join
from enum import IntEnum


def main():

    unwanted_chars = "=+<>"
    """
    INITIATION STATE
    # Asks the user which of the functions they'd like to use.
    """
    class Mode(IntEnum):
        SPLITTING = 1
        MATCHING = 2
        EXIT = 3

    print("---")
    print("Enter the number corresponding to the feature you'd like to use.")
    print("Splitting mode - \"1\"")
    print("Matching mode - \"2\"")
    print("Exit - \"3\"")


    def chooseMode():
        chosen_mode = input("Enter mode choice: ")
        if chosen_mode == "1" or chosen_mode == "2" or chosen_mode == "3":
            if chosen_mode == "3": print("Exiting.")
            else: print("Mode chosen.")
        else:
            print("That's not one of the numbered modes! Please try again.")
            chosen_mode = chooseMode()
        return chosen_mode


    mode_choice = chooseMode()


    # Entering splitting mode
    if mode_choice == "1":
        print("FILE SPLITTING MODE CHOSEN")
        """
        SPLITTING STATE
        # Splits files into multiple "mini" files based on user defined number of characters.
        """
        # Finds a file and makes sure it exists
        def findfile(path):
            newpath = path
            try:
                open(path, "r")
            except IOError:
                newpath = findfile(input("That file doesn't appear to exist. Try again:\n"))
            return newpath


        # Ask the user which file they're splitting
        path = findfile(input("Where's the file you'd like to split?:\n"))
        print("File found!\n")


        # Ask the user how many characters they'd like in each file
        NUM_CHARS = int(input("How many characters per file?:\n"))
        current_file = 0
        current_char = 0
        total_chars = 0
        with open(path) as fileobj:
            if not os.path.exists(path + "minis/"):
                os.makedirs(path + "minis/")
            fout = open(path + "minis/mini_0.txt", "wb")
            for line in fileobj:
                for char in unwanted_chars:
                    line = line.replace(char, '')

                for ch in line:
                   total_chars = total_chars + 1
                   current_char = current_char + 1
                   fout.write(ch.encode())
                   if total_chars % NUM_CHARS == 0:
                       current_file = current_file + 1;
                       fout = open(path + "minis/mini_%d.txt" %current_file, "wb")
            fout.close()

        print("Files split.")


    # Entering matching mode
    if mode_choice == "2":
        print("FILE MATCHING MODE CHOSEN")
        # Checks if a folder exists or not
        def doesFolderExist(folder_path):
            folder_to_be_searched = folder_path

            # If the folder doesn't exist, ask for it again
            if not os.path.exists(folder_path):
                folder_to_be_searched = doesFolderExist(input("That folder doesn't appear to exist. Please try again:\n"))


            return folder_to_be_searched

        # Get user inputted folder to be searched
        folder = doesFolderExist(input("Please enter the location of the folder you would like to search:\n"))
        # Create a list of all the files in the folder
        all_files = [f for f in listdir(folder) if isfile(join(folder, f))]

        # Clear the terminal for easy memorization
        os.system('cls' if os.name == 'nt' else 'clear')


        # Check if the text inputted by user corresponds to the text of any of the files
        def checkContent(user_text):
            file_found = False
            matching_file = None
            for file in all_files:
                with open(folder + "/" + file, 'r') as content_file:
                    if user_text == content_file.read():
                        file_found = True
                        matching_file = content_file
            if file_found:
                print("File found! It's " + matching_file.name)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("File not found!")
                main()

        # Ask the user to type out the full text of the file
        checkContent(input(""))

    # Complete application, ask if they'd like to rerun
    rerun = input("Would you like to rerun in a new mode? (Y/N)\n")
    if rerun.capitalize() == "Y" or rerun.capitalize() == "Yes" or rerun.capitalize() == "YES":
        main()
    else:
        return

main()