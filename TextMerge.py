#combine f1.txt and f2.txt
import os
from functools import partial
import ctypes
try:
    from alive_progress import alive_bar
except ImportError:
    os.system("pip install alive-progress")
    os._exit()

utf8open = partial(open, encoding="UTF-8", errors="ignore")

def buf_count_newlines_gen(fname):
    print("Counting lines in", f"\"{fname}\"")
    def _make_gen(reader):
        while True:
            b = reader(2 ** 16)
            if not b: break
            yield b

    with open(fname, "rb") as f:
        count = sum(buf.count(b"\n") for buf in _make_gen(f.raw.read))
    return count

def main():
    total_count = 0
    finished_count = 0
    dir_path = ".\\"
    for path in os.scandir(dir_path):
            if path.is_file():
                if path.name.endswith(".txt") and not path.name.startswith("combine"):
                    total_count += 1
    print('Total File count:', total_count)
    for filename in os.listdir("."):
        if filename.endswith(".txt") and not filename.startswith("combine"):
            with utf8open(filename, "r") as f, utf8open("combine.txt", "w") as combine:
                ctypes.windll.kernel32.SetConsoleTitleW(f"Finished {finished_count} / {total_count} files")
                counted_lines = buf_count_newlines_gen(filename)
                with alive_bar(counted_lines, title=f"{filename}", refresh_secs=1) as bar:
                    for line in f:
                        combine.write(line)
                        bar()
                finished_count += 1
if __name__ == "__main__":
    main()
    input()
