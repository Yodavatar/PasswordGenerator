#Coding : utf-8
#Coding by Yodavatar
#Licensed code MIT License
#App : PasswordGenerator

import random
import time

def create_seed():
    """
    Create a seed for the password generator with the current time.
    """
    random.seed(int(time.time() * 1000))# time in milliseconds
    return random.randint(0, 1000000)

#Coding : utf-8
#Coding by Yodavatar
#Licensed code MIT License
#App : PasswordGenerator