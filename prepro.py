import time
import os, os.path as path
from tkinter import *


class ProPreper:
    def __init__(self):
        self.basedir = str(input('Enter project directory: '))
        self.list_of_folders = list(os.listdir(self.basedir))
        self.no_of_folders = len(self.list_of_folders)

        # this is just by the way
        self.file_names = ['project', 'Description']
        self.extensions = ['.py', '.txt']
        print('')
        os.chdir(self.basedir)
        self.find_new_folder()

    def find_new_folder(self):
        while True:
            list_folders = os.listdir()
            # Test for if there is a new folder
            if len(os.listdir()) > self.no_of_folders:
                # find that new folder
                for item in list_folders:
                    if item in self.list_of_folders:
                        pass
                    else:
                        # Has found the new folder.
                       # Have a pop up tkinter window to enable developer input project details.
                        if item == "New folder":
                            pass
                        else:
                            print(f'New Project found: {item}')
                            # print('')
                            self.list_of_folders.append(item)
                            # this should be equal to the tkinter entry
                            self.create_files_needed(item)
                            print(f"{item} has been successfully added ")
                            break
                        break


    def create_files_needed(self, item):
        # Take description of the project
        description = str(input('What is this project supposed to do?: '))
        # Must take final input from tkinter GUI
        # Creating new file path
        os.chdir(item)
        name_list = [item, 'Description']
        ext_list = ['py', 'txt']

        for filename, extension in zip(name_list, ext_list):
            creation_path = path.join(os.getcwd(), f'{filename}.{extension}')
            with open(creation_path, 'w') as file:
                file.write('')
            with open('Description.txt', 'w') as file:
                file.write(description)


        # for files, extensions in zip(self.file_names, self.extensions):
        #     new_path = path.join(os.getcwd(), files+extensions)
        #     # Creating the new files
        #     with open(new_path, 'w') as file:
        #         file.write('')
        #     with open(new_path, 'w') as file:
        #         file.write(f"{description}")
        os.chdir(self.basedir)
        print(f'Returned to {os.getcwd()}')
        return 0

    # This method finds out if a file has been deleted and then removes it from index.
    def take_away_form_indexing(self):
        # first detect and locate deleted file by filename
        pass


ProPreper()


# There can be a list of filenames and another list of file extentions from which the project names will be derived.
# {
# *************  POSSIBLE FUNCTIONALITIES  *************
# 1. User enters language of project and that languag's file is created
# 2. App will be part of startup windows applications
# 3. Functionality to monitor entire drives} #