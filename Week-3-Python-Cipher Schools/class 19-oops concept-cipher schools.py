#The __init__method
#Dunders(magic methods)(event methods)
#____
a=5
def func():
  pass
type(func)
class A:
  name="jatin"
  marks=50
  type(A)
  A=5
  type(A)
  type(int)
  type(object)
  type(int)
  object
  isinstance(a,object)
  type(int)
  isinstance(a,int)
  class A:
    pass
b=A.__call__()
b=A()
def func():
  print("Hello")
  func()
  func.__call__()
a={"name":"Jatin"}
a["name"]
a.__getitem__("name")
class Exponent:
  def __init__(self,n):
    self. n= n
  def __getitem__(self,x):
    return x ** self.n
e=Exponent(3)
e[6]
a = A()
type(a)
a()
b = A.__call__(A)
a=5
for i in range(5):
   print(i)
class A:
  name = "Asim"
  def __init__(self,n):
    self.n = n
a=A(2)
a.name
a.n
class Dog:
  kind = 'canine'
  def __init__(self, name):
    self.name=name
a=Dog("Max")
a.name
a.kind
a=[]
b=a
b.append(1)
class Dog:
  
  tricks = []

  def __init__(self, name):
    self.name = name
  def add_trick(self, trick):
    self.tricks.apend(trick)
d1=Dog("Maxx")
d1.add_trick("fetch")
d1.add_trick("talk")
d1.tricks
d2=Dog("Bells")
d2.tricks
d2 = Dog("Sells")