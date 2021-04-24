import os

while True:
    
    url = input("Paste URL\n")

    #output = "C:\\Users\\Office\\Documents\\EGDownloads\\Media"

    os.system("youtube-dl {}".format(url))
    #os.system("cmd /k echo hello world")
