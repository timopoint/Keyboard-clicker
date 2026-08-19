import tkinter as tk
from tkinter import ttk
import keyboard
import mouse
import time
import json
import threading as thr




#
root = tk.Tk()

root.title("Keyboard Clicker")

root.geometry("500x300")
root.resizable(False, False)
#




#
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

text_on = tk.IntVar(value= 0)

mouse_on = tk.IntVar(value= 0)

double_on = tk.IntVar(value= 0)

def typing_loop():
    while work:
        keyboard.write(data["text"])
        time.sleep(data["delay"])

def clicking_loop():
    global work
    selected = mouse_buttons[mouse_buttons_list.curselection()[0]]
    if double_on.get() == 1:
        while work:
            mouse.double_click(button= selected)
            time.sleep(data["delay"])
    else:
        while work:
            mouse.click(button= selected)
            time.sleep(data["delay"])
            

def clicker():
    global work
    if not work:
        work = True
        if text_on.get() == 1:
            thr.Thread(target=typing_loop, daemon=True).start()
        if mouse_on.get() == 1:
            thr.Thread(target=clicking_loop, daemon=True).start()
    else:
        work = False

def change_hotkey():
    keyboard.remove_hotkey(clicker)
    global data
    event = keyboard.read_event()
    data["hotkey"] = event.name       
    hotkey_label.config(text = "hotkey: " + data["hotkey"])
    keyboard.add_hotkey(data["hotkey"], clicker)

def set_text():
    global data
    data["text"] = text_entry.get()
    text_label.config(text= "Saved text: " + data["text"])

def set_delay():
    global data
    data["delay"] = float(delay_entry.get())
    delay_label.config(text= "Delay: " + str(data["delay"]))

def finish():
    with open("Options.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False, sort_keys=True)
    root.destroy()

keyboard.add_hotkey( data["hotkey"], clicker)
#



#
base_frame = tk.Frame(borderwidth=1, relief="solid")

##
hotkey_label = tk.Label(base_frame, text = "hotkey: " + data["hotkey"])
hotkey_label.place(x= 110, y= 12 )

change_hotkey_btn = tk.Button(base_frame, text= "change hotkey", command= change_hotkey )
change_hotkey_btn.place(x= 12, y = 10, width= 90)
##

##
delay_entry =tk.Entry(base_frame)
delay_entry.place(x = 210, y= 47)

delay_hint_label = tk.Label(base_frame, text= "Delay in seconds:")
delay_hint_label.place(x = 110, y= 45)

delay_label = tk.Label(base_frame, text= "Delay: " + str(data["delay"]))
delay_label.place(x = 340, y= 45)

set_delay_btn = tk.Button(base_frame, text= "set delay", command= set_delay)
set_delay_btn.place(x= 12, y = 42, width= 90)
##

##
text_on_checkbtn = ttk.Checkbutton(base_frame, text= "Keyboard mode", onvalue=1, offvalue= 0, variable=text_on)
text_on_checkbtn.place(x= 175, y= 12 )

mouse_on_checkbtn = ttk.Checkbutton(base_frame, text= "Mouse mode", onvalue=1, offvalue= 0, variable=mouse_on)
mouse_on_checkbtn.place(x= 290, y= 12)
##

base_frame.place(x= 5, y= 5, width=490, height= 80 )
#



#
text_frame = tk.Frame(borderwidth=1, relief="solid")

##
set_text_btn = tk.Button(text_frame, text= "set text", command= set_text )
set_text_btn.place(x= 12, y = 10, width= 90)

text_entry = tk.Entry(text_frame)
text_entry.config(width=51)
text_entry.place(x = 175, y= 14)

text_hint_label = tk.Label(text_frame, text = "Enter text: ")
text_hint_label.place(x = 110, y= 12)

text_label = tk.Label(text_frame, text = "Saved text: " + data["text"])
text_label.place(x= 110, y= 35 )
##

text_frame.place(x= 5, y= 90, width= 490, height= 65)
#

#
mouse_frame = tk.Frame(borderwidth=1, relief="solid")

##
mouse_buttons = ["left", "right", "middle"]
mouse_buttons_var = tk.Variable(value=mouse_buttons)

mouse_buttons_list = tk.Listbox(mouse_frame, selectmode= ["single"], height= 3, listvariable=mouse_buttons_var)
mouse_buttons_list.place(x= 5, y= 10)

double_click_checkbtn = ttk.Checkbutton(mouse_frame, text= "double click", onvalue=1, offvalue= 0, variable=double_on)
double_click_checkbtn.place(x= 5, y= 65)

##

mouse_frame.place(x= 5, y= 160, width= 490, height= 100)
#


root.protocol("WM_DELETE_WINDOW", finish)

root.mainloop()