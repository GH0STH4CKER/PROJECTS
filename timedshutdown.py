import os

print(" _____ _           _      _                   _____ _         ")            
print("/  ___| |         | |    | |                 |_   _(_)         ")           
print("\ `--.| |__  _   _| |_ __| | _____      ___ __ | |  _ _ __ ___   ___ _ __ ")
print(" `--. \ '_ \| | | | __/ _` |/ _ \ \ /\ / / '_ \| | | | '_ ` _ \ / _ \ '__|")
print("/\__/ / | | | |_| | || (_| | (_) \ V  V /| | | | | | | | | | | |  __/ |   ")
print("\____/|_| |_|\__,_|\__\__,_|\___/ \_/\_/ |_| |_\_/ |_|_| |_| |_|\___|_|   ")
print("       [+] made by @GH0$TH4CK3R")
print("")
shutdown = input("Do you want to shutdown your pc ? (Yes/No)\n")

if shutdown == "No" or shutdown == "NO" or shutdown == "no":
    exit()
elif shutdown == "Yes" or shutdown == "YES" or shutdown == "yes":
    count = input("Now or few minutes later ? t(input in seconds)\n") 
    os.system("shutdown /s /t " + count)
    abort = input("To abort scheduled shutdown , (yes/no) : \n")
    if abort == "yes":
        os.system("shutdown /a")
    else:
        exit()
else:
    print("Incorrect input, TRY AGAIN")
    
