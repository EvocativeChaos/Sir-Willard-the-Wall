knight = "Ser Willard the Wall"
print ("To play this game, you are given a story with different scenearios, and with deduction you choose the right answer and survive.")
from Question import Question
question_prompts = [
    "Ready to start?\n(a) Yes\n(b) No"
]
questions = [
    Question(question_prompts[0], "a")
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            print ("Let's go! The army needs you!")
        elif answer != question.answer:
            print ("Alright, have it your way ¯\_(ツ)_/¯")
            exit()
run_test(questions)

print ("This is it, this is the battle that will decide the victor,\nand the one that will echo through the ages!")
print ("And as a knight, you've been appointed to aid " + knight + " ,whom\nhas never been surpassed in battle.")
print ("With his legendary hammer which boasts a staggering 7 feet! The enemies\nfast approach!")
from Question import Question
question_prompts = [
    "Do you...\n(a) Take your Sword\n(b) Take your War Axe"
]
questions = [
    Question(question_prompts[0], "a,b")
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print ("You're getting ready for war!")


run_test(questions)

print("Some hours have passed and you managed to take down 3 spear men, who dared to\ncross " + knight + "'s blindspot.")
print (knight + " thanked you for your aid, the chance of him dying is an absolute 0,\nbut you managed to save the men with mere padding as armor from\nhostile spear men.")
from Question import Question
question_prompts = [
    "Do you say...\n(a) You're quite welcome, my liege\n(b) No problemo my man"
]
questions = [
    Question(question_prompts[0], "a,b")
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print ("Honor surges through you!")
run_test(questions)
print ("After 3 days, you see another army marching closer to you. It seems the enemies\nhave sent reinforcements to best our army. Suddenly\n" + knight + " calls your name and tells you to look back and you then\nyou see an assasin with a blade capable of piercing your helmet's visor\ncharging at you with great speed")
from Question import Question
question_prompts = [
    "Do you...\n(a) Grab his arms\n(b) Try and unsheathe your weapon"
]
questions = [
    Question(question_prompts[0], "a")
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            print ("You survived the attack!")
        elif answer != question.answer:
            print ("Game Over...")
            exit()
run_test(questions)
print ("You managed to kill the assassin, but your heart is racing. You try and calm\nyourself down. You notice 2 water cantines, one says Overwatch,\nand the other Battleborn.")
from Question import Question
question_prompts = [
    "From which do you drink out of?\n(a) Battleborn\n(b) Overwatch"
]
questions = [
    Question(question_prompts[0], "b")
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            print ("You are calming down")
        elif answer != question.answer:
            print ("You drank poison...")
            exit()
run_test(questions)
print ("Several days have passed and the war is nearing its conclusion. " + knight + " is exhausted but still insermountable.\nYou can barely move a limb, your muscles are greatly fatigued. You see\nthe man you must kill to end this war.")
print (knight + " would like to promote you for he sees great potential in you, great potential indeed. He offers\nyou two crossbows, a light-draw weight crossbow for impact on shorter distances and\na heavy-draw weight cross bow good for very long distances.")
print ("The man whose murder you must pursue is retreating to call in reinforcements!")
from Question import Question
question_prompts = [
    "Quick! Which crossbow do you choose?!\n(a) Light Crossbow\n(b) Heavy Crossbow"
]
questions = [
    Question(question_prompts[0], "a")
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            print ("You did it! Along with your promotion, you saved your Kingdom!" + knight + " is forever your comrade and in your debt!")
        elif answer != question.answer:
            print ("The man escaped, the war is prolonged, you are captured in combat and put to death by torture...")
run_test(questions)
print ("Credits\nVictor De Luna:           Character and Story")
print ("Angel M. Carballo:           Game Design and Programming")
