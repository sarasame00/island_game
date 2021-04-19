import time
import random


def print_pause(string, seconds):
    print(string)
    time.sleep(seconds)


invalid_input = ["\nSorry, but that's not correct.", "\nI think "
                 "we are not understanding each other.", "\nI do"
                 "n't know what you mean, try again!", "\nSorry, "
                 "I didn't understand you."]


# !!!!!!! INTRO !!!!!!!


def welcome():
    global man_name
    global password
    global color1
    global color2
    global backpack
    global visits_woman
    global visits_man
    global visits_carpenter
    global visits_flor
    global visits_mystery
    global visits_pharmacy
    global visits_yose
    global player_name
    color1 = random.choice(["blue", "green", "yellow", "purple", "black"])
    color2 = random.choice(["gray", "red", "white", "orange"])
    password = random.choice(["casa", "habitacion", "cantautor", "fuego",
                              "oregano", "primavera", "tardor", "cigarro",
                              "efimer", "enlluernador", "bonita", "invierno",
                              "arbre"])
    man_name = random.choice(["Josep", "Andreu", "Nil", "Joan", "Jordi",
                              "Ramón", "Guillem", "Pedro", "Ricardo",
                              "Arturo", "Luís", "Federico", "Antoni", "David",
                              "Martí", "Marc", "Adrián"])
    backpack = []
    visits_woman = 0
    visits_man = 0
    visits_carpenter = 0
    visits_flor = 0
    visits_mystery = 0
    visits_pharmacy = 0
    visits_yose = 0
    player_name = ""
    print_pause("\nWelcome player!\n", 3)
    print_pause("\nBefore we start, here are some instructions:\n", 3)
    print_pause("\nWhen you are asked a question you will have several options"
                " with a number in front of it. You have to enter the number "
                "of the option you want to carry out.\nThere are also some "
                "open questions, such as when they ask for your name.\n\nHavin"
                "g said this...\n", 10)
    want_to_play = input("\nAre you ready to play?\n\n1. Yes\n2. No\n")
    if want_to_play == "1":
        print_pause("\nCool! So let's start!", 2)
        return intro()
    elif want_to_play == "2":
        print_pause("\nOh...Well, come back when you are ready!\n", 5)
        return False
    else:
        print_pause(random.choice(invalid_input), 4)
        return welcome()
    return False


def intro():
    print_pause("\n\nYou don't know how, and neither do I, but you have arrive"
                "d at an island. It's quite pretty, but you must go home.\nSo,"
                " your mission here is to get off the island.\n\nSomeone told "
                "me that there is a boat that sets sail every day, but it "
                "won't be easy that they let you hop on!\n\nYou start at the "
                "train station.\n\nGOOD LUCK!\n\n", 14)
    return train_station()


# !!!!!!! TRAIN STATION !!!!!!!


def train_station():
    print_pause("\nYou are in the train station. In the following minutes, "
                "three trains depart with three different destinations.", 3)
    return train_decision()


def train_decision():
    choice = input("\nThe first one goes to the port, the second "
                   "one to the woods and the last one to the vil"
                   "lage.\nWhich one will you choose?\n\n1. Port\n2. Woods"
                   "\n3. Village\n")
    if choice == "1":
        return port()
    elif choice == "2":
        return woods()
    elif choice == "3":
        return village()
    else:
        print_pause(random.choice(invalid_input), 2)
        return train_decision()


# !!!!!!!! WOODS !!!!!!!!


def woods():
    print_pause("\nWhen the train stops and you get off, you see yourself in"
                " the middle of the deep woods.", 3)
    return woods_decision()


def woods_decision():
    print_pause("\nThere are two possible paths, the one on the right and the"
                " one on the left.", 1)
    choice = input("\n\nWhich one will you choose?\n\n1. Right path\n2. Left "
                   "path\n3. Back to the train station\n")
    if choice == "1":
        return right_choice()
    elif choice == "2":
        return left_choice()
    elif choice == "3":
        return train_station()
    else:
        print_pause(random.choice(invalid_input), 3)
        return woods_decision()


# !!!!! RIGHT CHOICE !!!!!


