# Online Python - IDE, Editor, Compiler, Interpreter
#character input
import datetime

name = input("What is your name? ")
age = int(input("What is your age? "))
year_100 = 100 - age + datetime.datetime.now().year
print(f"Hello, {name}! You will turn 100 in the year {year_100}.")
