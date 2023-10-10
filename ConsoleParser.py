import os
import re

# Given a TF2 console log, this will extract chat messages recorded.
def parse_console(filename):
    
    ##### Private helper function. #####
    def clean_list(string_list):
        sl_2 = [item.replace("*DEAD* ", "").replace('*DEAD*', "").replace("\n", "").replace("(TEAM)", "") for item in string_list]
        ping_reg = re.compile("^\s+\d{1,4} ms")
        error_reg = re.compile("^Error:")
        bind_reg = re.compile("^\"\w+\"")
        mdl_reg = re.compile("\.mdl : ")
        return [item for item in sl_2 if not (ping_reg.search(item) or error_reg.search(item) or bind_reg.search(item) or mdl_reg.search(item))]
    #####################################
    
    assert isinstance(filename, str)
    assert ('.txt' in filename or '.log' in filename)
    
    string_list = []
    regexp = re.compile('.+( : ).+')
    no_ff = re.compile('(freak_fortress_2)')
    f = open(filename, 'r', encoding="utf-8")
    while True:
        try:
            line = f.readline()
            if not line:
                break
            if (regexp.search(line) and not no_ff.search(line)) or (") Connected" in line):
                string_list.append(line)
        except:
            pass
    return clean_list(string_list)

# Function to get recorded names via SteamID.
def instances_of_name(all_chat, steamid):
    name_list = []
    if steamid == None:
        return []
    steamid_string = f" ({steamid})"
    for chat in all_chat:
        if steamid in chat:
            new_name = chat.split(steamid_string)[0].lower()
            if new_name not in name_list:
                name_list.append(new_name)
    return name_list

# Function to restrict searches to a certain phrase from someone specific. If SteamID is provided, it will try to get messages from any recorded names.
def from_contains(name, text, all_chat, steamid=None):
    name_list = [name.lower()] + instances_of_name(all_chat, steamid)
    text = text.lower()
    text_reg = re.compile(rf" : .*{text}.*")
    chat_list = []
    
    for chat in all_chat:
        for known_names in name_list:
            name_reg = re.compile(rf".*{re.escape(known_names)}.* : ")
            if name_reg.search(chat.lower()) and text_reg.search(chat.lower()):
                chat_list.append(chat)
                break
                    
    return chat_list

# Function to restrict searches to a certain phrase.
def contains(text, all_chat):
    text = text.lower()
    text_reg = re.compile(rf" : .*{text}.*")
    chat_list = []
    for chat in all_chat:
        if text_reg.search(chat.lower()):
            chat_list.append(chat)
    return chat_list

# Function to restrict searches to a certain person. If SteamID is provided, it will try to get messages from any recorded names.
def from_user(name, all_chat, steamid=None):
    name_list = [name.lower()] + instances_of_name(all_chat, steamid)
    name_reg = re.compile(rf".*{name}.* : ")
    chat_list = []
    
    for chat in all_chat:
        for known_names in name_list:
            name_reg = re.compile(rf".*{re.escape(known_names)}.* : ")
            if name_reg.search(chat.lower()):
                chat_list.append(chat)
                break
    return chat_list