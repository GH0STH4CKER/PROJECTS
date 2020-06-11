import sys, time, colorama, datetime
from colorama import Fore, Back, Style, init
init()

def slowprint(str):
   for c in str :
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0.2)

print(Fore.LIGHTGREEN_EX +"")
slowprint("Hello Dimuth !\n")
time.sleep(1)

DT = str(datetime.datetime.now())
DThour = int(DT[11:13])
DTminute = int(DT[14:16])
DTtime = (DThour * 100) + DTminute
#print(DT,DThour,DTminute,DTtime)
if DTtime > 500 and DTtime < 1200:
  slowprint("\nGood Morning...\n")
elif DTtime >= 1200 and DTtime < 1500:
  slowprint("\nGood Afternoon...\n")
elif DTtime >= 1500 and DTtime < 1900:
  slowprint("\nGood Evening...\n") 
elif DTtime >= 1900 and DTtime <= 2359:
  slowprint("\nGood Night...\n") 
else:
  slowprint("\nHave a good day ...!\n")  
   
Dtime = str(DT[11:16])  
slowprint("\nThe time is ")
slowprint(Dtime)
print("\n")
DTdate = str(DT[:10])

slowprint("The date is ")
slowprint(DTdate)

WKday = datetime.datetime.now().weekday()
if WKday == 0:
  weekDAY = "Monday"
elif WKday == 1:
  weekDAY = "Tuesday"  
elif WKday == 2:
  weekDAY = "Wednesday"    
elif WKday == 3:
  weekDAY = "Thursday"  
elif WKday == 4:
  weekDAY = "Friday"  
elif WKday == 5:
  weekDAY = "Saturday"  
elif WKday == 6:
  weekDAY = "Sunday"  
else:
  print("Error occured")  

slowprint("\n\nToday is ")
slowprint(weekDAY)  

print("\n")
input("Exit >")
