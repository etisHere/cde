import json
import requests
#MADE BY ET

print("Whats your coordinates?")
userlat = input("(lat): ")
userlon = input("(lon):")
#taking coordonates input for API
parameters = {
    "lat": userlat,
    "lon": userlon
}

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#This is the api to show whos in space and etc
def spacep():
    response = requests.get("http://api.open-notify.org/astros.json") 
    jprint(response.json())

def pasda():
    respones = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
    jprint(respones.json())

def picda():
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY") 
    jprint(response.json())



def mainmenu():
    print("""



    /\\
   /  \\
  |    |
  |NASA|
  |    |
  |    |
  |    |
 '      `
 |      |
 |      |
 |______|
  '-`'-`   .
  / . \'\ . .'
 ''( .'\.' ' .;'
'.;.;' ;'.;' ..;;'        

international space station = stat

"Who's in space?" = who

Pic of the day =  pic 

""")
    choice = input("Where to?: ")
    if choice == "stat":
        pasda()
    if choice == "who":
        spacep()
    if choice == "pic":
        picda()




mainmenu()
