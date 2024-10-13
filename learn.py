
if 5>2:
  print("five is greater than 2")
  x= "john"
  y= 5
  print(x)
  print(y)
  my_Name= "john"
  my_num=5
  print(my_Name)
  print(my_num)
  myvar="brevian"
  print(myvar)
  myNameIs="waffula"
  print(myNameIs)
  my_name_is="bravo"
  print(my_name_is)


  fruits=["mangos","oranges","avocados"]
  x,y,z= fruits
  print(x)
  print(y)
  print(z)


  a= "awesome"

def myfunc():
    print("kenya is "+ a)

myfunc()

#global and local variable declaration

x= "awesome"
def func():
 x="fantastic"
 print("kenya is " +  x)

func()
print("kenya is "+  x)



def myfunc():
    x="john doe"
    print(x)
myfunc()

def myfunc():
    global x
    x="fantastic"
myfunc()
print("kenya is " +x)



x="kazi poa"

def myfunc():
    x="form ni kutesa"
myfunc()
print("kenya " + x)


x="kazi poa"

def myfunc():
    global x
    x="form ni kutesa"
myfunc()
print("kenya " + x)

#type of numbers,int,complex,float,string,boolen
x=3j
y=2
z=3.5
a="brevian"
b=True

#how to check data types of values assigned
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))

# if elif else statements
wind = 100 
status = "unset"
if wind<8:
    status="calm"
elif wind>=8 and wind<=31:
    status="breeze"
elif wind>=32 and wind<=63:
    status="gale"
else:
    status="storm"
print(status)


#loop lists
#for loop

thisList = ["banana","apple","oranges"]
for x in thisList:
    print(x)

#adding an item  append()
thisList = ["banana","apple","oranges"]
thisList.append("guava")
print(thisList)

#insering an item to a specific index insert()
thisList = ["banana","apple","oranges"]
thisList.insert(2,"guava")
print(thisList)


thisList = ["banana","apple","oranges"]
thisList[0:2]=["mapera","bravooo"]
print(thisList)


#adding list to current list use Extend()
thisList = ["banana","apple","oranges"]
thisList2 =  ["banana","apple","oranges"]
thisList.extend(thisList2)
print(thisList)


#removing an item
thisList = ["banana","apple","oranges"]
thisList.remove("apple")
print(thisList)

#Remove Specified Index
#The pop() method removes the specified index.
thisList = ["banana","apple","oranges"]
thisList.pop(2)
print(thisList)

#Clear the List
#The clear() method empties the list.

#The list still remains, but it has no content.

thisList = ["banana","apple","oranges"]
thisList.clear()
print(thisList)


thisList = ["banana","apple","oranges","tomatoes","potatoes"]
i = 1
while i < len(thisList):
    print(thisList[i])
    i+=1





#PYTHON INHERITANCE
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()


#python fstring
#allows formating selected part of a string
#to format in fstring you add a placeholder'{}'


#perforing operations

price= 50
txt= f"the price is { price} dollars"
print(txt)


price2= 50
tax= 0.25
txt1= f"The price is {price2 + price2*tax} dollars"
print(txt1)


price3= 100
txt3= f"it is very {"expensive"if price3 >99 else "cheap"}"
print(txt3)

#Execute Functions in F-Strings

fruits= "apples"
txt4= f"i love {fruits.upper()}"
print(txt4)


def converter(x):
    return x*2
txt5 = f"the plane is flying at {converter(3000)} above sea level"
print(txt5)


#The while Loop
#With the while loop we can execute a set of statements as long as a condition is true.


i =1
while i <20:
    print(i)
    if i ==17:
        break
        i+=1
