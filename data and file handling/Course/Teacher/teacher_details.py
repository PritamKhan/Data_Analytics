# >Why the need of creating different script for student and teacher?

# To maintain the code, to improve understanding of code.
# Best practice is to keep different component in different  scripts.

# Example: Model training and EDA should be in different scripts.

# >Modules: It is a single file with.py extension that contains python code.
# Insise module functions, class, variables or some  python codes.

# Example : student_detalis.py and teacher_details.py are modules.

# >Package: It is collection of modules organised in directories.
# Each directory can have multiple python scripts.

# Example: Student and teacher folder is packages.

# >Versions before python 3.3, to make a package it eas nessary to include __init__.py in package to initialise package and expose required modules  and functions. >> not required any more.


# >Library: It is colection of multiple packages and modules, Pre-define code to perform common task.

# Example: numpy, pandas

#__pycache__  aslo known as pyt files:These are compiled python files >> source code is compiled into python bytecode >> stored in.pyc file inside __pycache__ directory.
#this hlep to load the code faster next time when it is imported. 

import os, sys
from os.path import dirname, abspath, join

parent_dir_path = abspath( join(dirname( __file__), ".."))
sys.path.insert(0, parent_dir_path)

from Student import student_details

def teacher():
    print("This is teacher details")


student_details.student()

