import time
import pyautogui
import webbrowser

webbrowser.open('https://www.facebook.com/nesarali.titumir')#put your friend's profile URL here

no_of_posts = 10
liked = 0
while(True):
    time.sleep(0.5)

    found = pyautogui.locateOnScreen('likebtn.png' , confidence=.5) #to use confidence,install opencv-python
    if found is not None:
        pnt = pyautogui.center(found)
        x,y = pnt
        pyautogui.click(x,y)
        liked = liked + 1
        print("post no " + str(liked) + " liked")
        time.sleep(1)

    if(liked>=no_of_posts):
        break

    pyautogui.vscroll(-10)
    time.sleep(0.5)

