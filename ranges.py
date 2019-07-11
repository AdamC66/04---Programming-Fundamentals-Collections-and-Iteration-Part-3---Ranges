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
        