from __future__ import unicode_literals
import os
from guizero import App, Text, TextBox, PushButton
from tkinter import Tk
from tkinter.filedialog import askopenfilenames, askdirectory
import youtube_dl
#Tk().withdraw()


def download():
    #Text.text = "Button was pressed"
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['{}'.format(input_box.value)])


def save_dir():
    #Text.text = "Button was pressed"
    save = askdirectory()
    print(save)
    save_text = Text(app, text="Saving to..." + save )
    button_start = PushButton(app, text="Start Download", command=download)


app = App(width = 500, height = 200)

url_text = Text(app, text="Paste Video URL below")

input_box = TextBox(app, width = 600)

button_dest = PushButton(app, width = 50, text = "Chose Save Location", command=save_dir)

app.display()

#output = "C:\\Users\\Office\\Documents\\EGDownloads\\Media"






