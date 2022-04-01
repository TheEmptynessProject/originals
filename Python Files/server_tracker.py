import datetime
import socket
import time
import keyboard
import matplotlib.pyplot as plt

print("Examples: google.com; amazon.com; mozilla.org")

CheckSuccessTime = ""

def check(site):
    global CheckSuccessTime
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((site, 80))
        CheckSuccessTime = datetime.datetime.now().time()
        return True
    except:
        CheckSuccessTime = datetime.datetime.now().time()
        return False

def countTime(secs):
    for x in range(secs, 0, -1):
        if keyboard.is_pressed('q'):
            print('You Pressed A Key!')
            break
        print(x, end=" ", flush=True)
        time.sleep(1)
    return print('')

stop = False

def onkeypress(event):
    global stop
    if event.name == 'q':
        stop = True

keyboard.on_press(onkeypress)

toCheck = str(input('What website to track:\n'))
x = []
y = []

if(toCheck.find(".") != -1):
    while True:
        if stop:
            break
        checked = check(toCheck)
        if keyboard.is_pressed('q'):
            print('You Pressed A Key!')
            break
        if(checked):
            x.append(str(CheckSuccessTime))
            y.append(1)
            print('Success ', CheckSuccessTime)
        else:
            x.append(str(CheckSuccessTime))
            y.append(0)
            print("Failure ", CheckSuccessTime)
        countTime(10)
        
plt.figure(figsize=(20, 3))
plt.bar(x, y)
plt.show()
