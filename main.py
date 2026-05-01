class Transport:
    def __init__(self,speed,fuel):
        self. speed = speed
        self. fuel = fuel


    def move(self):
        print(f'Transport{self.speed} tezlikda,{self.fuel} yoqilgi bilan harakatlanmoqda')


class Car(Transport):
    def __init__(self,brand,speed,fuel,color):
        super().__init__(speed,fuel)
        self. brand = brand
        self. color = color


    def move(self):
        super().move()
        print(f'Car {self.brand},rang:{self.color}')


m1 = Car("Bmw",150,30,'Qora')
m1.move()


# 2-m
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender


    def introduce(self):
        print(f'ism:{self.name}')
        print(f'yosh:{self.age}')
        print(f'jins:{self.gender}')

class Student(Person):
    def __init__(self,name,age,gender,grade,university):
        super().__init__(name,age,gender)
        self.grade = grade
        self.university = university

    def introduce(self):
        super().introduce()
        print(f'Grade {self.grade},un:{self.university}')

p1 =Student('Ali',20,'ogil bola','kimyo','sdtu')
p1.introduce()

class Animal:
    def __init__(self,name,age,type):
        self.name = name
        self.age = age
        self.type = type

    def eat(self):
        print(f'ism:{self.name} ovqat yeyapti')
        print(f'yosh: {self.age}')
        print(f'it:{self.type}')

class Dog(Animal):
    def __init__(self,name,age,type,breed,color):
        super().__init__(name,age,type)
        self.breed = breed
        self.color = color

    def eat(self):
        super().eat()
        print(f'breed {self.breed},color:{self.color}')
a1 =Dog('rex',3,'it',"ovchi it","oq")
a1 .eat()

# 4-m
class Employee:
    def __init__(self,name,salary,experience):
        self.name = name
        self.salary = salary
        self. experience = experience

    def work(self):
        print(f'ism:{self.name} ishlamoqda')
        print(f'maosh:{self.salary}')
        print(f'tajriba:{self.experience}')


class Manager(Employee):
    def __init__(self,name,salary,experience,department,team_size):
        super().__init__(name,salary,experience)
        self.department = department
        self.team_size = team_size

    def work(self):
        parent_work = super().work()
        print(f"{parent_work}\nManager {self.department} bo‘limini boshqarmoqda")



m = Manager("Ali", 5000, 5, "IT", 10)
print(m.work())

# 5-m
class SHape:
    def __init__(self,name,color):
        self.name = name
        self. color = color

    def area(self):
        print(f'ism:{self.name} shakl yuzasi aniqlanmagan')
        print(f'rang:{self.color}')

class Rectangle(SHape):
    def __init__(self,name,color,width,height):
        super().__init__(name,color)
        self.width = width
        self.height = height

    def area(self):
        super().area()  # ota metodni chaqirish
        result = self.width * self.height
        print(f"Yuza: {result}")
        return result




rect = Rectangle("To'rtburchak", "qizil", 5, 10)
rect.area()

# 6-m
class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def read(self):
        print(f'sarlavha:{self.title} oqilmoqda')
        print(f'muallif:{self.author}')
        print(f'sahifa: {self.pages}')

class EBook(Book):
    def __init__(self,title,author,pages,file_size,format):
        super().__init__(title,author,pages)
        self.file_size = file_size
        self.format = format

    def read(self):
        super().read()
        print(f'file_size: {self.file_size} ,text:{self.format}')

b1 = EBook('odam bolish qiyin','A.Qodiriy',123,2,'hgfgf')
b1.read()

# 7-m
class Device:
    def __init__(self,brand,power,warranty):
        self.brand = brand
        self.power = power
        self.warranty = warranty

    def turn_on(self):
        print(f'brand:{self.brand} yoqildi')
        print(f'quvvat:{self.power}')
        print(f'kafolat:{self.warranty}')

class Phone(Device):
    def __init__(self,brand,power,warranty,model,sim_count):
        super().__init__(brand ,power,warranty)
        self.model = model
        self.sim_count = sim_count

    def turn_on(self):
        super().turn_on()
        print(f'model :{self.model},sim_count: {self.sim_count}')

d1 =Phone('iphon',"132 GB",'8-yil','iphone','telefon')
d1.turn_on()

# 8-m
class User:
    def __init__(self,username,password,email):
        self.username =username
        self.password = password
        self.email = email

    def login(self):
        print(f'ism:{self.username} tizimga kirdi')


class Admin(User):
    def __init__(self,username,password,email,role,perissions):
        super().__init__(username,password,email)
        self.role = role
        self.perissions = perissions

    def login(self):
        super().login()
        print(f'role:admin')
        self.delete_user()
u1 = Admin('Azamat','Iud','sgulshoda@','ajayib','kompyuter')
u1.login()


# 9-m
class Vehicle:
    def __init__(self, speed, weight, fuel_type):
        self.speed = speed
        self.weight = weight
        self.fuel_type = fuel_type

    def drive(self):
        print(f"Vehicle {self.speed} km/soat tezlik bilan harakat qilmoqda.")


class Bike(Vehicle):
    def __init__(self, speed, weight, fuel_type, bike_type, gear):
        super().__init__(speed, weight, fuel_type)
        self.bike_type = bike_type
        self.gear = gear

    def drive(self):
        super().drive()  # ota metodni chaqirish
        print(f"Bike turi: {self.bike_type}")


b = Bike(40, 15, "benzin", "sport", 6)
b.drive()

10-m
class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience

    def teach(self):
        print(f"{self.name} dars bermoqda")


class MathTeacher(Teacher):
    def __init__(self, name, subject, experience, level, salary):
        super().__init__(name, subject, experience)
        self.level = level
        self.salary = salary

    def teach(self):
        super().teach()  # ota metodni chaqirish
        print(f"Daraja (level): {self.level}")

    def solve_problem(self):
        print(f"{self.name} matematik masalani yechmoqda")


t = MathTeacher("Ali", "Matematika", 5, "Senior", 3000)

t.teach()
t.solve_problem()
