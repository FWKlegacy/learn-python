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

