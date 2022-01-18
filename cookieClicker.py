import pyautogui, time, webbrowser, random

webbrowser.open('https://orteil.dashnet.org/cookieclicker/') #Open website

time.sleep(3) #Give webpage time to load

#TO BREAK LOOP YOU MUST PUT CURSOR IN CORNER FOR FAILSAFE TO ACTIVATE
#main loop
while True:
    for i in range(random.randrange(1, 3)):
        #Clicks on the cookie for a random amount of times and for random intervals to prevent bot detection
        pyautogui.click(x=220,y=400,duration=random.uniform(0,.1),interval=random.uniform(.1,.25))

    for i in range(1519, 878, -107):
        #Clicks the upgrades twice while I work on color detection with cv2
        pyautogui.click(x=2427,y=i)

#Parameters of interest on my computer
#(1350,420) Top upgrade
#(1350,790) Bottom upgrade
#[36, 90, 119] Ready to buy upgrade
#[22, 22, 22] Not ready to buy upgrade
#pyautogui.click(x=220,y=400) Cookie placement