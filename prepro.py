import os, os.path as path


class ProPreper:
    # Define primary variables
    def __init__(self):
        self.basedir = str(input('Enter project directory: '))
        self.refferal, self.reffered = os.listdir(self.basedir), os.listdir(self.basedir)
        self.no_of_folders = len(self.refferal)
        # this is just by the way
        self.file_names = ['project', 'Description']
        self.extensions = ['.py', '.txt']
        print('')
        os.chdir(self.basedir)
        print(os.getcwd())
        self.find_new_folder()

    # Detect when a new folder is created
    def find_new_folder(self):
        while True:
            list_folders = os.listdir()
            # Test for if there is a new folder
            if len(os.listdir()) > self.no_of_folders:
                # find that new folder
                for item in list_folders:
                    if item in self.refferal:
                        pass
                    else:
                        # Has found the new folder.
                       # Have a pop up tkinter window to enable developer input project details.
                        if item == "New folder":
                            pass
                        else:
                            print(f'New Project found: {item}')
                            # print('')
                            self.refferal.append(item)
                            # this should be equal to the tkinter entry
                            self.create_files_needed(item)
                            print(f"{item} has been successfully added ")
                            break
                        break

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

    # This method finds out if a file has been deleted and then removes it from index.
    def delete_deleted_project(self):
        pass

ProPreper()


# There can be a list of filenames and another list of file extentions from which the project names will be derived.
# {
# *************  POSSIBLE FUNCTIONALITIES  *************
# 1. User enters language of project and that languag's file is created
# 2. App will be part of startup windows applications
# 3. Functionality to monitor entire drives} #