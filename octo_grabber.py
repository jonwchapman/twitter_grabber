import os
import sys
import subprocess

print("Octo-grabber")


y = 0

for x in range(0, 9000, 450):
    lower = x
    upper = x + 449
    print(lower)
    print(upper)
    stmt = "konsole -e python3 /home/turbo/PycharmProjects/twitter_grabber/follower_grabber.py " + str(lower) + " " + str(upper)
    #stmt = "konsole -e python3 /home/turbo/PycharmProjects/twitter_grabber/test_octo.py"
    #subprocess.run(['konsole', '--', 'python3', stmt])
    child = subprocess.Popen(stmt, shell=True)


