#importing teacher_details module from Teacher package 
#from is used with package, import is used with modules
#generic use from whwnever we wat to import something from modules/packages,
import os, sys 
#os provide functions to interact with operating system
#sys provide access to system specific parameters and functions such as pyton path
from os.path import dirname, abspath, join
#__file__ >> give the path of current script, examples : This Script is at c:\Users\Pritam\Desktop\Data Analyst Resources\Python\Data_Analytics\data and file handling\Course\Student\student_details.py
#dirname >> give the directory of the script, examples : This Script is at c:\Users\Pritam\Desktop\Data Analyst Resources\Python\Data_Analytics\data and file handling\Course\Student
#join >> join to or more paths, inseting '/' as needed
#join(dirname( __file__), "..") >> move one directory up from the current script directory
#abspath( join(dirname( __file__), "..")) >> abspath coverts the relative path to absolute path
parent_dir_path = abspath( join(dirname( __file__), ".."))
sys.path.insert(0, parent_dir_path)
#at index 0, add this directory to the beginning of module search/syatem path
#it allows to search modules and packages

#from Teacher import teacher_details

def student():
    print("This is a student details")

#teacher_details.teacher()