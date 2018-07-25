
import random

coin_flip = ["heads", "tails"]

list_of_option_0 = [1]

list_of_option_1 = [1]

print("There is 1 Option 0 ball and 1 Option 1 ball in the hat.")

number_of_iterations = int(input("How many times do you want to run the trial? (please enter a natural number) "))

#If coin flip is heads (option 0), based on the outcome of the option, adds 1 to the corresponding list for that option.
for i in range(number_of_iterations):
    if random.choice(coin_flip) == "heads":
        print("Option 0 was randomly selected.")
        answer0 = input("Did the trial yield a favorable outcome? (yes or no) ")
        if answer0 == "yes":
                list_of_option_0.append(1)
                print("There is/are now", len(list_of_option_0), "Option 0 ball(s) and", len(list_of_option_1), "Option 1 ball(s) in the hat.")
        elif answer0 == "no":
                list_of_option_1.append(1)
                print("There is/are now", len(list_of_option_0), "Option 0 ball(s) and", len(list_of_option_1), "Option 1 ball(s) in the hat.")
        else:
            print("Please enter valid input.")
            continue
    else:
        break


#If coin flip is tails (option 1), based on the outcome of the option, adds 1 to the corresponding list for that option.
    if random.choice(coin_flip) == "tails":
        print("Option 1 was randomly selected.")
        answer1 = input("Did the trial yield a favorable outcome? (yes or no) ")
        if answer1 == "yes":
                list_of_option_1.append(1)
                print("There is/are now", len(list_of_option_0), "Option 0 ball(s) and", len(list_of_option_1), "Option 1 ball(s) in the hat.")
        elif answer1 == "no":
                list_of_option_0.append(1)
                print("There is/are now", len(list_of_option_0), "Option 0 ball(s) and", len(list_of_option_1), "Option 1 ball(s) in the hat.")
        else:
            print("Please enter valid input.")
            continue
    else:
        break

#Gives output for the better option.
if len(list_of_option_0)>len(list_of_option_1):
    print("Option 0 is better.")

if len(list_of_option_0)<len(list_of_option_1):
    print("Option 1 is better.")
