import pyautogui
import time
from python_imagesearch.imagesearch import *

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
se_tilbud = R"C:\Users\Julius\Documents\CODING\Python\rejection\1.png"
afvis_tilbud = R"C:\Users\Julius\Documents\CODING\Python\rejection\2.png"
bekræft = R"C:\Users\Julius\Documents\CODING\Python\rejection\3.png"


# Define function to show offer
def show_offer():
    pos = imagesearcharea(se_tilbud, 1388, 606, 1529, 684)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        time.sleep(1)
        click(1444, 653)
        time.sleep(2)
    else:
        print("image 1 not found")
        raise(RuntimeError)

# Define function to decline offer
def decline_offer():
    pos = imagesearcharea(afvis_tilbud, 1412, 987, 1511, 1044)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        click(1461, 1010)
        time.sleep(1)
        pyautogui.press('pagedown')
        time.sleep(3)
    else:
        print("image 2 not found")
        raise(RuntimeError)
    
# Define function to confirm
def confirm_no():
    pos = imagesearcharea(bekræft, 1338, 395, 1433, 458)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        time.sleep(1)
        click(1390, 422)
        time.sleep(8)
        pyautogui.press('home')
    else:
        print("image 3 not found")
        raise(RuntimeError)


# Main function
def main():
    # Are you READY?
    pyautogui.alert("Ready?")
#    mouse_pos()

    # amount of offers to decline (can be found under: https://www.dabbolig.dk/min-side/min-boligsoegning/)
    offer_count = 24
    # THE loop
    while offer_count > 0:
        show_offer()
        decline_offer()
        confirm_no()
        offer_count - 1
        if offer_count == 0:
            print("DONE!")
            break


if __name__ == "__main__":
    main()