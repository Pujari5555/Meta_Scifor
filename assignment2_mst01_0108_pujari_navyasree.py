# -*- coding: utf-8 -*-
"""Assignment2_MST01-0108_PUJARI NAVYASREE

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OOGebpY1CIUVqko83dOUrOe0zVp7q8wV

**1.Its childrens day and the class teacher wanted to share chocolates with the entire class the details are as follows,The number of chocolates with the teacher are = 327 Number of kids in the class are = 78. Write a program to perform modulus division using (%) modulus operator and find out how many chocolates are remaining with the teacher after equally distributing 327 chocolates to 78 students.**
"""

# Number of chocolates and students
total_chocolates = 327
total_students = 78

remaining_chocolates = total_chocolates % total_students

print("The number of remaining chocolates after distribution :", remaining_chocolates)

"""**2.It's Domino's 25th Anniversary and is planning for a big give away and in order to choose the lucky draw winner Domino's first needs to collect all of its customer details. On collecting the customer details Domino's even wants to thank each and every customer for visiting as soon as they entered their details.Write a program to accept customer details like customer name, customer mobile number, customer age, customer email Id.On successfully receiving all the customer information write a print() to thank the customer by using his name for example"Hi", customerName,"!! Thanks for visiting our restaurant and registering for our lucky draw competition on our 25th Anniversary.""Once the lucky draw results are announced you will receive a message on your mobile number :",customerMobileNumber"An detailed description of your gift on your email Id :",customerEmailId"Thank you for being a valued customer",customerName,"!!""Dominos"**"""

# Collect customer details
customer_name = input("Enter your name: ")
customer_mobile_number = input("Enter your mobile number: ")
customer_age = input("Enter your age: ")
customer_email_id = input("Enter your email ID: ")

print("Hi {}!! Thanks for visiting our restaurant and registering for our lucky draw competition on our 25th Anniversary.".format(customer_name))
print("Once the lucky draw results are announced you will receive a message on your mobile number: {}".format(customer_mobile_number))
print("A detailed description of your gift will be sent to your email ID: {}".format(customer_email_id))
print("Thank you for being a valued customer, {}!!".format(customer_name))
print("Domino's")

"""**3.Teacher wants to conduct a quiz activity in her class. For that she is planning to group 4 students for each team among 60 students. She wants to know how many teams she can create among 60 students.Write a program to find the total number of teams that can be created among students by dividing total number of students to the number of students per team.Total number of student = 60 Number of students per team =4**

"""

#group formation
team_size = 4
total_students = 60

total_teams = total_students // team_size

print("Total number of teams that can be created:", total_teams)

"""**4.Nidhi loves to travel to different countries. She is now in a country where the temperature is measured in Fahrenheit and she is not able to understand it in a better way. To help her in this situation, write program to convert temperature from Fahrenheit to celsius. ● Hint: (0°C × 9/5) + 32 = 32°F**"""

#CONVERSION OF TEMPRATURE FROM FAHRENHEIT TO CELSIUS
F = float(input("Enter the temperature in Fahrenheit: "))
C = (F - 32) * 5/9
print("Temperature in Celsius:", C)