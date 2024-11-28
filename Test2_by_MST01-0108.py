# create a prime number and a composite number program
def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i ==0:
            return False
    return True

def check_num(limit):
    primes = []
    composites =[]
    for n in range(1,limit+1):
        if is_prime(n):
            primes.append(n)
        elif n>1:
            composites.append(n)
    return primes, composites

limit =100
primes,composites = check_num(limit)

print("prime numbers from 1 to 100")
print(primes)
print("composite numbers from 1 to 1oo")
print(composites)


# create range of multilication table 
def mul_table(start,end):
  for i in range(start,end+1):
    for j in range(1,11):
      result = i*j
      print(f"{i} x {j} = {result}")
    print()

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number:"))
mul_table(start,end)



# # program1---
#Priyanka wants to read a text file using python and she wants to print the content of that file in the terminal. But she is unable to specify the file name correctly. To help Priyanka write a program in python and show how to read the content of the text file and print it on the screen using python. ● Name of the text file: aboutPython.txt ● Content: ● Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. It's high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed. ● . ● Hint: ● Create a text file aboutPython.txt ● Copy the given content in that file ● Using python read the content of the file. ● Use the concept of file handling.



f =open("aboutPython.txt",'r')
print(f.read())
f.close()


#txt file
#Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. It's high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.



# program2---
#Himanshi has a text file and she wants to check whether that file contains any numerical value. So to help Himanshi write a python program that can check whether the text file includes any numerical value or not. As text files contain so many lines, so print the line number that has numerical values

f1 =open("program2_text.txt",'r')
line_num = 1
for line in f1:
    for char in line:
        if char.isdigit():
            print("line contain numericals at line {}".format(line_num))
            break 
    line_num+=1
f1.close()

# txt file 
# hello this is navya1
# this is he python exam
# mnb hjk ghju5852 ffgho5
# kjhjik8l hghjnk5




#program3---
#Arvind has a huge text file and he wants to put a serial number at the beginning of each line. Doing this task manually can take a lot of time. He is not aware of python file handling. Write a python program that can put a serial number in front of each line in any specified text file.


i_f_opening = open("input.txt",'r')
o_f_opening = open("output_txt",'w')

s_num = 1
for line in i_f_opening:
    o_f_opening.write("{}.{}".format(s_num,line))
    s_num+=1
i_f_opening.close()
o_f_opening = open("output_txt",'r')
print(o_f_opening.read())
o_f_opening.close()


# output file
# 1.hello this is navya1
# 2.this is he python exam
# 3.mnb hjk ghju5852 ffgho5
# 4.kjhjik8l hghjnk5