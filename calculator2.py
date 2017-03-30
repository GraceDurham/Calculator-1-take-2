from arithmetic import *

while True:
    user_input=raw_input(">")

    split_action = user_input.split(" ")
    print split_action

    if "q" in split_action:
        print "You will exit."
        break

    elif len(split_action) < 2:
        print "Not enough input"
        continue

    num1 = split_action[1]

    if len(split_action) < 3:
        num2 = 0

    else:
        num2 = split_action[2]

    if not num1.isdigit() and not num2.isdigit():
        print "those aren't numbers"
        continue
    elif split_action[0] == "+":
        print add(int(num1), int(num2))
    elif split_action[0] == "-":
        print subtract(int(num1), int(num2))
    elif split_action[0] == "*":
        print multiply(int(num1), int(num2))
    elif split_action[0] == "/":
        print divide(int(num1), int(num2))
    elif split_action[0] == "square":
        print square(int(num1))
    elif split_action[0] == "cube":
        print cube(int(num1))
    elif split_action[0] == "pow":
        print power(int(num1), int(num2))
    elif split_action[0] == "mod":
        print mod(int(num1), int(num2))

    else:
        print "Invalid input please choose one of the following operators +, -, *, /, square, cube, pow, mod or check the number arguments. Enter q to quit."
