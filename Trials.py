from tkinter import *
root = Tk()
root.title('New Project Detected')
root.geometry('500x500')


def printing():
    print('hello world')


def collect_details():
    # def all widgets to be used
    title = Label(root, text="Enter Project Details")
    name_label = Label(root, text='Project Name:')
    project_name = Entry(root, width=30)
    description = Label(root, text='What is the project supposed to do?:')
    E_description = Entry(root, width=30)
    packages_list = Listbox(root, selectmode='single', yscrollcommand='scrollable')
    submit = Button(root, text='Create Project')

    # Pack all def widgets
    title.grid()
    name_label.grid(column=0, row=5, sticky=W)
    # project_name.pack()
    # description.grid()
    # E_description.grid()
    # packages_list.grid()
    # submit.grid()


collect_details()
root.mainloop()