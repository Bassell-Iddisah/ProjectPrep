import time
import os, os.path as path
from tkinter import *

file_name_dic= {
    'flask_files': ["app", "routes", "forms", "models", "__init__", "config", "Details"]
}
file_exts_dic= {

    'flask_exts': [".py", ".html"]
}

class ProPreper:
    def __init__(self):
        # Set the variable needed
        #     variables for setting up project folder
        # self.basedir = str(input('Enter directory: '))
        # self.project_name = str(input('Enter the name of your project: '))
        # self.description = str(input('Enter project description: '))
        # #   variables for setting up project files
        # self.file_names = ['Details', self.project_name]
        # self.extensions = ['.txt', '.py']
        # #   variables will be used for testing
        # os.chdir(self.basedir)
        # print('Current Working Directory: ', os.getcwd())
        self.list_of_folders = []
        self.no_of_folders = len(self.list_of_folders)
        self.description = ''
        print('')

        self.create_project_folder()

    # def find_new_folder(self):
    #     while True:
    #         list_folders = os.listdir()
    #         # Test for if there is a new folder
    #         if len(os.listdir()) > self.no_of_folders:
    #             # find that new folder
    #             for item in list_folders:
    #                 if item in self.list_of_folders:
    #                     pass
    #                 else:
    #                     time.sleep(3)
    #                     # Has found the new folder.
    #                    # Have a pop up tkinter window to enable developer input project details.
    #                     if item == "New Folder":
    #                         # os.rename(item, self.project_name)
    #                         print(f'New Project found: {item}')
    #                         print('')
    #                         self.list_of_folders.append(item)
    #                         # this should be equal to the tkinter entry
    #                         description = str(input('Enter the description of this coming project: '))
    #                         self.create_files_needed(item, description)
    #                         print(f"{item} has been successfully added ")
    #                         break



    # def create_project_folder(self):
    #     # Creating the project folder
    #     if self.project_name in os.listdir():
    #         self.project_name = str(input('folder already exists, please give a new name: '))
    #         self.create_files_needed(self.description)
    #     else:
    #         os.mkdir(path.join(self.basedir, self.project_name))
    # #     Move into project dir and create all the files needed
    #     os.chdir(self.project_name)
    #     print(os.getcwd())
    #     self.create_files_needed(self.description)
    #     return 0

    # def create_files_needed(self, description):
    #     # Creating new file path
    #     for files, extensions in zip(self.file_names, self.extensions):
    #         new_path = path.join(os.getcwd(), files+extensions)
    #         # Creating the new files
    #         with open(new_path, 'w') as file:
    #             file.write(f'{description}')
    #         with open(new_path, 'w') as file:
    #             file.write(f"{description}")
    #     os.chdir(self.basedir)
    #     print(os.getcwd())
    #     return 0

    # This method finds out if a file has been deleted and then removes it from index.
    # def take_away_form_indexing(self):
    #     # first detect and locate deleted file by filename
    #     pass


ProPreper().collect_details()


# There can be a list of filenames and another list of file extentions from which the project names will be derived.
# {
# *************  POSSIBLE FUNCTIONALITIES  *************
# 1. User enters language of project and that languag's file is created
# 2. App will be part of startup windows applications
# 3. Functionality to monitor entire drives} #