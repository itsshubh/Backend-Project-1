from spy_details import spy, friends
from steganography.steganography import Steganography
from datetime import datetime

status_messages = ['status1', 'status2', 'status3.' ]

#friends = []


print 'Hello!!'
# Backslash or Escaping Characters.
# Another way to do is using double quotes :->   "Let's ge started"
print'let\'s get started'

question = "Do you want to continue as " + spy['salutation'] + " " + spy['name'] + "(Y/N)?"
exiting = raw_input(question)


def add_status(current_status_message):

    updated_status_message = None

    if current_status_message != None:
        print 'Your current status message is %s \n' %(current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message you want to set? ")

        if len(new_status_message) > 0:
            status_messages.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == "Y":

        item_position = 1

        for message in status_messages:
            print "%d. %s" %(item_position, message)
            item_position += 1

        message_selection = int(raw_input("\n Choose from the above Messages "))

        if len(status_messages) >= message_selection:
            updated_status_message = status_messages[message_selection - 1]


    else:
        print "The option you chose is not valid..  Press either y or n."


    if updated_status_message:
        print 'Your updated status message is : %s' %(updated_status_message)
    else:
        print 'You did not update your status message.'

    return updated_status_message


def add_friend():

    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'chats' :[]
    }

    new_friend['name'] = raw_input("Please add your Friend's name: ")
    new_friend['salutation'] = raw_input("Are they Mr. or Mrs.?: ")
    new_friend['name'] = new_friend['salutation'] + new_friend['name']

    new_friend['age'] = int(raw_input("Enter your Friend's age: "))

    new_friend['rating'] = float(raw_input("what is the rating? "))

    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['age'] < 50 and new_friend['rating'] >= spy['rating']:   #todo check the condition
        friends.append(new_friend)
        print "Friend is added!! "
    else:
        print "SORRY.. Invalid Entry. We can't add this spy with the details given. "

    return len(friends)


def select_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s aged %d with rating %.1f is online' %(item_number + 1, friend['name'],
                                                            friend['age'], friend['rating'])
        item_number += 1

    friend_choice = raw_input("Choose from your Friends.. ")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


def send_message():
    friend_choice = select_friend()

    original_image = raw_input("What is the name of the image? ")
    output_path = 'output.jpg'
    text = raw_input("What is your secret message?? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = {
        'message': text,
        'time': datetime.now(),
        'sent_by_me': True
    }
    friends[friend_choice]['chats'].append(new_chat)

    print 'Your secret message image is ready..'


def read_message():

    sender = select_friend()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    new_chat = {
        'message' : secret_text,
        'time': datetime.now(),
        'sent_by_me' : False
    }
    friends[sender]['chats'].append(new_chat)
    print 'The secret message is '+ secret_text
    print 'Your secret message has been saved.'


def start_chat(spy_name, spy_age, spy_rating):

    current_status_message = None

    spy['name'] = spy['salutation'] + " " + spy['name']

    if spy['age'] > 12 and spy['age'] < 50:

        if spy['rating'] > 4.5:
            print 'You are an ACE!'
        elif spy['rating'] < 4.5 and spy['rating'] > 3.5:
            print 'You are one of GOOD ONE\'s'
        elif spy['rating'] < 3.5 and spy['rating'] > 2.5:
            print 'You can always do better'
        else:
            print 'You can help in office.'

        spy['is_online'] = True

        print 'Authentication completed! WELCOME.. %s of age %d rated %.1f. Proud to have you onboard ' %(spy['name'], spy['age'], spy['rating'])

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do??  \n 1.Add a status update. \n 2.Add a friend. \n 3.Send a secret message. \n4.read a Secret message. \n 5.Read chats from user \n 6. Close Application. \n"
            menu_choice = int(raw_input(menu_choices))

            #if len(menu_choices) > 0:
            #    menu_choice = menu_choices

            if menu_choice == 1:
                current_status_message = add_status(current_status_message)
            elif menu_choice == 2:
                number_of_friends = add_friend()
                print 'You have %d friends' %(number_of_friends)
            elif menu_choice == 3:
                send_message()
            elif menu_choice == 4:
                read_message()
            else:
                show_menu = False

    else:
        print "You are not of correct age to become a spy"


if  exiting.upper() == 'Y':
    start_chat(spy['name'], spy['age'], spy['rating'])
else:
    spy = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online': False
    }

    spy['name'] = raw_input('Welcome to spy chat, you must tell me your spy name first:')


    if len(spy['name']) > 0:

        spy['salutation'] = raw_input('What should we call you (Mr. or Mrs.)')
        print spy['salutation'] + ' ' + spy['name']


        print 'Alright ' + spy['name'] + ', before proceeding, I would like to know more about you.'

        spy['age'] = int(raw_input('Enter your Age.'))
        # to check the type of any variable we use :->  print type(spy_age)
        # And, as shown above to convert any type to different type we just do:->  int(variable_name)  or  float(variable_name)
        spy['rating'] = float(raw_input('Enter Rating'))

        spy_is_online = True
        start_chat(spy['name'], spy['age'], spy['rating'])
    else:
        print "Please enter a valid spy name."

# Todo Working on action
# todo mth library
# todo virtual environment
# todo next project use virtual environment
