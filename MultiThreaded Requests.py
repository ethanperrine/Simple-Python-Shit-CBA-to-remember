import easygui
import requests
import time
import threading
from alive_progress import alive_bar

# os.system("pip install grequests")

global output
output = []
global hashes
hashes = open(easygui.fileopenbox("Import you Data here:")).readlines()
email = "@gmail.com"
code = ""

hash_type = "md5"

count = 0
threads = input("Please put number of threads: ")
# print(count)
def dehasher():
        for line in hashes:
            hashes.remove(line) # DO THIS SO IT DOES NOT DO IT MULTIPLE TIMES
            if ":" in line:
                line = line.split(":")
                foohash = line[1].strip()
                r = requests.get(
                    f"https://md5decrypt.net/en/Api/api.php?hash={foohash}&hash_type={hash_type}&email={email}&code={code}").text
                poppop = str(line[0] + ":" + r)
                if len(poppop) != 0 and len(r) != 0:
                    print(poppop.strip())
                    output.append(poppop)
            else:
                barhash = line.strip()
                req = requests.get(
                    f"https://md5decrypt.net/en/Api/api.php?hash={barhash}&hash_type={hash_type}&email={email}&code={code}").text
                if len(req) != 0:
                    print(req.strip())
                    output.append(req)

threadsList = []

start = time.time()

for i in range(1, int(threads)):
    x = threading.Thread(target=dehasher)
    threadsList.append(x)
    x.start()


    #threading.Thread(target=dehasher(), args=()).start()

for x in threadsList:
    x.join()

# print(f"list: {output}")
with open("dehashed.txt", "w") as f:
    for line in output:
        if len(line) != 0:
            f.write(f"{line.strip()}\n")
                

end = time.time()

print("\nIt took:", (end - start), "seconds")
