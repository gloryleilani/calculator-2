"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

from _functools import reduce


def my_reduce_func(func, nums):
    answer = func(nums[0], nums[1]) #default answer if 2 num entries
    
    for items in nums[2:]:              #handling case of >2 entries
        answer = func(result, item)
    
    return answer


def calculate_nums():

    while True:
        user_input = input("Enter your equation >")
        tokenized_user_input = user_input.split(" ")

        operator, *user_nums = tokenized_user_input #operator is position 0 in list, nums are position 1 onward.
        converted_nums = []
        answer = ""
        #print("operator and tokens", operator, *user_nums)

        #Add user-entered numbers to a list of numbers converted from strings to floats
        
        try:
            for item in tokenized_user_input[1:]:
                #print("list item i:", item) 
                converted_nums.append(float(item))

        except ValueError: 
            print("One or more of your operand entries was not a number.")   
            continue
        
        #print("Converted nums list:", converted_nums)

        #Error message if user entered too many or too few numbers
        #if operator == "cube" or operator == "square":
        #    if len(converted_nums) > 1 or len(converted_nums) < 1:
        #        print ("One operand was expected. Please try again.")
        #        continue

        #elif len(converted_nums) > 2 or len(converted_nums) < 2:
        #        print("Two operands were expected. Please try again.")
        #        continue


        if operator == "q":
            return
        
        elif operator == "+":
            answer = reduce(add, converted_nums)

        elif operator == "-":
            answer = reduce(subtract, converted_nums)
        
        elif operator == "*":
            answer = reduce(multiply, converted_nums)
        
        elif operator == "/":
            answer = reduce(divide, converted_nums)
        
        elif operator == "square":
            answer = square(converted_nums[0])
        
        elif operator == "cube":
            answer = cube(converted_nums[0])
        
        elif operator == "pow":
            answer = reduce(power, converted_nums)
        
        elif operator == "mod":
            answer = reduce(mod, converted_nums)
        
        else:
            print("I'm sorry, I didn't understand that operator. Hint: start with the arithmetic operator, followed by the number or numbers, each separated with a single space.")

        if answer != None:
            print(answer)

calculate_nums()


# Help on built-in function reduce in module _functools:

# reduce(...)
#     reduce(function, sequence[, initial]) -> value
    
#     Apply a function of two arguments cumulatively to the items of a sequence,
#     from left to right, so as to reduce the sequence to a single value.
#     For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
#     ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
#     of the sequence in the calculation, and serves as a default when the
#     sequence is empty.

#Prior code, which has since been enhanced/refactored:
# def calculate_nums():

#     while True:
#         user_input = input("Enter your equation >")
#         tokenized_user_input = user_input.split(" ")

#         try: num1 = int(tokenized_user_input[1])
#         except: 
#             answer = ""    

#         try: num2 = int(tokenized_user_input[2])
#         except: 
#             answer = ""

#         try: num3 = int(tokenized_user_input[3])
#         except: 
#             answer = ""

#         if tokenized_user_input[0] == "q":
#             return
        
#         elif tokenized_user_input[0] == "+":
#             answer = add(num1, num2)
        
#         elif tokenized_user_input[0] == "-":
#             answer = subtract(num1, num2)
        
#         elif tokenized_user_input[0] == "*":
#             answer = multiply(num1, num2)
        
#         elif tokenized_user_input[0] == "/":
#             answer = divide(num1, num2)
        
#         elif tokenized_user_input[0] == "square":
#             answer = square(num1)
        
#         elif tokenized_user_input[0] == "cube":
#             answer = cube(num1)
        
#         elif tokenized_user_input[0] == "pow":
#             answer = power(num1, num2)
        
#         elif tokenized_user_input[0] == "mod":
#             answer = mod(num1, num2)
        
#         else:
#             print("I'm sorry, I didn't understand that. Hint: start with the arithmetic operator, followed by the number or numbers, each separated with a single space.")

#         print(answer)

# calculate_nums()
