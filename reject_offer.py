import pyautogui
import time
from python_imagesearch.imagesearch import *
import pathlib


file_prefix = pathlib.Path(__file__).parent.resolve()

# Define function to find mouse position
def mouse_pos():
    # set counter
    counter = 0  
    # counter ticks for 2 minutes and then stops - courtesy of time.sleep in while loop 
    while counter <= 120:

        print(pyautogui.position())
        time.sleep(1)
        counter + 1


# Define mouse click function
def click(x, y):
    pyautogui.click(x, y)


# Declare images to search for
se_tilbud = RF"{file_prefix}\1.png"
afvis_tilbud = RF"{file_prefix}\2.png"
bekræft_nej = RF"{file_prefix}\3.png"


# Define function to show offer
def show_offer():
    pos = imagesearcharea(se_tilbud, 1388, 606, 1529, 684)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        time.sleep(0.5)
        click(1444, 653)
        time.sleep(1.5)
    else:
        raise FileNotFoundError(F"image {se_tilbud} not found on screen")

# Define function to decline offer
def decline_offer():
    pos = imagesearcharea(afvis_tilbud, 1405, 950, 1511, 1044)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        click(1461, 1008)
        time.sleep(0.9)
        pyautogui.press('pagedown')
        time.sleep(1.5)
    else:
        raise FileNotFoundError(F"image {afvis_tilbud} not found on screen")

# Define function to confirm
def confirm_no():
    pos = imagesearcharea(bekræft_nej, 1338, 375, 1433, 488)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        time.sleep(0.3)
        click(1390, 420)
        time.sleep(5.3)
        pyautogui.press('home')
    else:
        raise FileNotFoundError(F"image {bekræft_nej} not found on screen")


# Main function
def main():
    
    # Dialog to await confirmation before execution of main function- uncomment if needed
#     pyautogui.alert("Ready?")

#    mouse_pos()



    # amount of offers to decline (can be found under: https://www.dabbolig.dk/min-side/min-boligsoegning/)
    offer_count = 1

    # THE loop
    while offer_count > 0:
        show_offer()
        decline_offer()
        confirm_no()
        offer_count =- 1
    print("DONE!!!")


if __name__ == "__main__":
    main()