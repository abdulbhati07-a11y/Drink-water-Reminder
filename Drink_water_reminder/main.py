from plyer import notification
import time

while True:
    print("Please drink some water!")
    notification.notify("title = Drink Water ", 
                         "message = You need to drink some water.",)
    
    time.sleep(10)