def path(adjective):
    time.sleep(2)
    print_pause("\nYou are getting on the path on the " + adjective + ".", 2)


wrong_answer = ['"\nWrong! Try again!"', '\n"I\'m sorry, that\'s not corr'
                'ect. You have another opportunity."', '\n"NOOOOOOO'
                '! Try again."', '\n"I\'m starting to '
                'get tired of you. Come on, try again."']


def right_choice():
    path("right")
    print_pause("You walk", 1)
    for x in range(5):
        print_pause("and walk", 1)
    print_pause("And finally you see a little house inside the woods.\n"
                "You walk until you are in front of the house.", 4)
    return knock()


def knock():
    answer = input("\nYou are in front of the door.\nAnd "
                   "then, what do you want to do? Go back or knock on the "
                   "door?\n\n1. Go back\n2. Knock on the door\n")
    if answer == "2":
        print_pause("\nYou knock.\n", 1)
        return password_check()
    elif answer == "1":
        print_pause("\nSo you walk back to the crossroad.\n", 1)
        return woods_decision()
    else:
        print_pause(random.choice(invalid_input), 3)
        return knock()


def password_check():
    print('\n"Hi traveller, if you want to come in I\'ll'
          ' need you to say the magic word."')
    times = 0
    while password not in input("The password is...").lower():
        if times > 4:
            print('\n"Okay, honey, enough! You are'
                  ' laughing at me!\nGo away!!!"')
            time.sleep(3)
            print_pause("\nOh..It seems like you will have to leave the house"
                        "...", 4)
            return knock()
        else:
            print(random.choice(wrong_answer))
            times += 1
    print_pause('\n"Alright, come on in!"', 2)
    return wanna_play()


def wanna_play():
    global visits_carpenter
    print_pause("\nYou are inside a little house, full of carpentry tools."
                "\n", 3)
    if visits_carpenter == 0:
        visits_carpenter += 1
        play = input('"Mmm someone told me that you are looking for a way out '
                     'of this island...\nI may have some things that can help '
                     'you. But first you will need to answer some questions. '
                     'Agree?"\n\n1. Yes\n2. No\n')
    else:
        if "tools" in backpack:
            print_pause('"Hi ' + player_name + '! I gave you all I have! Sorry'
                        ', but I\'m working now... Bye-bye!!"\n', 3)
            return knock()
        else:
            play = input('"Hey!! You again! Want to play?"\n\n1. Yes\n2. No')

    if play == "1":
        return play_game()
    elif play == "2":
        print_pause('\n"Oh..what a pity. Well, come back when you are ready to'
                    ' play. See you!!"', 3)
        return knock()
    else:
        print_pause(random.choice(invalid_input), 3)
        return wanna_play()


def play_game():
    global player_name
    answers = []

    def correct_or_not(result, question):
        if result == question:
            answers.append("correct")
        else:
            answers.append("incorrect")

    if player_name == "":
        player_name = input('\n"Cool!"\n"First things first, what\'s your '
                            'name?"\n')
        print_pause('\n"Alright ' + player_name + ', let\'s start!"\n\n"Hope '
                    'you are good at mathematics because this is about testing'
                    ' your calculus skills hahahaha! Good luck!"\n', 5)
    else:
        print_pause('\n"Cool!"\n', 2)
        print_pause('\n"Alright, let\'s start!"\n\n"Hope you '
                    'are good at mathematics because this is about testing '
                    'your calculus skills hahahaha! Good luck!"\n', 5)

    question1 = input('\n"23 x 3 + 11 ="\n')
    correct_or_not("80", question1)
    question2 = input('\n"(34 + 8) : 7 ="\n')
    correct_or_not("6", question2)
    question3 = input('\n"24 x 4 + 11 ="\n')
    correct_or_not("107", question3)
    question4 = input('\n"(56 - 6 x 2) : 4  ="\n')
    correct_or_not("11", question4)
    question5 = input('\n"2 x 12 - (96 : 3)  ="\n')
    correct_or_not("-8", question5)
    print_pause('\n"Okay! Let\'s check you amswers!"\n', 2)
    outcome = 0
    for result in answers:
        if result == "correct":
            outcome += 1
    if outcome == 4:
        print_pause('\n"Seems that you did pretty well! "\n', 2)
        return tools()
    if outcome == 5:
        print_pause('\n"You did EXCELLENT!! "\n', 2)
        return tools()
    if outcome <= 3:
        print_pause('\n"Mm... Sorry but you are not good at this! Come '
                    'back after some practice (or a lot!)"\n', 3)
        return knock()


