"""
    This script provides the functionality to access and modify items in the database.
    because we have decoupled the db logic from the main app logic
    It lets us easily replace the db (i.e. from json files to sql) 
    without updating the main script code
"""

import json
event_db = "./db/event.json"

def read_events_db():
    # opens and reads the contents of the json file (our database)
    with open(event_db, 'rb') as database:
        return json.load(database)

def save_command(data):
    # reusable function to update the json file (our database)
    with open(event_db, "w") as database:
        database.write(data)  
        
def create_event(event_details):    
    db = read_events_db()
    # handle id increments for each event
    if len(db) == 0:
        event_details["id"] = 1
    else:
        # if we already have records, we append based on the last record entered
        event_details["id"] = db[-1]['id'] + 1
    
    # add new event to list of items
    db.append(event_details)
    
    # sort the items in db by id before saving them
    db = sorted(db, key=lambda item:item['id'])
    
    """
        you'll notice we are using a lambda function here.
        it's a short hand way of writing a function
        this lambda function is the same as doing:
            def return_id(item):
                return item['id']
            db = sorted(db, key=return_id)     
    """  
    
    # save the new list of events to the database
    save_command(json.dumps(db))
    
def view_events(filter_criteria=None):        
    db = read_events_db()
    if len(db) == 0:
        print("sorry no events, could be found.")
        return
    
    print("found events:")
    
    # if a filter criteria is provided, we search for items matching that criteria.
    if filter_criteria != None:
        for key, value in filter_criteria.items():
            search_result = [item for item in db if item[key] == value]
            # the above is known as list comprehension.
            # it is the same as doing the below:
            # search_result = []
            # for item in db:
            #     if item[key] == value:
            #         search_result.append(item)
    
    else:
        # if no filter criteria is provided, then we display the entire db.
        search_result = db
    
    if search_result == []:
        print ("no events match that criteria, please try again... ")
        return
    
    for event in search_result:
        
        # I normally would not name variables like this.
        # I am doing this only because i want the code to fit nicely on the page.
        # please make your variable names meaningful.
        
        id = event.get('id')
        name = event.get('name')
        s_dt = event.get('start_date')
        dur = event.get('duration')
        locale = event.get('location')
        
        # string interpolation using f"regular words {python_code}" 
        # allows us to mix regular string and python code.        
        print(f"""id:{id}, name:{name}, start date:{s_dt}, duration:{dur}, location:{locale}""")

def update_event(event_id, update_criteria):    
    db = read_events_db()
    search_result = [event for event in db if event.get('id') == event_id]
    event_item = search_result[0]
    
    # updating the event_item dictionary object. 
    for key, value in update_criteria.items():
        event_item[key] = value
    
    # delete old event by removing it from the list based on the id
    # yes list comprehension again.
    [db.remove(event) for event in db if event.get('id') == event_id]
    
    # add new one with updated details 
    db.append(event_item)
    
    db = sorted(db, key=lambda item:item['id'])
    save_command(json.dumps(db))
    
def delete_event(event_id):    
    db = read_events_db()
    [db.remove(event) for event in db if event.get('id') == event_id]
    save_command(json.dumps(db))
