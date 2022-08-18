import easygui
from functools import partial

utf8open = partial(open, encoding="UTF-8")
filename = './antipub.txt'

create_file = open(filename, "a")

def blocks(files, size=65536):
    while True:
        b = files.read(size)
        if not b: break
        yield b


with utf8open(filename, "r", errors='ignore') as start_file:
    start = (sum(bl.count("\n") for bl in blocks(start_file)))

    with utf8open(easygui.fileopenbox("import your file", "r")) as input_file:
        data = input_file.read()
        try:
            if data not in utf8open(filename).read():
                with utf8open(filename, "a") as outfile:
                    outfile.write(data)
        except IOError:  # if the file doesn't exist create a new one
            with utf8open(filename, "a") as outfile:
                outfile.write(data)  # if you want to add a new line

with utf8open(filename, "r", errors='ignore') as end_file:
    end = (sum(bl.count("\n") for bl in blocks(end_file)))

print("Added", end - start, "lines")
