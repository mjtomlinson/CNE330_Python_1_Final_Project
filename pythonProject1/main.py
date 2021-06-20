# Matt Tomlinson - Student
# CNE330 Python1
# 6/19/2021
# Source code from: https://data-flair.training/blogs/python-mad-libs-generator-game/ (and)\
# https://github.com/kforti/python_projects
# Justin Ellis - Instructor
# Final Project-MadLibs Generator

# import module
from tkinter import *
import json
import os

# initialize window
root = Tk()
root.geometry('600x600')
root.title('Final Project-Mad Libs Generator')
Label(root, text='Mad Libs Generator \n Have Fun!', font='arial 20 bold').pack()
Label(root, text='Click Any One :', font='arial 15 bold').place(x=40, y=80)


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


def select_template():
    print("Select a Mad Lib from the following list:")
    templates = os.listdir(MadLibs.path)
    template = input(str(templates) + " ")
    return template


temp_name = select_template()
# temp_name = "day_at_the_zoo.json"
mad_lib = MadLibs.from_json(temp_name)
words = mad_lib.get_words_from_user()
story = mad_lib.build_story()
mad_lib.show_story()

# buttons
Button(root, text='A Day At the Zoo', font='arial 15', command=select_template, bg='ghost white').place(x=60, y=120)
Button(root, text='apple and apple', font='arial 15', command=mad_lib, bg='ghost white').place(x=70, y=180)
Button(root, text='The Butterfly', font='arial 15', command=temp_name, bg='ghost white').place(x=80, y=240)

root.mainloop()
