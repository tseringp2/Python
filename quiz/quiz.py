'''
The Objective of this program is to quiz the user on basic high school
trivia. 
@author: Tsering Pelmo
'''
  #Make a variable called score to keep track of the correct answers. And set
#it to 0.
score = 0
#Ask the user question one. And store the users answer.
x = input("What is the powerhouse of the cell? A) mitochondria B) nucleus C) ribosome")
answer = "A"
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
if(x.upper() == "A"):
    print("Correct")
    score = score + 1
else:
    print("Incorrect, the correct answer is A")
#Ask the user question two. And store the users answer.
y = input("How many states comprise the United States? A) 13 B) 45 C) 50")
answe = "C" 
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
if(y.upper() == "C"):
    print("Correct")
    score = score + 1
else:
    print("Incorrect, the correct answer is C")
#Ask the user question three. And store the users answer.
z = input("In y = mx + b, what does m stand for?A) slope B) output C) I don't understand math")
answer = "A"
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
if (z.upper() == "A"):
    print("Correct")
    score = score + 1
else:
    print("Incorrect, the correct answer is A")
#Ask the user question four. And store the users answer.
o = input("In English, a person, place or thing is called:A) verb B) adjective C) noun")
answer = "C"
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
if (o.upper()== "C"):
    print("Correct")
    score = score + 1
else:
    print("Incorrect, the correct answer is C")
#Calculate the percentage the user got. And store it in a variable called p
p = score / 4 * 100
#Print out the users score: "You got a [score]/4. Or a [p]%."
print(p)
