'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by putting in some parameters
and printing what is returned outside of the function.

EXAMPLE TASK:
'''
#EX) Define a function that has two parameters. Make the function add the two
#numbers together and return the result.
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that has two int parameters. Make the function subtract 
#the first parameter minus the second one. Then, return the result. Now call 
#the function.
#Print what the function returns.
def sub_two_numbers(num1, num2):
    subtractionOfTwoNumbers = num1 - num2
    return subtractionOfTwoNumbers

x = sub_two_numbers(1, 2)
print (x)

#2) Define a function that has one parameter. Make the function divide the 
#parameter by 2, multiply it by 77, and then add 10,000. Return the result.
#Now call the function.
#Print what the function returns.
def num_function(num):
    num = num / 2
    num = num * 77
    num = num + 10000
    return num 
number = num_function (3)
print (number)
#3) Define a function that has two int parameters. Make the function check if 
#two numbers are equal. If they are equal, return true. If they are not equal, 
#return false. Now call the function.
#Print what the function returns.
def function(num1, num2):
    if (num1 = num2)
    print (True)
    else 
    print (False)
    return 
#4) Define a function that has two int parameters. Make the function
#check which parameter is bigger, and return the bigger parameter. 
#If they are the same, it should just return either parameter. Now call the 
#function.
#Print what the function returns.
def function(num1, num2):
    if (num1 > num2)
    print (num1)
    elif (num2 > num1)
    print (num2)
    else 
    print (num1 or num2)
    return 

#5) Define a function that has two string parameters. Make the function
#add the two strings together. And then return the combined string. Now call 
#the function.
#Print what the function returns.
def function(string1,string2):
    add_string = string1 + string2
    return add_string
x = "string" 
y = "string2"
return function(x,y)
#6) Define a function that has three int parameters. If the first number is 
#equal to the second OR the third number, return true. Else, return false. Now 
#call the function.
#Print what the function returns.
def function(num1,num2, num3):
    if (num1 = num2 or num3)
    print (True)
    else 
    print (False)
    return 
#7) Define a function that prints your name. It should have no parameters and 
#shouldn't return anything. Now call the function.
def function:
    print(tsering)
    

#8) Define a function that has one string parameter. The string should be a
#color. If that string is equal to your favorite color, it prints "That's my 
#favorite color!". If it is not, it prints "That is not my favorite color. 
#Try again.". It shouldn't return anything. Now call the function.
def function(string1):
    if ("color" = string1)
    print ("That's my favorite color!")
    else 
    print ("That is not my favorite color")
#9) Define a function that has one int parameter. The int should be 
#positive. If the number is not equal to zero, the function runs a loop that
#decrements the parameter by 1 and prints it each time. Now call the function.
def function(num1):
    num1 > 0 
    while num1 > 0 
        print(num1)
        num1 = num1 - 1
    return(num1)
