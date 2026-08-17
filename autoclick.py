import tkinter as tk
import keyboard
import time
import json
import threading as thr


try:
    with open("Options.json", "r", encoding="utf-8") as file:
        pass
except:
    with open("Options.json", "w", encoding="utf-8") as file:
        json.dump( {"hotkey" : "f1", "text" : "", "delay" : 0.5}, file, indent=4, ensure_ascii=False, sort_keys=True)

data = {
    "hotkey" : "",
    "text" : "",
    "delay" : 0.5
}

with open("Options.json", "r", encoding="utf-8") as file:
    data = json.load(file)


work = False

def typing_loop():
    while work:
        keyboard.write(data["text"])
        time.sleep(data["delay"])

def clicker():
    global work
    if not work:
        work = True
        thr.Thread(target=typing_loop, daemon=True).start()
    else:
        work = False

def change_hotkey():
    keyboard.remove_hotkey(clicker)
    global data
    event = keyboard.read_event()
    data["hotkey"] = event.name       
    hotkey_label.config(text = "hotkey: " + data["hotkey"])
    man = keyboard.add_hotkey(data["hotkey"], clicker)

def set_text():
    global data
    data["text"] = text_entry.get()
    text_label.config(text= "saved text: " + data["text"])

def set_delay():
    global data
    data["delay"] = float(time_entry.get())
    time_label.config(text= "seconds: " + str(data["delay"]))

def finish():
    with open("Options.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False, sort_keys=True)
    root.destroy()

keyboard.add_hotkey( data["hotkey"], clicker)




#
root = tk.Tk()

root.title("Keyboard Clicker")

root.geometry("500x130")
root.resizable(False, False)
#



#
hotkey_label = tk.Label(root, text = "hotkey: " + data["hotkey"])
hotkey_label.place(x= 110, y= 12 )

change_hotkey_btn = tk.Button(root, text= "change hotkey", command= change_hotkey )
change_hotkey_btn.place(x= 12, y = 10, width= 90)
#



#
set_text_btn = tk.Button(root, text= "set text", command= set_text )
set_text_btn.place(x= 12, y = 40, width= 90)

text_entry = tk.Entry(root)
text_entry.config(width=51)
text_entry.place(x = 175, y= 44)

text_hint_label = tk.Label(root, text = "Enter text: ")
text_hint_label.place(x = 110, y= 42)

text_label = tk.Label(root, text = "saved text: " + data["text"])
text_label.place(x= 110, y= 65 )
#



#
time_entry =tk.Entry(root)
time_entry.place(x = 210, y= 90)

time_hint_label = tk.Label(root, text= "Delay in seconds:")
time_hint_label.place(x = 110, y= 90)

time_label = tk.Label(root, text= "seconds: " + str(data["delay"]))
time_label.place(x = 340, y= 90)

set_time_btn = tk.Button(root, text= "set delay", command= set_delay)
set_time_btn.place(x= 12, y = 88, width= 90)
#


root.protocol("WM_DELETE_WINDOW", finish)

root.mainloop()