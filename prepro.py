import os, os.path as path
import time

to_pass = ["venv", "env", "clone-env", "__pycache__", ".git",
           ".idea", "Styling Garlore", "globalenv", "Image files",
           "Lessons", "Other files", "None", "New folder"]

project_dir_list = [
        "F:/Works/__Name__Main/Python/Beginners_Level",
        "F:/Works/__Name__Main/Python/Intermediate_Level",
        "F:/Works/__Name__Main/Python/Advanced_Level",
        "F:/Works/__Professional",
        "F:/Works/Final-Year-Project"
    ]


class ProPreper:
    # Define primary variables
    def __init__(self):
        for self.basedir in project_dir_list:
            self.basedir.replace("\ ", "/")
            # time.sleep(2.5)
        # Scan currently active directory and save to list
            self.definite = os.listdir(self.basedir)
            self.no_of_folders = len(self.definite)
            # this is just by the way
            print('')
            os.chdir(self.basedir)
            print("Currently working @: ", os.getcwd())
            time.sleep(2.3)
            self.find_new_folder()

    # Detect when a new folder is created
    def find_new_folder(self):
        if self.no_of_folders != len(os.listdir()):
        # while True:
            list_folders = os.listdir()
            # Test for if there is a new folder
            if len(os.listdir()) > self.no_of_folders:
                # find that new folder
                for item in list_folders:
                    if item in self.definite:
                        pass
                    else:
                        # Has found the new folder.
                        # Have a pop up tkinter window to enable developer input project details.
                        if item in to_pass:
                            pass
                        else:
                            print(f'New Project found: {item}')
                            # # print('')
                            # self.definite.append(item)
                            # # this should be equal to the tkinter entry
                            # self.create_files_needed(item)
                            # print(f"{item} has been successfully added ")
                            # self.no_of_folders += 1
            #   From here test if there is a deleted project and call respective function
            return 0
            # elif self.no_of_folders > len(os.listdir()):
            #     self.delete_deleted_project()

    # Create all files neded for the project
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
        os.chdir(self.basedir)
        print(f'Returned to {os.getcwd()}')
        return 0

    # This method finds out if a file has been deleted and then refreshes project index.
    def delete_deleted_project(self):
        if len(self.definite) != len(os.listdir()):
            # Test for a missing folder
            if len(os.listdir()) < self.no_of_folders:
                time.sleep(0.1)
                no_of_removed_projects = self.no_of_folders - len(os.listdir())
                print(f"Number of projects removed: {no_of_removed_projects}")
                print("Refreshing project index")
                # ProPreper(self.basedir)
            else:
                pass


while True:
    ProPreper()
    time.sleep(2.3)

# There can be a list of filenames and another list of file extentions from which the project files will be derived.
# *************  POSSIBLE FUNCTIONALITIES  *************
# 1. User enters language of project and that languag's file is created 
# 2. App will be part of startup windows applications
# 3. Functionality to monitor entire project directories}  (Applied) #






# What to do
# Set the app to move through all derectories and scan them all to find if there is an added folder or a deleted folder