def tools():
    global backpack
    print_pause('\n"Okay! I have some carpenter tools that I am sure you will'
                ' need, and you won them! So, here you have them!\nNow, let me'
                ' work! See you!"', 4)
    backpack.append("tools")
    return knock()


# !!!!! LEFT CHOICE !!!!!


def left_choice():
    path("left")
    print_pause("\nAfter a little walk you reach a rocky area, and next to it"
                " some wood logs.\n", 2)
    return rocky_logs()


def rocky_logs():
    choice = input("Would you like to go to the rocky area or look the logs?"
                   "\n\n1. Go to the rocky area\n2. Look at the logs\n")
    if choice == "1":
        return enter_cave()
    elif choice == "2":
        return look_loogs()
    else:
        print_pause(random.choice(invalid_input), 3)
        return rocky_logs()


def look_loogs():
    global backpack
    print_pause("\nUhmm...those logs look very useful!\n", 2)
    if "flowerpot" in backpack:
        print_pause("But you don't need more flowerpots!!! You go back.\n", 4)
        return woods_decision()
    elif "tools" in backpack:
        if visits_flor == 0:
            print_pause("\nYou could build something, but what? It will be"
                        " better to come back when you have something to build"
                        ".\n", 5)
            return woods_decision()
        else:
            print_pause("You use the carpenter tools to build a flowerpot!\n"
                        "Once you have it, you go back.\n", 5)
            backpack.append("flowerpot")
            return woods_decision()

    else:
        print_pause("But you really have nothing to do here...\nYou"
                    " go back.\n", 4)
        return woods_decision()


def enter_cave():
    entercave = input("\nIt seems that there is a cave, do you want to enter"
                      "?\n\n1. Yes\n2. No\n")
    if entercave == "1":
        return cave()
    elif entercave == "2":
        print_pause("\nOkay, then you walk back to the crossroad.\n", 1)
        return woods_decision()
    else:
        print_pause(random.choice(invalid_input), 3)
        return enter_cave()


def cave():
    print_pause("\nUhh it's very dark in here!!\n", 3)
    print_pause("Okay, there are many possible paths in here.\n\nThis is like"
                " a maze!!!\nAt each crossroad you will be asked if you want "
                "to go left or right. If you know the order to follow, you mi"
                "ght find somthing really important, but if you don't, you mu"
                "st be careful, you can get lost!\n", 9)
    print_pause("Now, let's make this easier.\n", 3)
    return laberint()


def laberint():
    print_pause("When you want to go to the right you enter 'R', and when you"
                " want to go to the left you enter 'L'.\n\nLet's start then"
                "!", 2)
    return laberint_loop()


crossroad_cave = ["\nIn this crossroad, do you want to go to the right or to "
                  "the left?\n(R/L)\n", "\nIn this other crossroad, right or "
                  "left?\n(R/L)\n", "\nMmm you have to choose again, right or"
                  " left?\n(R/L)\n", "\nAnother crossroad!! Do you want to go"
                  " to the right or to the left?\n(R/L)\n"]


def laberint_loop():
    half_correct_order = ["right", "left", "right", "left"]
    correct_order = ["right", "left", "right", "left", "right", "left", "left",
                     "left"]
    choosen_order = []
    tries = 0
    while tries < 3:
        for crossroads in crossroad_cave:
            time.sleep(2)
            choice = input(crossroads).lower()
            if "l" in choice:
                choosen_order.append("left")
            elif "r" in choice:
                choosen_order.append("right")
            else:
                print_pause("You are not doing this correctly, let's start"
                            " again!\n\n", 2)
                return laberint()
        tries += 1
        if choosen_order != half_correct_order:
            if choosen_order == correct_order:
                return tresor()
            else:
                decision = input("\nI think you are getting lost. If I was"
                                 " you I would turn around. Do you want "
                                 "to?\n\n1. Yes\n2. No\n")
                if decision == "1":
                    print_pause("\nGood choice!", 3)
                    return enter_cave()
                elif decision == "2":
                    print_pause("\nMmm...As you wish...\n", 1)
                else:
                    print_pause("You are not doing this correctly, let's start"
                                " again!\n\n", 2)
                    return laberint_loop()
    return roof_falls()


