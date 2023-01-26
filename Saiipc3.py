#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Employee:
    number_of_employees = 0 

    def __init__(self, name, family, salary, department):#constructor to initialize name, family, salary, department.
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.number_of_employees += 1

    def average_salary(self): #a function to average salary.
        return sum([emp.salary for emp in Employee.emps])/len(Employee.emps)

    emps = []#creating an empty list.

class FulltimeEmployee(Employee):#Creating a class and inheriting the properties from Employee class.
    pass

e1 = Employee("Rahul", "Gandhi", 5000, "Data Science")
e2 = Employee("Sam", "Pitroda", 6000, "AI")
e3 = FulltimeEmployee("Dk", "Shivkumar", 5000, "Java")
e4 = FulltimeEmployee("Sachin", "Pilot", 15000, "Aeronautics")

#Appending to 'emps' list.
Employee.emps.append(e1)
Employee.emps.append(e2)
Employee.emps.append(e3)
Employee.emps.append(e4)

print("Avg salary of the employees is: ", e1.average_salary())
print("Number of employees: ",FulltimeEmployee.number_of_employees)


# In[5]:


import numpy as np

# Creating a random vector of size 20 having only float in the range 1-20. 
vec = np.random.uniform(1, 20, 20)

# Reshape the array to 4 by 5
arr = vec.reshape(4, 5)

# Replace the max in each row by 0 (axis=1)
arr[np.arange(4), arr.argmax(axis=1)] = 0
print(arr)


# In[ ]:




