from Spy_details import spy_name, spy_salutation, spy_age, spy_rating, spy_is_online

print "Hello!\nLet's get started!\nWelcome to spy chat!"
question1 = "Do you want to continue as %s %s?(Y/N)" % (spy_salutation, spy_name)
existing_spy = raw_input(question1)

STATUS_MSG = []


def update_status(status):
    if status is None:
        print "You don't have any status."
        new_status = raw_input("What status message do you want to set?\n")
        if len(new_status) > 0:
            STATUS_MSG.append(new_status)
            print STATUS_MSG
            status = new_status
    else:
        print "Your current status is [%s] " % status
        default = raw_input("Do you want to select from older status? (y/n) ")
        if default.upper() == 'N':
            new_status = raw_input("What status message do you want to set?\n")
            if len(new_status) > 0:
                STATUS_MSG.append(new_status)
                print STATUS_MSG
                status = new_status
        elif default.upper() == 'Y':
            pos = 1
            for msg in STATUS_MSG:
                print "%d. %s" % (pos, msg)
                pos += 1
            x = input("Select the number corresponding to the status you want to set.")
            status = STATUS_MSG[x - 1]
            if x > pos:
                print "Incorrect choice. Choose a correct option."
                return None
    return status


Outer_List = []


def add_friend():
    Spy_Friends = []
    new_name = raw_input("Please add your friend's name: ")
    new_age = input("Age?")
    new_rating = input("Spy rating?")

    if len(new_name) > 0 and 50 > new_age > 12 and spy_rating <= new_rating < 5.0:
        Spy_Friends.append(new_name)
        Spy_Friends.append(new_age)
        Spy_Friends.append(new_rating)
        Outer_List.append(Spy_Friends)
        print Outer_List
    else:
        print "Sorry! Invalid entry. We can't add spy with the details you provided"


def start_chat(spy_name, spy_age, spy_rating):
    status = None
    spy_name = spy_salutation + " " + spy_name
    if 12 < spy_age < 50:
        print "Authentication complete. \nWelcome %s (age %d  and spy rating %.1f)\nProud to have you with us!" % (
            spy_name, spy_age, spy_rating)
        show = True
        while show:
            question2 = "What would you like to do?\n1. Update Status.\n2. Add a friend. \n3. Send a secret message. " \
                        "\n4. Read a secret message. \n5. Read chats from a user. \n6. Exit\n "
            menu_choice = input(question2)
            if menu_choice == 1:
                status = update_status(status)
                print status
            elif menu_choice == 2:
                add_friend()
            elif menu_choice == 6:
                print "Thanks for visiting spy_chat! Logging out..."
                show = False


if existing_spy.upper() == 'Y':
    start_chat(spy_name, spy_age, spy_rating)
else:
    # Check if the length of the string entered is more than zero and is alphabets (not numerals or spl characters)
    spy_name = raw_input("What is your name? ")
    if len(spy_name) > 0 and spy_name.isalpha():
        spy_salutation = raw_input("What should I call you (Mister or Miss)? ")
        # Check if the salutation is correct
        if spy_salutation == "Mister" or spy_salutation == "Miss" or spy_salutation == "mister" or spy_salutation == "miss" or spy_salutation == "Mr" or spy_salutation == "Ms" or spy_salutation == "mr" or spy_salutation == "ms":
            spy_name = spy_salutation + " " + spy_name
        else:
            print "You haven't typed the right salutation! \nExiting SpyChat..."
            exit(0)
        print "Alright " + spy_name + ". I'd like to know a little bit more about you before we proceed..."
        spy_age = 0
        spy_rating = 0.0
        spy_is_online = False
        spy_age = int(spy_age)
        spy_age = input("What is your age?")
        if 12 < spy_age < 50:
            spy_rating = input("What is your spy rating?")
            if spy_rating > 5.0:
                print "You are a fake spy! The rating is up to 5.0 only!"
                exit(0)
            elif 4.5 < spy_rating <= 5.0:
                print "Great ace!"
            elif 3.5 < spy_rating <= 4.5:
                print "You are one of the good ones."
            elif 2.5 <= spy_rating <= 3.5:
                print "You can always do better"
            else:
                print "We can always use somebody to help in the office."
            spy_is_online = True
            start_chat(spy_name, spy_age, spy_rating)
        else:
            print "You are not of the age to be a spy!:'("
    else:
        print "You aren't a real spy!!"
