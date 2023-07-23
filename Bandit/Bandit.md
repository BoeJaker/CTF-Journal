Blind CTF

im not using the hints


0. bandit0

    ls

    cat readme

1. NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL

    cat ./*

2. rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi

    cat "spaces in this filename"

3. aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG 

    ls -a ./inhere
    cat ./inhere/.hidden

4. 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe

    ls -a ./inhere
    cat ./*
    There is a segment of the output that looks like a flag in the 7th file
    cat "./-file07"

5. lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR

    ls -a

    We have lots of files now too many to search by hand, we know the password is of length 32 so

    find . * -exec grep -E '\b.{32}\b'  {} \;

    This command will search each file in each of the subdirectories for a 32 character word.

6. P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU

    There are no files in the home directory of bandit6 so we must try something else to locate the password file.

    We know the password is 32 characters and it is owned by both this user and the next bandit7.

    The command below will search allz files for a file matching these characteristics

    find / -user bandit7 -group bandit6 -exec grep -E '\b.{32}\b'  {} 2>/dev/null \;


7. z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S

    Opening the file in the home directory i can see its a large file containing 32 character strings

    The first thing that comes to mind is to brute force the list but that seems heavy handed and out of scope, im going to check the specification for this one.

    Ok, the specification says i need to find the flag next to the key 'millionth'.

    grep "millionth" ./data.txt

8. TESKZC0XvTetK0S9xNwm25STk5iWrBvP

    Again a list of 32 character strings is provided, this time without a key, 
    
    Another property of the flags is they tend to be unique strings.

    With that in mind ill try sorting and filtering out the duplicated lines.
    
    sort ./data.txt | uniq -u

    bingo

9. EN632PlfYiZbn3PhVK3XOGSlNInNE00t

    cat ./data.txt

    file -i ./data.txt
    
    Shows we have a binary file

    If we add the a switch to grep we can search it as if it were text for a 32 character string

    grep -aE '\b.{32}\b' 

10. G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s

    cat ./data.txt

    base64 -d ./data.txt
    

11. 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM

    cat ./data.txt

    Displayed is a string of characters with a structure identical the previous flag file, but the letters look scrambled. 

    I ran the text though a ceaser cipher brute script written in python.

    Shift 13: The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv


12. JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv

    