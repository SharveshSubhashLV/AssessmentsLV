# -*- coding: utf-8 -*-
"""IA1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JmFZDWlvHX4SwcidUlTxo5m4zdqRth4A
"""

#Q1
l = float(input("Enter the length of your property: "))
w = float(input("Enter the width of your property: "))
def classifier(l,w):
  a = l*w
  if a<500:
    print("Small size Property","\n Area of the property: ", a,"sq.m.")
  elif a>=500 and a< 1000:
    print("medium sized Property","\nArea of the property: ", a,"sq.m.")
  else:
    print("Large scaled property","\nArea of the property: ", a,"sq.m.")
classifier(l,w)

#Q2
class person:
  def bmi(self,w,h):
    return (w / (h ** 2))

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

p = person()
bmi = p.bmi(weight,height)
print(bmi)

#Q3
students = {}
def add():
  name = input("Name: ")
  marks = input("For all subjects spaced with comma:").split(",")
  students[name]=marks
  print("\nDisplaying all records added till now\n")
  print(students)
def retrieve(n):
  print(n,"- Marks: ",students[n])
def update():
  add()
c = int(input("Press 1 to add records, 2 to retrieve a record and 3 to update a record and press 0 to exit."))
while c>0:
  match c:
    case 1:
      add()
      c = int(input("what do you want to do?"))
    case 2:
      n = input("Enter the name of the student to retrieve his marks")
      retrieve(n)
      c = int(input("what do you want to do?"))
    case 3:
      update()
      c = int(input("what do you want to do?"))]

#Q4
age = int(input("Enter your age"))
movies = {"HIGH-Rated-U":["Children contents in a list"],"High-Rated-A":["Teen and Adult content"],"High-Rated-S":["Senior Contents in list"]}
if age<=17:
  print("recommended content : ",movies["HIGH-RATED-U"])
elif age>=18 and age <40:
  print("recommended content : ",movies["High-Rated-A"])
elif age>=40:
  print("recommended content : ",movies["High-Rated-S"])

#Q5
subscriberid = [1,2,3,4,5,6,7,8,9,10,11,12]
def evenselector(f):
  r = []
  for i in f:
    if i%2 ==0:
      r.append(i)
  return r
print("Even IDs selected for promotion: ",evenselector(subscriberid))

#Q6
password = input()
def security(p):
  if password == "HashCodedPassword":
    print("Access Granted")
  else:
    print("Access Denied")
security(password)

#Q7
data = [9,10,8,7,6,5,8,9,10]
def insight(d):
  total = sum(d)
  l = len(d)
  print("Average Customer Rating: ", total/l)
  avg = total/l
  if avg>5:
    print("Good Customer Support performance")
  else:
    print("Customer Support needs improvement!")
insight(data)

#Q8
comments = ["The service is very good", "sooooooo goooooooooooood", "Best in the region","Can be better", "yoooooo youuuuuu can do"]
vcountL=[]
for s in comments:
  l = list(s.lower())
  v = ["a","e","i","o","u"]
  vcount = 0
  for e in v:
      vcount+= l.count(e)
  vcountL.append(vcount)

spamchecker = [True if x<14 else False for x in vcountL]
print("\nPrinting comments which are not spam\n")
print(vcountL)
for i in range(len(vcountL)):
  if spamchecker[i] is True:
    print(comments[i])
  else:
    print("Spam")

#Q9

#Q10
numerator = float(input("Enter the amount: "))
denominator = float(input("enter the numerical to divide the amount by: "))
try:
  if denominator ==0:
    raise ZeroDivisionError
except ZeroDivisionError:
  print("Zero can not be the divisor")

#Q11
def polling(data):
  for x in data:
    if isinstance(x,int):
      pass
    else:
      print(x, " is not in correct data type format, need int data type")
polling([1,2,3,4,"sharvesh"])

#Q12
expData = float(input("Enter the ExpData: "))
expdata2 = float(input("enter the numerical to divide this by: "))
def add():
  return expData+expdata2
def subtract():
  return expData-expdata2
try:
  if expdata2 ==0:
    raise ZeroDivisionError
except ZeroDivisionError:
  print("Zero can not be the divisor")

#Q13
import datetime

def write_UPTIME_data():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("uptime_data.txt", 'a') as f:
        f.write(f"Timestamp: {timestamp}\n")
        f.write("\n")
write_UPTIME_data()

#Q14
def read_lod_data():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("uptime_data.txt", 'r') as f:
      f.open()
read_log_data()