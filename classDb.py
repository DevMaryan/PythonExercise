import json
import sqlite3

employees = []

con = sqlite3.Connection('Employees.db')
c = con.cursor()

class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def GetInfo():
    name = input('Enter your name: ')
    age = input('Enter your age: ')
    newEmp = Employee(name, age)
    employees.append(newEmp)
    return newEmp

def Welcome():
    info = GetInfo()
    print("Welcome to " + info.name + " " + info.age)

def JsonToFile(jsonEmps):
    with open('employees.txt','a') as outfile:  # a - append, w - overwrite existing content
        json.dump(jsonEmps, outfile)

def Result():
    for em in employees:
        print("New Employees: " + em.name + " " + em.age)
    jsonEmployees = json.dumps(employees, default=vars)
    print(jsonEmployees) # print in json format new employees
    JsonToFile(jsonEmployees) # write into file format new employees
    Repository(em) # write into Database new employees

def Repository(em):
    try:
        query = ("INSERT INTO Employee(Name,Age) VALUES (?, ?)")
        data_tuple = (em.name, em.age)
        c.execute(query, data_tuple)
        con.commit()
    except sqlite3.Error as e:
        print(e)

i = True

while i:
    Welcome()
    ask = input("Would you like to continue? No or press Enter ")
    if ask == "No":
        Result()
        i = False

    
def AllEmployees():
        try:
        query = ("SELECT * FROM Employee")
        c.execute(query)
        rows = c.fetchall()
        
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)
