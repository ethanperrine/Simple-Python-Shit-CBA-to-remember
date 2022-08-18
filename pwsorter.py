from easygui import fileopenbox

with open("password_hash.txt", "w") as output_file:
    with open(fileopenbox("Import your Data here:"), "r") as input_file:
        for line in input_file.readlines():
            if ":" in line:  # If the line contains a colon, it is a hash
                line = line.split(":")  # delimits the line with a colon
                password_hash = line[1].strip()  # strips the password hash from the line
            else:
                password_hash = line.strip()  # if there is no email present, it will just grab the hash
            output_file.write(password_hash + "\n")  # writes the hash to the output file
