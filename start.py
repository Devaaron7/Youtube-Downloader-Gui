from __future__ import unicode_literals
import os
from guizero import App, Text, TextBox, PushButton
from tkinter import Tk
from tkinter.filedialog import askopenfilenames, askdirectory
import youtube_dl
import subprocess as sp
import time
#Tk().withdraw()

save = ""

def save_dir():
    global save
    #Text.text = "Button was pressed"
    folder = askdirectory()
    save += folder
    save_text = Text(app, text="Saving to..." + save )
    button_start = PushButton(app, text="Start Download", command=download)


def download():
    #global save
    #print(save)
    #input()
    #Text.text = "Button was pressed"
    
    ydl_opts = {
    'outtmpl': '{}\%(title)s.%(ext)s'.format(save)
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['{}'.format(input_box.value)])
    print(ydl_opts)
    


app = App(width = 500, height = 200)

url_text = Text(app, text="Paste Video URL below")

input_box = TextBox(app, width = 600)

button_dest = PushButton(app, width = 50, text = "Chose Save Location", command=save_dir)

app.display()

#output = "C:\\Users\\Office\\Documents\\EGDownloads\\Media"

'''
url = input()
out = sp.getoutput('youtube-dl --get-filename https://www.youtube.com/watch?v=BzUV9BciHe8')
to = "C:\\Users\\ATUser\\Desktop\\mp3"
fr = "{}".format(out)
print(fr)
os.system('cmd /c "youtube-dl {}'.format(url))
time.sleep(2)
os.system('cmd /c "move {} {}'.format(fr, to))
'''




#print(out)