def roof_falls():
    print_pause("\nGHJKHDF!! Oh..WHAT'S HAPPENING?!\n", 1)
    for x in range(3):
        print_pause("\nTHE ROOF FALLS!!\n", 1)
        print_pause("\nAhhhhhhh!!\n", 1)
        print_pause("\nPuum!Katapumm!!pummm!katakaka!!!!!\n", 1)
    print_pause("\n.\n.\n.\n.\n.\n", 2)
    print_pause("\nIt's too late to get out of here.....\n\nYou "
                "die buried between rocks...", 5)
    return bad_ending()


def tresor():
    global backpack
    print_pause("\nOh!!! Seems like you have arrived somewhere!\n\n", 3)
    print_pause("And...What's that!?!\nLooks like a treasure!!!", 4)
    if "key" in backpack:
        print_pause("\nMaybe the key that that mysterious person gave to you "
                    "works here..Let's try!\n", 4)
        print_pause("\nIt does!!!", 3)
        print_pause("\nAnd here there is enough money to pay for the ship!! "
                    "Congratulations, you'll finally be able to get out of "
                    "here.\nBut first, let's find the way out of this cave.",
                    8)
        backpack.append("pesos")
        print_pause("\nYou leave the cave behind and you are now in the cros"
                    "sroad in the woods.\n", 3)
        return woods_decision()
    else:
        print_pause("\nOh...but it's closed! You will have to get the key fi"
                    "rst... ", 4)
        print_pause("\n\nYou leave the cave behind and you are now in the cros"
                    "sroad in the woods.\n", 3)
        return woods_decision()


# !!!!!!! PORT !!!!!!!


def port():
    print_pause("\nYou are in the train. It stops, the doors open and you can "
                "see an old port in front of you.", 3)
    return port_decision()


def port_decision():
    decision = input("\nThere's a small " + color1 + " boat and a man in front"
                     " of it. Also, on the right there is a woman on the "
                     "floor, looking sick.\nWould you rather go talk to the "
                     "man or to the woman, or you prefer to go back to the "
                     "train station?\n\n1. Talk to the man\n2. Talk to the wo"
                     "man\n3. Go back to the train station\n")
    if decision == "2":
        return talk_woman()
    elif decision == "1":
        return talk_man()
    elif decision == "3":
        return train_station()
    else:
        print_pause(random.choice(invalid_input), 2)
        return port_decision()


# !!!!! WOMAN !!!!!


def talk_woman():
    global visits_woman
    if visits_woman == 0:
        if "medicine" in backpack:
            print_pause('\n"Ohh.. ajjj...Who are you? What do you need from'
                        ' me?"\n', 3)
            print_pause('\n\"Wait! You have an antibiotic I need! Thank you '
                        'for giving it to me! In return I\'ll tell you a  '
                        'secret:\n', 2)
            womans_secret()
            visits_woman += 1
            return port_decision()
        else:
            print_pause('\n"Ohh.. ajjj...Who are you? What do you need from'
                        ' me?"\n', 3)
            print_pause('"Well... I don\'t really care about your things...\n'
                        'But if you bring an antibiotic to me I\'ll tell you a'
                        ' super interesting piece of information, that for '
                        'sure will open some doors for you."', 7)
            print_pause("\n\nIt seems that without that antibiotic this woman "
                        "will not tell you anything...It will be better to "
                        "go.", 4)
            visits_woman += 1
            return port_decision()
    else:
        if "medicine" in backpack:
            print_pause('\n"Oh!! You have my antibiotic!!! Thank you so much!'
                        '\nWell... A promise is a promise! I\'ll tell you a '
                        'secret: \n', 5)
            womans_secret()
            return port_decision()
        else:
            print_pause(random.choice(no_medicine), 4)
            return port_decision()


