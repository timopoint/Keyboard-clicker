import keyboard
import mouse
import time
import os

f = open("Hotkey.txt", 'a+', encoding='utf-8')
f.seek(0)
hotkey = f.read()

if hotkey == "":
    hotkey = 'f1'
    f.seek(0)
    f.write(hotkey)

f.close()




f = open("AbortHotkey.txt", 'a+', encoding='utf-8')
f.seek(0)
aborthotkey = f.read()

if aborthotkey == "":
    aborthotkey = 'f2'
    f.seek(0)
    f.write(aborthotkey)
    
f.close()




work = False
def change():
    global work
    work = not work
    time.sleep(0.5)
    print(f" '{hotkey}' - pressed ")


def out():
    os.abort()

keyboard.add_hotkey(hotkey, change)

keyboard.add_hotkey(aborthotkey, out )

f = open('./Keyboard.txt', 'a+', encoding='utf-8')
f.seek(0)
content = f.read()
f.close()
print (f" text: {content}")


print("script is working")
print(f"to turn it on/off press '{hotkey}' ")
print(f"to abort clicker press '{aborthotkey}' ")

while True:
    if work: 
        keyboard.write(f"{content}")
        time.sleep(0.2) 
    else:
        time.sleep(0.05) 
