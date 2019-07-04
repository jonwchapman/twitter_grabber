import os
import sys
import subprocess

print("Octo-grabber")


y = 0

for x in range(0, 8800, 450):
    lower = x
    upper = x + 449
    print(lower)
    print(upper)
    stmt = "python3 /home/turbo/PycharmProjects/twitter/follower_grabber.py " + str(lower) + " " + str(upper)
    os.system(stmt)



