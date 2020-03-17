import socket

print(" _          __ _           _       ")    
print("(_)        / _(_)         | |          ")
print(" _ _ __   | |_ _ _ __   __| | ___ _ __ ")
print("| | '_ \  |  _| | '_ \ / _` |/ _ \ '__|")
print("| | |_) | | | | | | | | (_| |  __/ |   ")
print("|_| .__/  |_| |_|_| |_|\__,_|\___|_|   ")
print("  | |                                  ")
print("  |_|     by - GH0$T_H4CKER       ")
print("")      
adrs = input("Enter the website address : ")
print("")
print("IP of the entered host is ",socket.gethostbyname(adrs))

input("press any key to exit")
