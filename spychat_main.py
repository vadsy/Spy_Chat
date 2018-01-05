from Spy_details import spy_name, spy_salutation, spy_age, spy_rating, spy_is_online

print "Hello!\nLet's get started!\nWelcome to spy chat!"
question1 = "Do you want to continue as %s %s?(Y/N)" % (spy_salutation, spy_name)
existing_spy = raw_input(question1)


def start_chat(spy_name, spy_age, spy_rating, spy_is_online):
    status = None
    spy_name = spy_salutation + " " + spy_name
    if 12 < spy_age < 50:
        print "Authentication complete. \nWelcome %s (age %d  and spy rating %.1f)\nProud to have you with us!" % (
        spy_name, spy_age, spy_rating)
        show = True
        while (show):
            question2 = "What would you like to do?\n1. Update Status.\n2. Exit\n"
            menu_choice = input(question2)
            if menu_choice == 1:
                print "Write your status."
                status = raw_input()
                print "Status updated. %s" %status
            if menu_choice == 2:
                print "Thanks for visiting spy_chat! Logging out..."
                show = False


if existing_spy == 'Y' or existing_spy == 'y' or existing_spy == "Yes" or existing_spy == "yes":
    start_chat(spy_name, spy_age, spy_rating, spy_is_online)
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
            print ("Authentication complete. \n"
                   "Welcome %s (age %d  and spy rating %.1f)\n"
                   "Proud to have you with us!") % (spy_name, spy_age, spy_rating)
        else:
            print "You are not of the age to be a spy!:'("
    else:
        print "You aren't a real spy!!"
