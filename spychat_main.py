import csv
from steganography.steganography import Steganography
from datetime import datetime
from Spy_details import Person, ChatMessage
from Spy_details import spy, f1, msg

print "Hello!\nLet's get started!\nWelcome to spy chat!"
question1 = "Do you want to continue as %s %s?(Y/N)" % (spy.salutation, spy.name)
existing_spy = raw_input(question1)

STATUS_MSG = []
friends = []


# ************************************************************VALIDATE DATA*********************************************************
def validate_data(v_name, v_salutation, v_age, v_rating):
    if len(v_name) > 0:
        if v_salutation.upper() == "MR" or v_salutation.upper() == "MS":
            if 12 < v_age < 50:
                if 0.0 < v_rating < 5.0:
                    return True


# ***************************************************************STATUS************************************************************
def update_status(Status):
    if Status is None:
        print "You don't have any status."
        new_status = raw_input("What status message do you want to set?\n")
        if len(new_status) > 0:
            STATUS_MSG.append(new_status)
            print STATUS_MSG
            Status = new_status
    else:
        print "Your current status is [%s] " % Status
        default = raw_input("Do you want to select from older status? (y/n) ")
        if default.upper() == 'N':
            new_status = raw_input("What status message do you want to set?\n")
            if len(new_status) > 0:
                STATUS_MSG.append(new_status)
                print STATUS_MSG
                Status = new_status
        elif default.upper() == 'Y':
            pos = 1
            for msg in STATUS_MSG:
                print "%d. %s" % (pos, msg)
                pos += 1
            x = input("Select the number corresponding to the status you want to set.")
            Status = STATUS_MSG[x - 1]
            if x > pos:
                print "Incorrect choice. Choose a correct option."
                return None
        else:
            print"Wrong option. status won't be changing."
    return Status


# *********************************************************Add a Friend************************************************************
def add_friend():
    new_friend = Person('', '', 0, 0.0)
    new_friend.name = raw_input("Please add your friend's name : ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.? : ")
    new_friend.name = "%s.%s" % (f1.salutation, f1.name)
    new_friend.age = input("What's your friend's age? ")
    new_friend.rating = input("What's your friend's spy rating? ")

    if len(new_friend.name) > 0 and new_friend.age >= 12 and new_friend.rating >= 3.0:

        friends.append(new_friend)
        print "Friend Added!"
    else:
        print "Sorry! Invalid entry. We can't add spy with the details you provided"
    with open('friends.csv', 'a') as friends_data:
        write = csv.writer(friends_data)
        write.writerow([new_friend.name, new_friend.salutation, new_friend.age, new_friend.rating])
    return len(friends)


# ***************************************************SELECT FRIEND METHOD************************************************************
def select_friend():
    item_number = 0
    for friend in friends:
        print "%d%s aged %d with rating %.2f is online" % (item_number + 1, friend.name, friend.age, friend.rating)
        item_number = item_number + 1
    friend_choice = input("Choose from your friends")
    friend_choice_position = friend_choice - 1
    return friend_choice_position


# *************************************************SEND MESSAGE FUNCTION************************************************************8
def send_message():
    friend_choice = select_friend()
    original_image = raw_input("What is the name of the image?")
    if '.jpg' in original_image or '.jpeg' in original_image:
        output_path = "output.jpg"
        text = raw_input("What do you want to say? ")
        Steganography.encode(original_image, output_path, text)
        msg.message = text
        msg.sent_by_me = True
        friends[friend_choice].chats.append(msg)
        with open('chats.csv', 'a') as msg_data:
            write = csv.writer(msg_data)
            write.writerow([msg.message, msg.time, msg.sent_by_me])
        print "Your secret message image is ready!"
    else:
        print "Not valid."


# *********************************************Method for reading Secret messages****************************************************
def read_message():
    sender = select_friend()
    output_path = raw_input("What is the name of the file?")
    text = Steganography.decode(output_path)
    msg.message = text
    msg.sent_by_me = False
    friends[sender].chats.append(msg)
    with open('chats.csv', 'a') as msg_data:
        write = csv.writer(msg_data)
        write.writerow([msg.message, msg.time, msg.sent_by_me])
    friends[sender].chats.append(msg)
    print "Your message is:"
    print msg.message
    print "Your secret message has been saved!"


def load_friends():
    with open('friends.csv', 'rb') as friends_data:
        reader = csv.reader(friends_data)

        for row in reader:
            x = Person(name=row[0], salutation=row[1], age=int(row[2]),  rating=float(row[3]))
            friends.append(x)
            #print friends
            print (", ".join(row))


# ***********************************************************Start Chat************************************************************
def start_chat(Spy):
    Status = None
    Spy.name = Spy.salutation + " " + Spy.name
    if 12 < Spy.age < 50:
        print "Authentication complete. \nWelcome %s (age %d  and spy rating %.1f)\nProud to have you with us!" % (
            Spy.name, Spy.age, Spy.rating)
        Show = True
        while Show:
            question2 = "What would you like to do?\n1. Update Status.\n2. Add a friend. \n3. Send a secret message. " \
                        "\n4. Read a secret message. \n5. Read chats from a user. \n6. Exit\n "
            menu_choice = input(question2)
            if menu_choice == 1:
                Status = update_status(Status)
                print Status
            elif menu_choice == 2:
                num = add_friend()
                print "You currently have %d friends!" % num
            elif menu_choice == 3:
                send_message()
            elif menu_choice == 4:
                read_message()
            elif menu_choice == 6:
                print "Thanks for visiting spy_chat! Logging out..."
                Show = False


# ********************************************************Checks for default user**************************************************
if existing_spy.upper() == 'Y':
    print "Loading friends"
    load_friends()
    print "Loaded friends"
    start_chat(spy)
elif existing_spy.upper() == 'N':
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
        spy = {'name': '', 'salutation': '', 'age': input("What is your age?"), 'rating': 0.0, 'is_online': False}
        if 12 < spy['age'] < 50:
            spy['rating'] = input("What is your spy rating?")
            if spy['rating'] > 5.0:
                print "You are a fake spy! The rating is up to 5.0 only!"
                exit(0)
            elif 4.5 < spy['rating'] <= 5.0:
                print "Great ace!"
            elif 3.5 < spy['rating'] <= 4.5:
                print "You are one of the good ones."
            elif 2.5 <= spy['rating'] <= 3.5:
                print "You can always do better"
            else:
                print "We can always use somebody to help in the office."
            spy['is_online'] = True
            print "Authentication complete. \nWelcome %s (age %d  and spy rating %.1f)\nProud to have you with us!" % (
            spy['name'], spy['age'], spy['rating'])
            show = True
            status = None
            while show:
                question2 = "What would you like to do?\n1. Update Status.\n2. Add a friend. \n3. Send a secret message. " \
                            "\n4. Read a secret message. \n5. Read chats from a user. \n6. Exit\n "
                menu_choice = input(question2)
                if menu_choice == 1:
                    status = update_status(status)
                    print status
                elif menu_choice == 2:
                    add_friend()
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 6:
                    print "Thanks for visiting spy_chat! Logging out..."
                    show = False

        else:
            print "You are not of the age to be a spy!:'("
    else:
        print "You aren't a real spy!!"
else:
    print "Wrong option press either y or n."
