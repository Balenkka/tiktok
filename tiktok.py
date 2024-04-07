import os
import requests
import random
import time
# Open the file in read mode
mrx=input('USER TIK TOK : ')
with open('user-agents.txt', 'r') as file:
    halo=range(10000)
    lines = file.readlines()

    for i in halo:
        url='https://tiktok.com/report/'
        if not lines:
            print("NOT FOUND USER AGENT")
        else:
            time.sleep(5)
            random_line = random.choice(lines)

            user=random_line.strip()
            rep=f'{url} + 21cf00d2-5ea1-4eb5-8a68-b4b266b3cce5'
            print(f'REPORT SEND FOR @{mrx} {user}')