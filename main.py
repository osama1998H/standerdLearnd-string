import time
import random


def start():

    for i in range(10):
        print(i+1)
        time.sleep(0.2)


def update(window):
    window.config(background=f"#f{int(random.uniform(100, 700))}78")
    window.after(3000, update)
