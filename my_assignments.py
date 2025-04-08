name = "Fatih Murat"
age = 20
print(name) #Fatih Murat
print(age) #20
print(type(name)) # <class 'str'>
print (type(age)) # <class 'int'>

x = 10 
if x > 5:
     print("x is greater than 5")
     
     



fruits = ["apple", "banana", "cherry", "mango"]

for fruit in fruits:
    print(fruit)


student = {
     "name": "Fatih",
     "age": 20,
     "grade": "A",
}

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
