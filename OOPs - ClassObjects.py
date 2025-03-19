class MyClass:
    x = 5 


p1 = MyClass()
print(p1.x)    
class TryClass:
    def __init__(self, name, age):
      self.name = name
      self.age = age

name = input("Enter you name : ")
age = input("Enter you age : ")
p2 = TryClass(name, age)
print(p2.name)    
print(p2.age)
print("My name is ",name+ " and I am ",age+ " years old")
#can delete class instance p2 using del p2
#pass can bypass the error if you want define class like below
class forpass:
   pass