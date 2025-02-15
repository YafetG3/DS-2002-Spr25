#!C:\Users\yafet\miniconda3\python.exe

import os

FAV_SPORT = input("What is your favorite sport? ")
FAV_COLOR = input("What is your favorite color? ")
HOME_TOWN = input("What is your hometown? ")

os.environ["FAV_SPORT"] = FAV_SPORT
os.environ["FAV_COLOR"] = FAV_COLOR
os.environ["HOME_TOWN"] = HOME_TOWN

print(os.getenv("FAV_SPORT"))
print(os.getenv("FAV_COLOR"))
print(os.getenv("HOME_TOWN"))
