import random

from pyfiglet import  Figlet

from termcolor import colored

fonts = ["slant","banners3-D","big","block""buble"
    ,"digital","doom","isometrical",
         "mini","small","starwars"]

colours = ["red","green","yellow","blue",
           "magnta","cyan"]

F = Figlet(font=random.choice(fonts))

print(colored(F.renderText("Happy New Year 2026"),
                            random.choice(colours)))