import requests
import time
import threading

# os.system("pip install grequests")

count = 0
threads = input("Please put number of threads: ")


# print(count)
def main():
    r = requests.get(f"link of URL").text
    print(r.strip())


threadsList = []

start = time.time()

for i in range(1, int(threads)):
    x = threading.Thread(target=main)
    threadsList.append(x)
    x.start()

for x in threadsList:
    x.join()

# print(f"list: {output}")
with open("dehashed.txt", "w") as f:
    for line in f:
        if len(line) != 0:
            f.write(line)
            # f.write(f"{line.strip()}\n")

end = time.time()

print("\nIt took:", (end - start), "seconds")
