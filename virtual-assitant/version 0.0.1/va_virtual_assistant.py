"""
    This is the main script that runs the virtual assistant code.
"""

# we need all the functions from va_helpers. We can pick specific functions, 
# but in this case, we need all functions. So, we import all.
from va_helpers import *

session_is_active = True
user_has_been_greeted = False

# If the session_is_active variable is true, the code will continue to loop through this sequence of steps defined inside it.
while session_is_active:

    # greet the user if we have not done so already.
    if user_has_been_greeted == False:
        print("\n Good day, it’s your virtual assistant here - I am at your service.")
        # we set the user_has_been_greeted variable to true, to stop greeting the user 
        # if we have already greeted them in the session.
        user_has_been_greeted = True

    else:
        
        # if we've already greeted the user, that means they have performed an action.
        # so here we check if the user wants to perform more actions.
        user_answer = input ("is there anything else? Enter yes or no ")
        if user_answer == "no":
            print ("Okay, good bye now and have a lovely day")
            # using the break keyword, we can break out of the while loop
            break

    show_commands() # display the available commands to the user

    # get the users response for what command they want to run
    user_command_input = input ("please enter a valid command here... ")
    
    if user_command_input == "exit":
        print ("Okay, goodbye now and have a lovely day")
        add_delay()
        
        # Setting the session_is_active to False, will exit the while loop.
        session_is_active = False
    
    # The rest of the code here should be self-explanatory.
    elif user_command_input == "add event":
        add_user_event()
        add_delay()
        print ("operation successful")
    
    elif user_command_input == "view events":
        view_user_events()
        add_delay()
        print ("operation successful")
        
    elif user_command_input == "update event":
        update_user_event()
        add_delay()
        print ("operation successful")
        
    elif user_command_input == "delete event":
        delete_user_event()
        add_delay()
        print ("operation successful")
    
    else:
        # if the user enters a command, we do not recognize then we let them know.
        print ("sorry, you have entered an unrecognized command.")
        add_delay(1)
