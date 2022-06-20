import os
import random
import time
print("""Simple amazon code generator DOES NOT CHECK

I take no responsibility for any illegal actions that you do with this program. You are responsible for actions. This is for proof of concept.

Made by BasedGamer#0001""")
time.sleep(1)
def start():
    def gen():

        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nums = "0123456789"

        length1 = 4
        length2 = 6
        length3 = 5

        string1 = upper + nums
        string2 = upper + nums
        string3 = upper + nums

        pt1 = "".join(random.sample(string1, length1))
        pt2 = "".join(random.sample(string2, length2))
        pt3 = "".join(random.sample(string3, length3))

        with open("working.txt", "a") as o:
            o.write(f"{pt1}-{pt2}-{pt3}\n")

    def next():
        amount = input("How many: ")
        for n in range(int(amount)):
            gen()
        print(f"Completed, codes saved to working.txt in {os.getcwd()}")

    if "working.txt" not in os.listdir():
        with open("working.txt", "w"):
            next()
    elif "working.txt" in os.listdir():
        next()
    else:
        print("Error")
if __name__ == "__main__":
    start()