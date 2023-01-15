"""
    The script contains functions that the va_virtual_assistant script needs to work.
    We have separated these functions to improve readability and code flexibility.
    Here we also handle the calls to the database functions kept in va_event_db.py
"""

import time
from va_event_db import create_event, view_events, delete_event, update_event

def add_delay(delay=2):
    # this function adds a time delay (2 seconds by default)
    # we do this so the user is not bombarded with messages in rapid succession
    time.sleep(delay)

def show_commands():
    # this function presents the list of available commands the user can select
    commands = [ "add event", "view events", "update event", "delete event", "exit"]
    print("please tell me what you'd like me to do:")
    for command in commands:
        print(f"\t {commands.index(command)}. {command}")
    print(f"\n")
    
def add_user_event():
    # This function handles creating a user event in the database
    # We get all the necessary input information from the user
    name = input("please enter event name... ")
    start_date = input("please enter event start date... ")
    duration = input("please enter event duration in days... ")
    location = input("please enter event location... ")
    
    # we save the information into a dictionary.
    input_values = {
        "name": name,
        "start_date": start_date,
        "duration": duration,
        "location": location,
    }
    
    # we perform some simple validation
    # if the user enters an empty value, we inform them and exit the function early
    # we could add more validation steps and separate it into its own function.
    
    for key, value in input_values.items():
        if value == "":
            print ("unable to save event", key, "information missing.")
            return
    
    # if all is well, we save the data to the datastore
    create_event(input_values)
    
def delete_user_event():
    # This function deletes a user from the database
    event_id = input("please enter event id... ")
    delete_event(int(event_id))

def view_user_events():
    # This function displays the events on the screen to the user.
    filter_criteria = input("enter search query e.g. location=london or press enter for all events... ")
    
    # remove any leading and trailing whitespace from the user input
    # then check if the user’s input is empty
    # if its empty we set it to none, and pass it to the view_events function
    if filter_criteria.strip() == "":
        filter_criteria = None
        
    else:
        # split by the equal sign to get our key, value pairing for the view events function
        filter_criteria = filter_criteria.split("=")
        # replace space with underscore, since we don’t have spaces in out DB keys
        filter_key = filter_criteria[0].replace(" ", "_")
        filter_value = filter_criteria[1]
        filter_criteria = {filter_key:filter_value}
    
    return view_events(filter_criteria)

def update_user_event():
    # This function updates the users details
    event_id = input("please enter event id and values to be updated... ")
    update_criteria = input("please enter update criteria e.g. location=houston... ")
    
    # split by the equal sign to get our key, value pairing for the update events function
    criteria = update_criteria.split("=")
    update_key = criteria[0].replace(" ", "_")
    update_value = criteria[1]
    criteria = {update_key:update_value}
    
    return update_event(int(event_id), criteria)
