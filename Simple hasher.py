import hashlib
from  passlib.hash import mysql41
from os import system, name

try:
    from easygui import fileopenbox
except ImportError:
    system('pip install easygui')

with open(fileopenbox(msg="input list")) as input_file:
    with open("output.txt", "w") as output_file:
        for line in input_file:
            if ":" in line:
                line = line.split(":")
                password = line[1].strip()
                username = line[0].strip()
                
                # Beginning of the hash types mentioned 2 comments after
                md5 = hashlib.md5(password.encode()).hexdigest()
                sha1 = hashlib.sha1(password.encode()).hexdigest()
                sha256 = hashlib.sha256(password.encode()).hexdigest()
                sha512 = hashlib.sha512(password.encode()).hexdigest()
                mysql = mysql41.hash(password)
                double_md5 = hashlib.md5(md5.encode()).hexdigest()
                # End of the hash types mentioned the comment after this

                # for the line below just change "mysql" to another hash type seen above
                output_file.writelines(username + ":" + mysql + "\n")
