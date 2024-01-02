contacts = {} #initiates open dictionary

def new_contact(name = 'You forgot their name!', phone_number = 'no phone number :(', email = 'none :('): #defines add_contact function
    contacts[name] = [phone_number, email]
    print(f"{name} added to contacts with phone number: {phone_number} and email: {email}")

def add_contact():
    while True:
        new_contact(input('enter contact name:'), int(input('enter contact phone number:')), input('enter contact email:'))
        x = input('Add another?')
        if x == 'No' or x == 'no':
            break
        else:
            continue

def delete_contact(name): #defines delete_contact function
    if name in contacts:
        del contacts[name]
        print('{name} deleted from from contacts!')
    else:
        print('That contact does not exist!')

def delete_all(): #defines delete_all function
    while len(contacts) != 0:
        for key in list(contacts.keys()): #iterates through a list of contact's keys
            if key != 'none':
                del contacts[key]
    print('No more contacts!')


def find_contact(name): #defines find_contact function
    if name in contacts:
        print(f"{name}'s phone number is {contacts[name][0]} and their email is {contacts[name][1]}!")
    else:
        print('{name} is not in your contacts silly!')

class count: #counts the number of contacts
    def __init__(self):
        self.number = 0

    def contacts(self):
        for i in contacts:
            self.number += 1
        if self.number > 1:
            print(self.number, 'contacts')
        else:
            print(self.number, 'contact')

import csv

def save_contacts():
    with open("contacts.csv", "w", newline="") as fp: # Open a csv file for writing

        writer = csv.DictWriter(fp, fieldnames=contacts.keys()) # Create a writer object

        writer.writeheader() # Write the header row

        writer.writerow(contacts) # Write the data rows
        print('Contacts saved!')

if __name__ == "__main__":
    count = count()

    add_contact()

    print(contacts)
    count.contacts()