import time
import random
from tkinter import Tk


def start():

    for i in range(10):
        print(i+1)
        time.sleep(0.2)


def update(window: Tk):
    window.title(f"{random.uniform(1, 10)}")
    # window.config(background=f"#f{int(random.uniform(100, 700))}78")
    window.after(3000, update)
