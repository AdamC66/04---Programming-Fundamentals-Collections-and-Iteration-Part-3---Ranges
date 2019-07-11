# Exercise 11
# Let's do our own Bitmaker version of FizzBuzz, which is the name of a classic job interview coding problem.

# Write a program that loops over the numbers from 1 to 100. If the number is a multiple of three, output the string "Bit". For multiples of five, output "Maker". For numbers which are multiples of both three and five, output "BitMaker". Otherwise output the number itself.

# To solve this problem you will likely need to search the web. Start with the particular aspect of the question you are unsure of, such as "check if number is multiple of another python". Do use online resources, but do not read or copy an entire solution to the problem. Make sure the code you submit is your own. You will learn much more if you work through it yourself!

# As always, don't forget to commit your work as you make progress.

for i in range(1,101):
    if i%3 ==0 and i%5 ==0:
        print("Bitmaker")
    elif i%3 ==0:
        print("Bit")
    elif i%5 == 0:
        print("Maker")
    else:
        print(i)

# Exercise 12
# PizzaMaker wants to handle bulk orders of pizzas, with varying amounts of toppings on each. Ask the user for a number of pizzas - call it quantity. 
# We then want to ask the user for quantity more numbers - the number of toppings on that pizza - and print them out as in the following example.

# How many pizzas do you want to order?
# $ 3
# How many toppings for pizza 1?
# $ 5
# You have ordered a pizza with 5 toppings.
# How many toppings for pizza 2?
# $ 1
# You have ordered a pizza with 1 toppings.
# How many toppings for pizza 3?
# $ 4
# You have ordered a pizza with 4 toppings.

# You will need:
# to ask the user for input twice.
# a loop of some kind.
# to make sure your variables are what you think they are! Convert them to integers if needed.
# string interpolation

numpizzas=0
pizzatoppings = []


def get_input(inputstring):
    variable=0
    wait_for_input=True
    while wait_for_input == True:
        print(inputstring)
        user_input = input()
        try:
            variable = int(user_input)
            wait_for_input = False
            return(variable)   
        except ValueError:
            print("Your input was invalid or unrecognized, please enter a number")
        
        

numpizzas=get_input("Please enter how many pizza\'s you would like to order")


for i in range(numpizzas):
    pizzatoppings.append(get_input("How many toppings for pizza # {}".format(i+1)))
    print("you have ordered a pizza with {} toppings\n".format(pizzatoppings[i]))