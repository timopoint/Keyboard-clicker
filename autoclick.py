import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import keyboard
import mouse
import time
import json
import threading as thr




# Root init
root = tk.Tk()

root.title("Keyboard Clicker")

root.geometry("500x300")
root.resizable(False, False)
#

# Preloading, variables and defines

data = {
    "hotkey" : "f1",
    "text" : "",
    "delay" : 0.5,
    "text_on" : 0,
    "mouse_on" : 0,
    "double_on" : 0,
    "code_on" : 0,
    "code_path" : "",
}

try:
    with open("Options.json", "r", encoding="utf-8") as file:
        pass
except:
    with open("Options.json", "w", encoding="utf-8") as file:
        json.dump( data, file, indent=4, ensure_ascii=False, sort_keys=True)



with open("Options.json", "r", encoding="utf-8") as file:
    data = json.load(file)


work = False

lines = []

text_on = tk.IntVar(value= data["text_on"])
mouse_on = tk.IntVar(value= data["mouse_on"])
double_on = tk.IntVar(value= data["double_on"])
code_on = tk.IntVar(value= data["code_on"])


def typing_loop():
    while work:
        keyboard.write(data["text"])
        time.sleep(data["delay"])

def clicking_loop():
    global work
    selected = mouse_buttons[mouse_buttons_list.curselection()[0]]
    if data["double_on"].get() == 1:
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
        if code_on.get() == 1:
            thr.Thread().start()
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
    global data
    data["text_on"] = text_on.get()
    data["mouse_on"] = mouse_on.get()
    data["double_on"] = double_on.get()
    data["code_on"] = code_on.get()

    with open("Options.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False, sort_keys=True)
    root.destroy()


def select_file():
    # Открытие диалога выбора файла
    file_path = filedialog.askopenfilename(defaultextension="txt")
    if file_path:
        data["code_path"] = file_path
        code_path_label.config (text= "Path: " + data["code_path"] )


intetpretation = {
    "INFLOOP" : 0,
    "FOR" : 0,
    "ENDFOR" : 0,
    "KEY_PRESS" : 0,
    "KEY_DOWN" : 0,
    "KEY_UP" : 0,
    "MOUSE_DOUBLE_CLICK" :0,
    "MOUSE_CLICK" :0,
    "MOUSE_DOWN" : 0,
    "MOUSE_UP" : 0,
    "WAIT" : 0,
}

def INFLOOP(Lines: list[str]):
    pass

def FOR(count: int, Lines: list[str]):
    pass


def KEY_PRESS(key: str):
    pass

def KEY_DOWN(key: str):
    pass
def KEY_DOWN(key: str, time: float):
    pass

def KEY_UP(key: str):
    pass


def MOUSE_DOUBLE_CLICK(key: str):
    pass

def MOUSE_CLICK(key: str):
    pass

def MOUSE_DOWN(key: str):
    pass
def MOUSE_DOWN(key: str, time: float):
    pass

def MOUSE_UP(key: str):
    pass


def WAIT(seconds: float):
    time.sleep(seconds)


def interpretator():
    try:
        with open(data["code_path"], "read", encoding="utf-8") as file:
            global lines
            lines = file.readlines() 
    except:
        pass

keyboard.add_hotkey( data["hotkey"], clicker)
#



# Base Frame for Every option
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
mouse_on_checkbtn.place(x= 285, y= 12)

code_on_checkbtn = ttk.Checkbutton(base_frame, text= "Code-file mode", onvalue=1, offvalue= 0, variable=code_on)
code_on_checkbtn.place(x= 380, y= 12 )
##

##
code_path_change_btn = tk.Button(base_frame, text= "Change path", command= select_file)
code_path_change_btn.place(x= 12, y= 75, width= 90)

code_path_label = tk.Label(base_frame, text= "Path: " + data["code_path"] )
code_path_label.place(x= 110, y= 78,)
##

base_frame.place(x= 5, y= 5, width=490, height= 110 )
#



# Text Frame for writing text
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

text_frame.place(x= 5, y= 120, width= 490, height= 65)
#

#Text Frame for wirting text
mouse_frame = tk.Frame(borderwidth=1, relief="solid")

##
mouse_buttons = ["left", "right", "middle"]
mouse_buttons_var = tk.Variable(value=mouse_buttons)

mouse_buttons_list = tk.Listbox(mouse_frame, selectmode= ["single"], height= 3, listvariable=mouse_buttons_var)
mouse_buttons_list.place(x= 5, y= 10)

double_click_checkbtn = ttk.Checkbutton(mouse_frame, text= "double click", onvalue=1, offvalue= 0, variable=double_on)
double_click_checkbtn.place(x= 5, y= 65)

##

mouse_frame.place(x= 5, y= 190, width= 490, height= 100)
#


root.protocol("WM_DELETE_WINDOW", finish)

root.mainloop()