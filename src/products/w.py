


from tkinter import N
from urllib.request import AbstractDigestAuthHandler


class Model1():
    name = 'name'
    text = 'text'

class Model2():
    name = 'name2'
    text = 'text'
    

names = Model1.name,Model2.name

for n in names:
    print(n)
    

