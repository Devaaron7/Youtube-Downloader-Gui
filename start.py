import os
from guizero import App, Text, TextBox, PushButton

def do_nothing():
    #Text.text = "Button was pressed"
    text.destroy()


app = App(width = 500, height = 200)
text = Text(app, text="Paste Video URL below")
input_box = TextBox(app, width = 600)
button_dest = PushButton(app, text = "Select Save Directory", command=do_nothing)
button_start = PushButton(app, command=do_nothing)
app.display()

'''
while True:
    
    url = input("Paste URL\n")

    #output = "C:\\Users\\Office\\Documents\\EGDownloads\\Media"

    os.system("youtube-dl {}".format(url))
    #os.system("cmd /k echo hello world")
'''
