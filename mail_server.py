from typing import Dict, List, Optional
from flask import Flask, request, jsonify
import pathlib
import uuid
import json


app = Flask(__name__) 
thisdir = pathlib.Path(__file__).parent.absolute() # path to directory of this file

# Function to load and save the mail to/from the json file

def load_mail() -> List[Dict[str, str]]:
    """
    Loads the mail from the json file

    Returns:
        list: A list of dictionaries representing the mail entries
    """
    try:
        return json.loads(thisdir.joinpath('mail_db.json').read_text())
    except FileNotFoundError:
        return []

def save_mail(mail: List[Dict[str, str]]) -> None:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)
    
    Summary: Saves the mail from the json file. 
    
    Arguments: "mail : List[Dict[str, str]]" , mail is the variable representing the list of dictionaries of the mail entries
    
    """
    thisdir.joinpath('mail_db.json').write_text(json.dumps(mail, indent=4))

def add_mail(mail_entry: Dict[str, str]) -> str:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)
    
    Summary: Adds a mail entry to the list of dictionaries representing the mail entries, and assigns this new mail entry a unique id. The list of mail entries is then saved.  
    
    Arguments: "mail_entry" is a dictionary with key:values that are both strings.
    
    Returns: Function returns the mail entry id (of type string)
    
    """
    mail = load_mail()
    mail.append(mail_entry)
    mail_entry['id'] = str(uuid.uuid4()) # generate a unique id for the mail entry
    save_mail(mail)
    return mail_entry['id']

def delete_mail(mail_id: str) -> bool:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)
    
    Summary: Removes a mail entry using its unique id. list.pop() can remove "the element at the specificed position" (source: https://www.w3schools.com/python/ref_list_pop.asp)
    
    Arguments: "mail_id" a string variable representing the unique id of a mail entry
    
    Returns: a boolean True if the mail entry matched with the input argument "mail_id" and was deleted and mail list was saved successfully. returns a boolean False in all other cases where entry['id'] does not match "mail_id." 
    """
    mail = load_mail()
    for i, entry in enumerate(mail):
        if entry['id'] == mail_id:
            mail.pop(i)
            save_mail(mail)
            return True

    return False

def get_mail(mail_id: str) -> Optional[Dict[str, str]]:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)
    
    Summary: Retrieves a specific mail entry by using its unique mail id as an input.
    
    Argument: "mail_id" is a string variable representing the unique id of a mail entry
    
    Returns: if mail_id matches with the unique id of one of the mail entries in mail list, then function returns that mail entry. if a match is not found, then the function will not return anything.
    """
    mail = load_mail()
    for entry in mail:
        if entry['id'] == mail_id:
            return entry

    return None

def get_inbox(recipient: str) -> List[Dict[str, str]]:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)
    
    Summary: creates an array called inbox, and adds the corresponding entry to inbox array based on who the recipient of the mail entry is. 
    
    Argument: "recipient" is a string variable
    
    Returns: the "inbox" array
    """
    mail = load_mail()
    inbox = []
    for entry in mail:
        if entry['recipient'] == recipient:
            inbox.append(entry)

    return inbox

def get_sent(sender: str) -> List[Dict[str, str]]:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)
    
    Summary: creates a new array called "sent". Function also adds a mail entry to the "sent" array if 'sender' value matches with the input argument. 
    
    Argument: "sender" is a string variable 
    
    Returns: the "sent" array
    """
    mail = load_mail()
    sent = []
    for entry in mail:
        if entry['sender'] == sender:
            sent.append(entry)

    return sent

# API routes - these are the endpoints that the client can use to interact with the server
@app.route('/mail', methods=['POST'])
def add_mail_route():
    """
    Summary: Adds a new mail entry to the json file

    Returns:
        str: The id of the new mail entry
    """
    mail_entry = request.get_json()
    mail_id = add_mail(mail_entry)
    res = jsonify({'id': mail_id})
    res.status_code = 201 # Status code for "created"
    return res

@app.route('/mail/<mail_id>', methods=['DELETE'])
def delete_mail_route(mail_id: str):
    """
    Summary: Deletes a mail entry from the json file

    Args:
        mail_id (str): The id of the mail entry to delete

    Returns:
        bool: True if the mail was deleted, False otherwise
    """
    # TODO: implement this function
    res = delete_mail(mail_id)
    return res
 

@app.route('/mail/<mail_id>', methods=['GET'])
def get_mail_route(mail_id: str):
    """
    Summary: Gets a mail entry from the json file

    Args:
        mail_id (str): The id of the mail entry to get

    Returns:
        dict: A dictionary representing the mail entry if it exists, None otherwise
    """
    res = jsonify(get_mail(mail_id))
    res.status_code = 200 # Status code for "ok"
    return res

@app.route('/mail/inbox/<recipient>', methods=['GET'])
def get_inbox_route(recipient: str):
    """
    Summary: Gets all mail entries for a recipient from the json file

    Args:
        recipient (str): The recipient of the mail

    Returns:
        list: A list of dictionaries representing the mail entries
    """
    res = jsonify(get_inbox(recipient))
    res.status_code = 200
    return res

# TODO: implement a route to get all mail entries for a sender
# HINT: start with soemthing like this:
@app.route('/mail/sent/<sender>', methods = ['GET','POST'])
def get_sent_route(sender: str):
	"""
	Summary: Gets all mail entries for a sender from the json file 
	
	Args:
		sender(str): the sender of the mail
	Returns:
		list: A list of dictionaries representing the mail entries
	"""
	res = jsonify(get_sent(sender))
	res.status_code = 200
	return res
	

if __name__ == '__main__':
    app.run(port=5000, debug=True)
