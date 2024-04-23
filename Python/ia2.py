# -*- coding: utf-8 -*-
"""IA2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yraxDa-o7vuMzCgk4ctUV4p2dGuie_Hk
"""

import numpy as np
#Q1
arr = np.array([1,2,3,4,5,6])
print("Mean: ",np.mean(arr))
print("Max: ",np.max(arr))
print("Min: ",np.min(arr))
print("Sum: ",np.sum(arr))
print("Standard Deviation: ",np.std(arr))

#Q2
health_data = np.array([[160, 70, 30],   # height, weight, age for individual 1
                        [165, 65, 35],   # height, weight, age for individual 2
                        [170, 75, 40]])  # height, weight, age for individual 3

def normalize(data):
  while np.mean(data)>0 and np.std(data)> 1:
      data = data - np.mean(data,axis=0) / np.std(data,axis=0)
      if (np.mean(data)==0) and (np.std(data)==1):
        break
  return data
ar = normalize(health_data)
print(ar)

#Q3 NA

#Q4
arr1 = np.linspace(15,25,24)
print(arr1)

#Q5
import numpy as np
daily_closing_prices = np.array([100, 102, 98, 105, 107, 110, 108, 112, 115, 118, 120])
window_size = 5

#Q6 NA

#Q7
import numpy as np
properties_matrix = np.array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]])

np.linalg.det(properties_matrix)

#Q8
m = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(m[m>5])

#Q9
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'Age': [25, 30, 35, 40, 45, 50, 55],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Miami', 'Boston'],
        'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales', 'IT', 'HR']}

import pandas as pd
df = pd.DataFrame(data)

df1 = df[(df['Age'] < 45) & (df['Department'] != 'HR')]

result = df1[['Name', 'City']].values.tolist()

print("Employees who are aged under 45 and dont belong to HR department")
print(result)

#Q10
import pandas as pd

data = {
    'Department': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Home Goods'],
    'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Sales': [70000, 50000, 30000, 40000, 60000]
}

df = pd.DataFrame(data)
department_sales = df.groupby('Department')['Sales'].sum()
department_salesman_count = df.groupby('Department')['Salesperson'].size()
average_sales_per_salesman = department_sales / department_salesman_count
ranked_departments = average_sales_per_salesman.sort_values(ascending=False).reset_index()
ranked_departments['Salespeople Count'] = department_salesman_count.reset_index(drop=True)
print("Ranked Departments based on Average Sales per Salesman:")
print(ranked_departments)

#Q11
data = {
    'Product': ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries', 'Flour', 'Grapes'],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit', 'Bakery', 'Fruit'],
    'Price': [1.20, 0.50, 3.00, 2.50, 4.00, 1.50, 2.00],
    'Promotion': [True, False, True, True, False, True, False]
}
df1 = pd.DataFrame(data)
df2 = df1[(df1['Category']=='Fruit') & (df1['Promotion'] == False)]
avg = df2['Price'].aggregate('mean')
print(df2[df2['Price'] >= avg])

#Q12
import pandas as pd

employee_data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'IT', 'Finance', 'IT'],
    'Manager': ['John', 'Rachel', 'Emily', 'Rachel']
}
#Dataset for employee project assignments
project_data = {
    'Employee': ['Alice', 'Charlie', 'Eve'],
    'Project': ['P1', 'P3', 'P2']
}


edf = pd.DataFrame(employee_data)
pdf = pd.DataFrame(project_data)

mdf = pd.merge(pdf, edf, on='Employee', how='left')

mdf['Department'] = mdf['Department'].fillna('Unassigned')
mdf['Manager'] = mdf['Manager'].fillna('Unassigned')

dep_ov = mdf.groupby(['Department', 'Manager'])['Project'].apply(list).reset_index()

print("Departmental Overview:")
print(dep_ov)

#Q13, 14, 15 - Data Uploading
import pandas as pd
spt = pd.read_csv("/content/sample_data/Q13_sports_team_stats.csv")
cp = pd.read_csv("/content/sample_data/Q14_customer_purchases.csv")
sg = pd.read_csv("/content/sample_data/Q15_student_grades.csv")

#Q13 NO score data available for each game data to find out average score per game
spt['WinRatio'] = spt['Wins']/spt['GamesPlayed']
spt

#Q14
import datetime as dt

cp['Date'] = pd.to_datetime(cp['Date'])
cp['LoyaltyProgramSignUp'] = pd.to_datetime(cp['LoyaltyProgramSignUp'])
cp

#Q15
sg1 = sg.groupby('Subject').mean()
sg1

"""#Clearly, the average grades in the Histroy subject is less, so I would recommend to give more support in that subject."""