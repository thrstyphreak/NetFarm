# Written by ThrstyPhreak
import Module1
import time
from colorama import Fore, init, Back, Style
import os


print("Starting NetFarm Framework")
time.sleep(3)

def help():
     print("#############################################################################################################################")
     print("#                                                HELP                                                                       #")
     print("#    set       sets a module     search Searches for a module        Help     Opens help options                            #")




def main():
    
    os.system('clear')
    inut = input("Enter option: ")

    if inut == ("Help"):
        help()
        time.sleep(10)
        main()

    if inut == ("help"):
        help()
        time.sleep(10)
        main()











main()
