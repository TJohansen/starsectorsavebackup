import os
import platform

print('1. Copy files to Google Drive \n2. Copy files to Starsector save directory')
while True:
    a = input('> ')
    if platform.system() == 'Darwin':
        if a == '1':
            os.system('cp -r /Applications/Starsector.app/saves/ /Users/thomas/Google\ Drive/Starsector\ Save')
            print("The saves have been synced to Google Drive")
            break
        elif a == '2':
            os.system('cp -r /Users/thomas/Google\ Drive/Starsector /Applications/Starsector.app/saves/')
            print("The saves have been downloaded from Google Drive")
            break
        else:
            print("You've made an invalid choice, please try again.")
    elif platform.system() == 'Windows':
        if a == '1':
            os.system('robocopy "C:\Program Files (x86)\Fractal Softworks\Starsector\saves" "D:\Google Drive\Starsector Save" /E')
            print("The saves have been synced to Google Drive")
        elif a == '2':
            os.system('robocopy "D:\Google Drive\Starsector Save" "C:\Program Files (x86)\Fractal Softworks\Starsector\saves" /E')
            print("The saves have been downloaded from Google Drive")
        else:
            print("You've made an invalid choice, please try again.")