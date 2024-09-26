import time
import random
from threading import Timer

operations = ["+", "-", "*", "/"]
rules = "\nThe rules are simple: 10 questions, each will have the chosen time limit and are worth 2 \
points.\nYou will have 3 lives. Good Luck!"
pb = 0


def difficulty_selector():
    while True:
        difficulty_user = input("\nChoose a difficulty level - [E]asy/[I]ntermediate/[H]ard: ")
        difficulty_level = difficulty_user.lower()
        if difficulty_level == "e" or difficulty_level == "i" or difficulty_level == "h":
            return difficulty_level
            break
        elif difficulty_level == "f":
            print("Respect.")
            continue
        else:
            continue


def time_selector():
    while True:
        try:
            time = (int(input("\nChoose time option - [5] Seconds/[10] Seconds: ")))
            if time == 5 or time == 10:
                return (time)
            else:
                print("choose either 5 or 10")
                continue
        except ValueError:
            print("please enter a number")
            continue


def difficulty_translator(difficult_letter):
    if difficult_letter == "e":
        return ("Easy")
    if difficult_letter == "i":
        return ("Intermediate")
    if difficult_letter == "h":
        return ("Hard")


def difficulty_number_translator(difficult_level):
    if difficult_level == "e":
        add_subt_low = 1
        add_subt_high = 10
        multiply_divide_low = 1
        multiply_divide_high = 4
        return add_subt_low, add_subt_high, multiply_divide_low, multiply_divide_high
    elif difficult_level == "i":
        add_subt_low = 5
        add_subt_high = 20
        multiply_divide_low = 2
        multiply_divide_high = 8
        return add_subt_low, add_subt_high, multiply_divide_low, multiply_divide_high
    else:
        if difficult_level == "h":
            add_subt_low = 10
            add_subt_high = 50
            multiply_divide_low = 3
            multiply_divide_high = 12
        return add_subt_low, add_subt_high, multiply_divide_low, multiply_divide_high


answers = []
questions = []


def problem_factory(add_sub_min, add_sub_max, mult_div_min, mult_div_max):
    for i in range(10):
        question = ""
        operation = random.choice(operations)
        if operation == "+":
            num_one = random.randint(add_sub_min, add_sub_max)
            num_two = random.randint(add_sub_min, add_sub_max)
            question = str(num_one) + " " + operation + " " + str(num_two)
            questions.append(question)
            answer = num_one + num_two
            answers.append(answer)
        elif operation == "-":
            num_one = random.randint(add_sub_min, add_sub_max)
            num_two = random.randint(add_sub_min, add_sub_max)
            question = str(num_one) + " " + operation + " " + str(num_two)
            questions.append(question)
            answer = num_one - num_two
            answers.append(answer)
        elif operation == "*":
            num_one = random.randint(mult_div_min, mult_div_max)
            num_two = random.randint(mult_div_min, mult_div_max)
            question = str(num_one) + " " + operation + " " + str(num_two)
            questions.append(question)
            answer = num_one * num_two
            answers.append(answer)
        else:
            while True:
                num_one = random.randint(mult_div_min, mult_div_max)
                num_two = random.randint(mult_div_min, mult_div_max)
                if num_one >= num_two:
                    if num_one % num_two == 0:
                        question = str(num_one) + " " + operation + " " + str(num_two)
                        questions.append(question)
                        answer = num_one // num_two
                        div_answer = int(answer)
                        answers.append(div_answer)
                        break
                    else:
                        continue
                else:
                    if num_two % num_one == 0:
                        question = str(num_two) + " " + operation + " " + str(num_one)
                        questions.append(question)
                        answer = num_two // num_one
                        div_answer = int(answer)
                        answers.append(div_answer)
                        break
                    else:
                        continue


def timeup():
    global out_of_time
    out_of_time = True
    print("\nTime's up: Press Enter to Continue")


def link_start(time_limit):
    global pb, out_of_time
    lives = 3
    points = 0
    user_answer = ""
    out_of_time = False
    print("\nGame Loading....")
    time.sleep(5)
    print("\nGame Starts!")
    time.sleep(1)
    for i in range(len(questions)):
        out_of_time = False
        time.sleep(1)
        print("\nQuestion" + " " + str(i + 1) + ":" " " + questions[i])
        try:
            limit = Timer(time_limit, timeup)
            limit.start()
            user_answer = int(input("Your answer: "))
            limit.cancel()
            if out_of_time == True:
                lives -= 1
                print("Nice try smart guy.")
                if lives > 0:
                    print("You have " + str(lives) + " lives left!")
                else:
                    print("\nYou have no lives left! Better luck next time.")
                    break
            elif user_answer == answers[i]:
                points += 2
                print(random.choice(["Good Job!", "Excellent!", "Correct!"]) + " Points Earned: " \
                      + str(points))
            elif user_answer != answers[i] and type(user_answer) == int:
                lives -= 1
                if lives > 0:
                    print("Good try! You have " + str(lives) + " lives left!")
                else:
                    print("\nYou have no lives left! Better luck next time.")
                    break
        except ValueError:
            if out_of_time == True:
                lives -= 1
                if lives > 0:
                    print("Oops! You have " + str(lives) + " lives left!")
                else:
                    print("\nYou have no lives left! Better luck next time.")
                    break
            else:
                limit.cancel()
                lives -= 1
                print("You should've typed a number. You have " + str(lives) + " lives left!")
                if lives == 0:
                    print("\nBetter luck next time.")
                    break
                time.sleep(1)
        if i == 9 and lives != 0:
            print("\nCongrats on Beating the Game!")
            print("Total Points Earned: " + str(points))
            if points > pb:
                pb = points
                print("New Personal Best: " + str(points) + " Points!")
            else:
                print("Personal Best: " + str(pb) + " Points")


def program(choice):
    while True:
        if choice == "y":
            difficulty = difficulty_selector()
            difficulty_set = (difficulty_translator(difficulty))
            time_limit = time_selector()
            num_a, num_b, num_c, num_d = difficulty_number_translator(difficulty)
            problem_factory(num_a, num_b, num_c, num_d)
            settings = "\nDifficulty: " + difficulty_set + "\nTime Limit per Question: " \
                       + str(time_limit)
            print(settings)
            time.sleep(1)
            print(rules)
            link_start(time_limit)
            repeat = input("\nDo you want to play again? [Y]es or [N]o: ")
            repeat_selection = repeat.lower()
            if repeat_selection == "y":
                answers = []
                questions = []
                continue
            else:
                print("\nAlright! Have a good rest of your day.")
                break
        else:
            print("\nAlright! Have a good rest of your day.")
            break


user_option = input("Do you want to play a math game? [Y]es or [N]o: ")
choice = user_option.lower()
program(choice)