def womans_secret():
    print_pause("Very deep into the woods there's a little house, maybe yo"
                "u can find something useful there. But if you want to get"
                " inside there remember this word: " + password + ".\nNow, "
                "please leave me alone!\"", 5)
    print_pause("\n\nThat seems like a really important piece of information."
                " Keep it in mind!", 4)


no_medicine = ['\n"You are back. Why? If you want to talk first I '
               'need medicine. Bye."', '\n"Hey you! I see you don\'t'
               ' have my medicine, come back when you\'ve got it."',
               '\n"Please tell me you\'ve got the medicine! Oh, I '
               'see, you don\'t have it yet. Go away!"']


# !!!!! MAN !!!!!


def talk_man():
    global visits_man
    if visits_man == 0:
        input(f'\n"Hello! My name is {man_name} and I\'m the captain of this '
              'ship. Leaving this island will cost you 2000 pesos. Do you '
              'have them?"\n\n1. Yes\n2. No\n')
        return pesos()
    else:
        input('\n"Hello! Do you have the 2000 pesos?"\n\n1. Yes\n2. No\n')
        return pesos()


def pesos():
    global visits_man
    if "pesos" in backpack:
        print_pause('\n"I see you do!! Get on board!"', 3)
        print_pause("\n\nYou have finally gotten off this island.\nYou go "
                    "home. ", 4)
        print_pause("\n\nCONGRATULATIONS!! YOU WON!!!", 6)
        return play_again()
    else:
        print_pause('\n"Mmm no, you don\'t. Come back when you can pay.'
                    '"', 2)
        visits_man += 1
        return port_decision()


# !!!!!!! VILLAGE !!!!!!!


def village():
    print_pause("\nThrough the window you can see some houses.\n", 2)
    print_pause("\nSuddenly the train stops and you get off at the main "
                "square.\n", 3)
    return village_decision()


def village_decision():
    print_pause("\nJust in front of you there is a little pharmacy. On your "
                "right hand you can see a bar, and on you left hand there is"
                " a florist.", 3)
    choice = input("\nWhere would you like to go?\n\n1. To the pharmacy\n2. To"
                   " the bar\n3. To the florist\n4. Go back to the train stati"
                   "on\n")
    if choice == "1":
        return pharmacy()
    elif choice == "2":
        return bar()
    elif choice == "3":
        return florist()
    elif choice == "4":
        return train_station()
    else:
        print_pause(random.choice(invalid_input), 3)
        return village_decision()


# !!!!! PHARMACY !!!!!


def pharmacy():
    open_or_closed = random.choice(["open", "open", "closed"])
    print_pause("\nYou go to the pharmacy.\n", 2)
    if open_or_closed == "closed" or "medicine" in backpack:
        print_pause('\nBut... there is a poster on the door that says: "'
                    'Sorry, but we are closed now. Come later!"\n\nOh! Seems'
                    ' like you will have to go back to the square.\n', 7)
        return village_decision()
    else:
        print_pause("\nIt's open, so you go into the shop.\n", 2)
        return inside_pharmacy()


def inside_pharmacy():
    if visits_pharmacy == 0:
        return pharmacy_first()
    else:
        return pharmacy_else()


def pharmacy_first():

    def pharmacy_welcome():
        answer = input('\n"Hi!! How can I help you?"\n\n1. I need a sedative\n'
                       '2. I need antibiotic\n3. I need band-aids\n')
        if answer == "2":
            print_pause('\nDo you want an antibiotic? Mmm...but you don\'t'
                        ' have money...Well, there\'s something you could'
                        'do!"\n', 5)
            return two_pots()
        if answer == "1" or answer == "3":
            print_pause('\n"I am sorry but I don\'t have any left!"\n', 4)
            return pharmacy_welcome()
        else:
            print_pause(random.choice(invalid_input), 2)
            return pharmacy_welcome()

    def two_pots():
        global visits_pharmacy
        print_pause("\n\"I have these two pots. One is antibiotic and the othe"
                    "r is poison.\"\n\"I have no idea which is which, "
                    "but there is a lady called Yose, that may help us with "
                    "that. She works in the bar.\"\n\n\"Come back after ta"
                    "lking to her and I will know the correct one.\"\n",
                    9)
        print_pause("\nYou go to the square again.", 3)
        visits_pharmacy += 1
        return village_decision()

    return pharmacy_welcome()


