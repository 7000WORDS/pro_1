class myClass:
    def __init__(self, name, age, job, planet, mission):
        self.name = name
        self.age = age
        self.job = job
        self.planet = planet
        self.mission = mission


name = input("Enter your name: ")
age = input("Enter your age: ")
job = input("Enter your job: ")
planet = input("Enter your planet: ")
mission = input("Enter your mission: ")

p1 = myClass(name, age, job, planet, mission)
print("Your name is " + p1.name)
print("You are " + p1.age + " years old")
print("You are working as " + p1.job)
print("You are from " + p1.planet)
print("You are currently working on the " + p1.mission + " mission")

answer = print("Is the information correct")
answer = input()
if answer == "no":
    print("ok, we will restart evrything")
elif answer == "yes":
    print("ok")

import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#%$#*&+=_-{}[]()<>?/|"

number = input("Number of passwords? - ")
number = int(number)

length = input("Password length? - ")
length = int(length)

for p in range(number):
    Password = " "
    for c in range(length):
        Password += random.choice(chars)
print(Password)

import string
from random import *
characters = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(characters) for x in range(randint(8, 16)))

Pass_word = " "
while Pass_word != password:
    print("enter password")
    Pass_word = input()

    if Pass_word == password:
        print("The password is the same")
    else:
        print("The password is wrong")
        print("The password = " + password)




import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Okwudili2009"
)

print(mydb)