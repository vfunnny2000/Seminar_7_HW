# from colorama import init
# from colorama import Fore, Back, Style
import os
import csv

# use Colorama to make Termcolor work on Windows too
# init()

def add_user(dictionary: dict):
    """
    Add new user
    :param dictionary:
    :return:dictionary
    """
   
    name = input('Enter name for abonent: ')
    phone = input('Enter phone number for abonent: ')
    if name in dictionary:
       print('This abonent already exist: Name: {} - Phone: {}'.format(name, dictionary[name]))
    else:
        dictionary[name] = phone
        print('New abonent "{}" is created'.format(name))
    return dictionary


def delete_user(dictionary: dict):
    """
    Deleted user
    :param dictionary:
    :return: dictionary
    """
    
    name = input('Enter name for abonent: ')
    if name in dictionary:
        dictionary.pop(name)
        print('Abonent "{}" is deleted'.format(name))
    else:
        print('Sorry, this abonent not exist')
    return dictionary


def update_user(dictionary: dict):
    """
    Update user number
    :param dictionary:
    :return: dictionary
    """
    name = input('Enter name for abonent: ')
    phone = input('Enter New phone number for abonent: ')
    if name in dictionary:
        dictionary[name] = phone
        print('Abonent "{}" is updated'.format(name))
    else:
        print('Sorry, this abonent not exist')
    return dictionary


def search_user(dictionary: dict):
    """
    Search user (Name or number)
    :param dictionary:
    :return: dictionary
    """
    
    search_value = input('Enter name or phone number for abonent: ')
    name_in_dict = False
    for key, value in dictionary.items():
        if key.lower() == search_value.lower() or value == search_value:
            print('Name: "{}" - Number: "{}"'. format(key, value))
            name_in_dict = True
    if name_in_dict == False:
        print('Sorry, this abonent not exist')


def print_phonebook(dictionary: dict):
    """
    Print all phonebook
    :param dictionary:
    :return: None
    """
   
    for key, value in dictionary.items():
        print('Phonebook Numbers: ' + '\n' + 'Name: "{}" - Number: "{}"'. format(key, value))


def read_file():
    """
    read from file phonebook.csv
    :return: phonebook
    """
    check_file = os.path.exists('./phonebook.csv')
    if check_file is True:
     
        with open('./phonebook.csv') as file:
            phonebook_from_file = csv.reader(file, delimiter = ",")
            phonebook = {}
            for abonent in phonebook_from_file:
                if len(abonent) > 0:  
                    phonebook[abonent[0]] = abonent[1]              
        return phonebook
    else:
        return dict()


def write_file(dictionary: dict):
    """
    write in file phonebook.csv
    :param dictionary:
    :return: None
    """
    with open('./phonebook.csv', 'w') as file:
        writing_file = csv.writer(file)
        for name, number in dictionary.items():
            writing_file.writerow([name, number])
            
    
    with open('./phonebook_1.csv', 'w') as file:
        writing_file = csv.writer(file)
        for name, number in dictionary.items():
            writing_file.writerow([name])
            writing_file.writerow([number])
            writing_file.writerow([])
            