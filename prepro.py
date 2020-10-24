import os, os.path as path
import time

to_pass = ["venv", "env", "clone-env", "__pycache__", ".git",
           ".idea", "Styling Garlore", "globalenv", "Image files",
           "Lessons", "Other files", "None", "none", "New folder"]

dir_list = ["F:/Works/__Name__Main/Python/Beginners_Level",
            "F:/Works/__Name__Main/Python/Advanced_Level",
            "F:/Works/__Name__Main/Python/Intermediate_Level",
            "F:/Works/__Professional",
            "F:/Works/Final-Year-Project"]


class ProPreper():
    # Define primary variables
    def __init__(self, basedir):
        self.refferal, self.reffered = os.listdir(basedir), os.listdir(basedir)
        self.no_of_folders = len(self.refferal)
        # this is just by the way
        self.file_names = ['project', 'Description']
        self.extensions = ['.py', '.txt']
        self.deleted = []
        print('')
        os.chdir(basedir)
        print(os.getcwd())
        print()
        self.find_new_folder()

    # Detect when a new folder is created
    def find_new_folder(self):
        if len(self.refferal) != len(os.listdir()):
            while len(self.refferal) != len(os.listdir()):
                print("method: find_new_folder")
                list_folders = os.listdir()
                # New folder found
                if len(os.listdir()) > self.no_of_folders:
                    # Identify new folder
                    for item in list_folders:
                        if item in self.refferal:
                            pass
                        else:
                            # Has found the new folder.
                            # Have a pop up tkinter window to enable developer input project details.
                            if item in to_pass:
                                pass
                            else:
                                print(f'New Project found: {item}')
                                print()
                                self.refferal.append(item)
                                # this should be equal to the tkinter entry
                                self.create_files_needed(item, basedir)
                                print(f"{item} has been successfully added ")
                                print()
                                self.no_of_folders += 1
                                break
                            break
                # elif self.no_of_folders > len(os.listdir()):
                #     self.delete_deleted_project()
                else:
                    self.delete_deleted_project()
        else:
            self.delete_deleted_project()

    # Create all files needed for the project
    def create_files_needed(self, item, basedir):
        print("method: create_files_needed")
        # Take description of the project
        description = str(input('What is this project supposed to do?: '))
        print()
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
        os.chdir(basedir)
        print(f'Returned to {os.getcwd()}')
        print()
        return 0

    # This method finds out if a file has been deleted and then refreshes project index.
    def delete_deleted_project(self):
        print("method: delete_deleted_project")
        deleted = []
        while len(self.refferal) != len(os.listdir()):
            # Test for a missing folder
            if len(os.listdir()) < self.no_of_folders:
                time.sleep(0.1)
                no_of_removed_projects = self.no_of_folders - len(os.listdir())
                print(f"Projects removed: {no_of_removed_projects}")
                print()
                for project in os.listdir():
                    if project in self.refferal:
                        pass
                    else:
                        deleted.append(str(project))
                print(f"list of deleted projects;")
                print()
                for deleted_projects in deleted:
                    print(deleted_projects)
                print("Refreshing project index")
                print()
                return 0
            else:
                return 0


while True:
    for basedir in dir_list:
        ProPreper(basedir)
        time.sleep(3)


# There can be a list of filenames and another list of file extentions from which the project files will be derived.
# *************  POSSIBLE FUNCTIONALITIES  *************
# 1. User enters language of project and that languag's file is created 
# 2. App will be part of startup windows applications
# 3. Functionality to monitor entire project directories}  (Applied) #