def pharmacy_else():
    global backpack
    talked = input('\n"Hello again! Have you talked to Yose?"\n\n1. Yes\n2. No'
                   '\n')
    if talked == "1":
        print_pause('\n"Cool!! So now you know which one is the good one!"\n',
                    3)
        print_pause('"Now, you tell me the color of the good pot, but, '
                    'you will have to taste the one you choose, so if you '
                    'choose the wrong one you will drink POISON!"\n', 6)
        return what_color()
    elif talked == "2":
        print_pause('\n"Oh..Sorry, but I can\'t help you until you talk to her'
                    '. Bye!"', 5)
        print_pause("\nYou go back to the square.\n", 4)
        return village_decision()
    else:
        print_pause(random.choice(invalid_input), 4)
        return pharmacy_else()


def what_color():
    color = input(f'\n"So, {color1} or {color2}?"\n\n1. {color1}\n2. {color2}'
                  '\n3. Go back\n')
    if color == "1":
        print_pause("\n\nYou drink a little bit and..........\n\nYou're "
                    "fine!!!!!\n\nNow, you leave with your antibiotic.", 5)
        backpack.append("medicine")
        return village_decision()
    elif color == "3":
        print_pause("\nYou have turned back, and you are in the square "
                    "again.", 5)
        return village_decision()
    elif color == "2":
        print_pause("\nYou drink a little bit and..........\n\nNOOOOOO!!!!"
                    "\n\nIt was POISON!\n", 6)
        return bad_ending()
    else:
        print_pause(random.choice(invalid_input), 3)
        return what_color()


# !!!!! FLORIST !!!!!

instructions = ('\n"If you want to stop the loop, remember: RIGHT, LEFT,'
                ' RIGHT, LEFT, RIGHT, LEFT, LEFT, LEFT."\n')


def florist():
    print_pause("\nYou go into the florist.\n", 4)
    global visits_flor
    if visits_flor == 0:
        return florist_first()
    else:
        return florist_else()


def florist_first():
    global visits_flor
    global player_name
    if player_name == "":
        print_pause('\n"Hey!!! Welcome! Someone told me you were here and I wa'
                    's waiting for you.\nThere is something I need from you'
                    ' and in return I\'ll give you some valuable instruction'
                    's."\n',
                    5)
        player_name = input('\n"But first, what\'s you name?"\n')
        print_pause('\n"Cool!"\n', 2)
        visits_flor += 1
        return need_flowerpot()
    else:
        print_pause('\n"Hey!!! Welcome! I was waiting for you. You are '
                    '' + player_name + ', aren\'t you?"\n', 4)
        print_pause('"There is something I need from you and in return I\'ll'
                    ' give you some valuable instructions."\n', 6)
        visits_flor += 1
        return need_flowerpot()


def florist_else():
    print_pause('"Hello ' + player_name + '!"', 3)
    if "flowerpot" in backpack:
        print_pause('\n"I see you have managed to build the flowerpot. Thank'
                    ' you so much!"', 4)
        print_pause(f'\n"Here are the instructions:"\n\n{instructions}', 6)
        print_pause('\n"I\'m sure you will know what to do '
                    'with them."\n\n"See you!"', 4)
        return village_decision()
    else:
        print_pause('"You don\'t have the flowerpot yet. Come back when you '
                    'have it built."', 5)
        return village_decision()


def need_flowerpot():
    print_pause('\n"Look, I need a flowerpot and I thought you could make'
                ' it with some tools and some wood from the woods."\n\n"I\'ll'
                ' be waiting for you!!!! Bye!"\n', 6)
    print_pause("\n\nWOW! That sounded like a very important thing to do!"
                "\nBut for now, you go back to the square!", 5)
    return village_decision()


