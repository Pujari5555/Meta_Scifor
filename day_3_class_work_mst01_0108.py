# -*- coding: utf-8 -*-
"""DAY-3_class_work_MST01-0108

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EctuIHiML9qzyEdIHdwZKE620LwMSkur

**1.Problem**
A palindrome is a word, number, phrase, or other sequence of characters that reads the same backward as forward, such as madam or racecar. Arunima got a new puppy (pet) and she wants to decide the name for her pet. The name of the pet should be a palindrome. Write a program to take the pet name as input and print "true" if it is palindrome or print "false" on screen. Help Arunima to decide the name ( should be palindrome ) of the puppy. Hint: reverse the name and compare it with the original name.
"""

pet_name=input("enter the pet name::")
reverse_name=pet_name[::-1]
if pet_name==reverse_name:
  print("true")
else:
  print("false")

"""**2.Problem**
Aarush and Yash are two friends in the same grade and they decided to create their secret language to communicate with each other. First of all, they decided to reverse each word. For example: come here = "emoc ereh". But this was very easy to understand for other students. They tried to make it a bit difficult and decided to put all the characters which are at odd indices first then all the characters which are at even indices. For example: come here = "oecm eehr". Write a program in python to create such type of secret language and convert the word Codeyoung into secret language using the same program. Can we convert the secret language back to normal language using python? Discuss
"""

text = "codeyoung"   # Input text
odd = text[1::2]
even = text[0::2]

secret_text = odd + even
print("Secret text is :: {}".format(secret_text))

splitting = len(secret_text) // 2
normal_text = ""

for i in range(splitting):
    normal_text += even[i] + odd[i]
if len(text) % 2 != 0:
    normal_text += even[-1]

print("Normal text is :: {}".format(normal_text))

"""**3.problem**
Vishal is creating a form and he wants to take the contact number as input. However, some people do not enter the number properly. Vishal is confused about how to verify whether the given number is in the correct format or not. To help Vishal write a python program to show how we can verify whether a given phone number is valid or not. ● Note: A valid phone number contains 10 digits with 9,8 or 7 as the first digit. Phone number only contains numbers and not any character. ● Hint: ● User len() function to verify the number of digits. ● Use isnumeric() function to check it only contains numeric values.Use indexing to check whether the first character is 9,8 or 7 or not.

"""

ph_no = int(input("enter the phone number::"))
ph_no = str(ph_no)
if len(ph_no)==10 and ph_no.isnumeric() and (ph_no[0]=='7' or ph_no[0]=='8' or ph_no[0]=='9'):
  print("valid")
else:
  print("Invalid")