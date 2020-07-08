"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
#BREAKING DOWN PROBLEM:
#Loop forever collecting user input and doing the operation
#Take in user input, can be any arithmetic operator and two numbers
#The input string needs to be tokenized by converting it to a list of string items.
#Using split operation on the string it tokenizes into alist. 
#If first token is x operation, call function xx, elif y...
#if first token is q, quit. 

#PSEUDOCODE
#While True:
#user_input = Input("Enter your equation >")
#tokenized_user_input = user_input.split(" ")
#if tokenized_user_input[0] == "q":
#   return
#elif tokenized_user_input[0] == "+":
#   add(tokenized_user_input[1], tokenized_user_input[2])
#elif tokenized_user_input[0] == "-":
#   subtract(tokenized_user_input[1], tokenized_user_input[2])
#elif tokenized_user_input[0] == "*":
#   multiply(tokenized_user_input[1], tokenized_user_input[2])
#elif tokenized_user_input[0] == "/":
#   divide(tokenized_user_input[1], tokenized_user_input[2])
#elif tokenized_user_input[0] == "square":
#   square(tokenized_user_input[1])
#elif tokenized_user_input[0] == "cube":
#   cube(tokenized_user_input[1])
#elif tokenized_user_input[0] == "pow":
#   power(tokenized_user_input[1], tokenized_user_input[2])
#elif tokenized_user_input[0] == "mod":
#   mod(tokenized_user_input[1], tokenized_user_input[2])
#else:
#   print("I'm sorry, I didn't understand that. Please enter your equation, starting with the arithmetic operator, followed by the number or numbers.")


def calculate_nums():

    while True:
        user_input = input("Enter your equation >")
        tokenized_user_input = user_input.split(" ")

        try: num1 = int(tokenized_user_input[1])
        except: 
            answer = ""    

        try: num2 = int(tokenized_user_input[2])
        except: 
            answer = ""

        if tokenized_user_input[0] == "q":
            return
        
        elif tokenized_user_input[0] == "+":
            answer = add(num1, num2)
        
        elif tokenized_user_input[0] == "-":
            answer = subtract(num1, num2)
        
        elif tokenized_user_input[0] == "*":
            answer = multiply(num1, num2)
        
        elif tokenized_user_input[0] == "/":
            answer = divide(num1, num2)
        
        elif tokenized_user_input[0] == "square":
            answer = square(num1)
        
        elif tokenized_user_input[0] == "cube":
            answer = cube(num1)
        
        elif tokenized_user_input[0] == "pow":
            answer = power(num1, num2)
        
        elif tokenized_user_input[0] == "mod":
            answer = mod(num1, num2)
        
        else:
            print("I'm sorry, I didn't understand that. Hint: start with the arithmetic operator, followed by the number or numbers, each separated with a single space.")

        print(answer)

calculate_nums()