# !!!!! BAR !!!!!


def bar():
    print_pause("\nYou go into the bar.\n", 4)
    print_pause("\nOnce inside, you go to the bar counter and...\n", 2)
    return bar_counter()


def bar_counter():
    drink = input('"Good afternoon! Can I offer'
                  ' you a drink? I have water and beer. What will you have?"\n'
                  '\n1. Water\n2. Beer\n')
    if drink == "1":
        print_pause('\n"Okay! Here you have your glass of water!"\n', 2)
        if visits_mystery == 0:
            return water()
        else:
            return bar_again("water")
    elif drink == "2":
        print_pause('\n"Okay! Here you have your beer!"\n', 2)
        if "medicine" in backpack:
            return bar_again("beer")
        else:
            return beer()
    else:
        print_pause(random.choice(invalid_input), 3)
        return bar_counter()


def water():
    global visits_mystery
    global backpack
    print_pause("\nYou take the glass and go take a seat at a table on the "
                "corner.\nAfter a few minutes, a mysterious person comes"
                " and sits next to you.\n", 5)
    print_pause('\n"Hi, I was waiting for you. She told me to give this to you'
                '. I must go now. Bye."\n', 5)
    print_pause("\nMmm that was quite strange... But let's see what (s)he "
                " gave to you.\nOh, it's a key! Keep it safe!!\n", 6)
    visits_mystery = 1
    backpack.append("key")
    return leave()


def leave():
    print_pause("\nYou stand up and go back to the square.\n", 4)
    return village_decision()


def beer():
    global visits_yose
    print_pause("\nYou take a seat at the bar counter. Immediately the barman"
                " starts talking to you:\n", 6)
    if visits_yose == 0:
        person = input('\n"So..I have never seen you around here. You are new,'
                       ' eh? Mm..you look very expectant.\nLet me guess, you '
                       'are looking for someone, eh? You do, eh? So, tell me, '
                       'who are you looking for?"\n\n1. Yose\n2. Gina\n3. '
                       'Laia\n4. Mercè\n')
    else:
        person = input('\n"So tell me, who are you looking for?"\n\n1. Yose\n2'
                       '. Gina\n3. Laia\n4. Mercè\n')
    if visits_pharmacy != 0:
        if person == "1":
            print_pause('\n"Oh yes! I know her! She is just there! Come!"', 4)
            print_pause('\n\n"Hello, I\'m Yose."', 3)
            visits_yose = 1
            return yose()
        elif person == "2" or person == "3" or person == "4":
            print_pause('\n"Uhuh..Sorry, I don\'t know her."\n', 3)
            visits_yose = 1
            return leave()
        else:
            print_pause(random.choice(invalid_input), 2)
            return beer()
    elif visits_pharmacy == 0:
        print_pause('\n"I can\'t help you with this now. Sorry,'
                    ' but I think you should leave."\n', 4)
        visits_yose = 1
        return leave()


def yose():
    medihelp = input('\n"Oh wait! You are here for that thing about the medic'
                     'ine, aren\'t you?"\n\n1. Yes\n2. No\n')
    if medihelp == "1":
        print_pause('\n"Okay, look. I\'m just gonna tell you one thing. Look'
                    ' at the boat\'s color."\n"Hope that helps you! Bye!"', 6)
        return leave()
    if medihelp == "2":
        print_pause('\n"Then, there\'s nothing I can help you with, sorry"',
                    4)
        return leave()
    else:
        print_pause(random.choice(invalid_input), 3)
        return yose()


def bar_again(drink):
    print_pause(f"\nYou finish your glass of {drink}, and then you leave.", 5)
    return village_decision()


# !!!!!!! END !!!!!!!


def bad_ending():
    print_pause("\nGAME OVER!", 5)
    return play_again()


def play_again():
    again = input("\n\nDo you want to play again?\n\n1. Yes\n2. No\n")
    if again == "1":
        return welcome()
    elif again == "2":
        print_pause("\nOK! See you when you feel like playing again!\n", 5)
        return False
    else:
        print_pause(random.choice(invalid_input), 4)
        return play_again()
    return False


while True:
    welcome()
    break
