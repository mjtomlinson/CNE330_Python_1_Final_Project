# Matt Tomlinson - Student
# CNE330 Python1
# 6/19/2021
# Source code from: https://data-flair.training/blogs/python-mad-libs-generator-game/ (and)\
# https://github.com/kforti/python_projects (and)
# https://pythonguides.com/python-tkinter-optionmenu/
# Justin Ellis - Instructor
# Final Project-MadLibs Generator
###############################

# import module###########
from tkinter import *
from tkterminal import Terminal
# from PIL import ImageTk,Image
import json
import os

# initialize window##################

# button Tk()###################

# root = Tk()
# root.geometry('600x600')
# root.title('Final Project-Mad Libs Generator')
# Label(root, text='Mad Libs Generator \n Have Fun!', font='arial 20 bold').pack()
# Label(root, text='Click Any One :', font='arial 15 bold').place(x=40, y=80)


# dropdown Tk()
root = Tk()
root.title('Final Project-Mad Libs Generator')
Label(root, text='Mad Libs Generator \n Have Fun!', font='arial 20 bold').pack()
Label(root, text='Click Any One :', font='arial 15 bold').place(x=40, y=80)
root.geometry('400x800')
# BG image set
img = PhotoImage(file='C:\Users\sinsu\PycharmProjects\pythonProject1\Images\Title Page.png')
label = Label(
    root,
    image=img
)
# noinspection SpellCheckingInspection
root.config(bg="#F9EBEA")
ws = tk.Tk()
terminal = Terminal(pady=10, padx=10)
terminal.shell = True
terminal.pack(expand=True, fill='both')


def display_selected(choice):
    choice = variable.get()
    print(choice)


Templates = ['A Day At the Zoo', 'Celebrity_apple_Orchard_Vacation', 'Birthday_Photos',
             'The Famous Butterfly Dream', 'Little_Red_Riding_Hood']

# setting variable for Integers
variable = StringVar()
variable.set(Templates[4])

# creating widget
dropdown = OptionMenu(
    root,
    variable,
    *Templates,
    command=display_selected
)

# positioning widget
dropdown.pack(expand=True)

root.mainloop()


# class
class MadLibs:
    path = "./templates"

    def __init__(self, word_descriptions, template):
        self.template = template
        self.word_descriptions = word_descriptions
        self.user_input = []
        self.story = None

    @classmethod
    def from_json(cls, name, path=None):
        if not path:
            path = cls.path
        fpath = os.path.join(path, name)
        with open(fpath, "r") as f:
            data = json.load(f)
        mad_lib = cls(**data)
        return mad_lib

    def get_words_from_user(self):
        print("Please provide the following words: ")
        for desc in self.word_descriptions:
            ui = input(desc + " ")
            self.user_input.append(ui)
        return self.user_input

    def build_story(self):
        self.story = self.template.format(*self.user_input)
        return self.story

    def show_story(self):
        print(story)


# Drop Down Menu
# def display_selected(choice):
#   choice = variable.get()
#   print(choice)


def select_template():
    print("Select a Mad Lib from the following list: \n field can not be blank")
    templates = os.listdir(MadLibs.path)
    template = input(str(templates) + " ")
    try:
        return template
    except NotImplementedError:
        print("field can not be blank")
    finally:
        return template


# variables
choice = select_template()
# temp_name = select_template()
# temp_name = "day_at_the_zoo.json"
# mad_lib = MadLibs.from_json(temp_name)
mad_lib = MadLibs.from_json(choice)
words = mad_lib.get_words_from_user()
story = mad_lib.build_story()
mad_lib.show_story()

# buttons
# Button(root, text='A Day At the Zoo', font='arial 15', command=select_template(), bg='ghost white').place(y=20, x=20)
# Button(root, text='Celebrity_apple_Orchard_Vacation', font='arial 15', command=select_template(), bg='ghost white').place(y=20, x=40)
# Button(root, text='Birthday_Photos', font='arial 15', command=select_template(), bg='ghost white').place(y=20, x=60)
# Button(root, text='The Famous Butterfly Dream', font='arial 15', command=select_template(), bg='ghost white').place(y=40, x=20)
# Button(root, text='Little_Red_Riding_Hood', font='arial 15', command=select_template(), bg='ghost white').place(y=40, x=60)


# infinite loop
# root.mainloop()
