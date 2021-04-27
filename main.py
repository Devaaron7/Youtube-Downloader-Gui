from __future__ import unicode_literals
import os
from guizero import App, Text, TextBox, PushButton, Picture
from tkinter import Tk
from tkinter.filedialog import askopenfilenames, askdirectory
import youtube_dl
import subprocess as sp
import time


save = ""
button_start = 0

def reset():
    global button_start
    button_start.destroy()
    button_start = PushButton(app, text="Start Download", command=download)


def save_dir():
    global save, button_start
    folder = askdirectory()
    save += folder
    save_text = Text(app, text="Saving to..." + save )
    button_start = PushButton(app, text="Start Download", command=download)
    button_dest.destroy()


def download():
    global button_start
    ydl_opts = {
    'outtmpl': '{}\%(title)s.%(ext)s'.format(save)
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['{}'.format(input_box.value)])
    picture.visible = True
    button_start.destroy()
    button_start = PushButton(app, text="Download Complete!")
    button_start.after(3000, reset)
    
    


app = App(width = 500, height = 250)
url_text = Text(app, text="Paste Video URL below")
input_box = TextBox(app, width = 600)
picture = Picture(app, visible=False,  width = 100, height = 100, image="done.gif")
button_dest = PushButton(app, width = 50, text = "Chose Save Location", command=save_dir)
app.display()



#CODE FOR COMMAND PROMPT USE SOLUTION. GAVE PERMISSION ISSUES WHEN CHOOSING DIRECTORY
##---------------------------------------------------------------------------------------------
'''
url = input()
out = sp.getoutput('youtube-dl --get-filename https://www.youtube.com/watch?v=BzUV9BciHe8')
to = 
fr = "{}".format(out)
print(fr)
os.system('cmd /c "youtube-dl {}'.format(url))
time.sleep(2)
os.system('cmd /c "move {} {}'.format(fr, to))
'''
##---------------------------------------------------------------------------------------------
