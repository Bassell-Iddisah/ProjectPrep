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
    def __init__(self, basedir):
        self.initial_scan = os.listdir(basedir)
        self.no_of_folders = len(self.initial_scan)
        # this is just by the way
        print('')
        os.chdir(basedir)
        print(os.getcwd())
        self.find_new_folder(basedir)

    # Detect when a new folder is created
    def find_new_folder(self, basedir):
        while True:
            # Test for if there is a new folder
            if len(os.listdir()) > self.no_of_folders:
                # find that new folder
                for item in os.listdir():
                    if item in self.initial_scan:
                        pass
                    else:
                        # Has found the new folder.
                        # Have a pop up tkinter window to enable developer input project details.
                        if item == "New folder":
                            pass
                        else:
                            print(f'New Project found: {item}')
                            # print('')
                            # self.initial_scan.append(item)
                            # this should be equal to the tkinter entry
                            # self.create_files_needed(item, basedir)
                            print(f"{item} has been successfully added ")
                            # self.no_of_folders += 1
                            break
                        break
            else:
                print('No new thing')
            time.sleep(2)
            # elif self.no_of_folders > len(os.listdir()):
            #     self.delete_deleted_project()
    # # Create all files neded for the project
    # def create_files_needed(self, item, basedir):
    #     # Take description of the project
    #     description = str(input('What is this project supposed to do?: '))
    #     # Must take final input from tkinter GUI
    #     # Creating new file path
    #     os.chdir(item)
    #     name_list = [item, 'Description']
    #     ext_list = ['py', 'txt']
    #
    #     for filename, extension in zip(name_list, ext_list):
    #         creation_path = path.join(os.getcwd(), f'{filename}.{extension}')
    #         with open(creation_path, 'w') as file:
    #             file.write('')
    #         with open('Description.txt', 'w') as file:
    #             file.write(description)
    #     os.chdir(basedir)
    #     print(f'Returned to {os.getcwd()}')
    #     return 0
    #
    # # This method finds out if a file has been deleted and then refreshes project index.
    # def delete_deleted_project(self):
    #     while True:
    #         # Test for a missing folder
    #         if len(os.listdir()) < self.no_of_folders:
    #             time.sleep(0.1)
    #             no_of_removed_projects = self.no_of_folders - len(os.listdir())
    #             print(f"Number of projects removed: {no_of_removed_projects}")
    #             print("Refreshing project index")
    #             ProPreper(basedir)
    #         else:
    #             pass


for basedir in project_dir_list:
    ProPreper(basedir.replace('\ ', '/'))

# There can be a list of filenames and another list of file extentions from which the project files will be derived.
# *************  POSSIBLE FUNCTIONALITIES  *************
# 1. User enters language of project and that languag's file is created 
# 2. App will be part of startup windows applications
# 3. Functionality to monitor entire project directories}  (Applied) #






# What to do
# Set the app to move through all derectories and scan them all to find if there is an added folder or a deleted folder