import pyautogui as p # main
import time # for waiting
listofwors = ['Follow AV7coder','A cool coder AV7coder is here', 'A young developer AV7coder', 'Follow AV7coder' ]
for i in range(0, 5):
    meassage = listofwors[i]
    time.sleep(10)
    p.press('Space') # press space
    p.write(meassage) # type
    p.press('Enter') # to send message

