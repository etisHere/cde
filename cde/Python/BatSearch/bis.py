import requests
import webbrowser
import os
import sys
import ast

#MADE BY ET
#Check line 16 for what i meant under readme 
def clear(): os.system('clear')
def rEddit():
    url0 = input("What are we searching for?: ")#Main user search
    clear()#Uses the os.system("clear").
    url9 = "https://www.reddit.com/search?q="#the sites search url
    for i in range(0, len(url0), 1):#Changing each space with %20
        if (url0[i] == " "):#This checks if there is a space
          url0 = url0.replace(url0[i], "%20")##This can be + such as on youtube.
          mainUr = url9+url0#making a full url//##I will mark the change under it
          xss = requests.get(mainUr)#Requesting url
          print(mainUr)#showing url
          print(xss)#showing <200> if good
          if xss == "requests.exceptions.ConnectionError:":#Error sign(not much to it because there's really not much you can screw up)
              print("Opps seems we ran into a issue..")
          uiii = input("OK, looking good, go to site?:(y/n)")#Checks if user wants to head to the site
          if uiii == 'y':
              webbrowser.open(mainUr)#Uses the webbrowser module to open the url
              sys.exit()#Exits the program
          if uiii == 'n':
                print("Okay have a good day!")
                sys.exit()
        if (url0[i] != " "):
            mainUr = url9+url0#making a full url//##I will mark the change under it
            xss = requests.get(mainUr)#Requesting url
            print(mainUr)#showing url
            print(xss)#showing <200> if good
            if xss == "requests.exceptions.ConnectionError:":#Error sign(not much to it because there's really not much you can screw up)
                 print("Opps seems we ran into a issue..")
            uiii = input("OK, looking good, go to site?:(y/n)")#Checks if user wants to head to the site
            if uiii == 'y':
                webbrowser.open(mainUr)#Uses the webbrowser module to open the url
                sys.exit()
            if uiii == 'n':
                print("Okay have a good day!")
                sys.exit()


def yOutube():
    url0 = input("What are we searching for?: ")
    clear()
    url9 = "https://www.youtube.com/results?search_query="
    for i in range(0, len(url0), 1):
        if (url0[i] == " "):
            url0 = url0.replace(url0[i], "+")#Heres the change i was talking about!
            mainUr = url9+url0
            xss = requests.get(mainUr)
            print(mainUr)
            print(xss)
            if xss == "requests.exceptions.ConnectionError:":
                print("Opps seems we ran into a issue..")
            uiii = input("OK, looking good, go to site?:(y/n)")
            if uiii == 'y':
               webbrowser.open(mainUr)
               sys.exit()
            if uiii == 'n':
                print("Okay have a good day!")
                sys.exit()		
        if (url0[i] != " "):
            mainUr = url9+url0
            xss = requests.get(mainUr)
            print(mainUr)
            print(xss)
            if xss == "requests.exceptions.ConnectionError:":
                print("Opps seems we ran into a issue..")
            uiii = input("OK, looking good, go to site?:(y/n)")
            if uiii == 'y':
                webbrowser.open(mainUr)
                sys.exit()
            if uiii == 'n':
                print("Okay have a good day!")
                sys.exit()		


def sTackOverFlow():
    url0 = input("What are we searching for?: ")
    clear()
    url9 = "https://stackoverflow.com/search?q="
    for i in range(0, len(url0), 1):
        if (url0[i] == " "):
            url0 = url0.replace(url0[i], "+")
            mainUr = url9+url0
            xss = requests.get(mainUr)
            print(mainUr)
            print(xss)
            if xss == "requests.exceptions.ConnectionError:":
                print("Opps seems we ran into a issue..")
            uiii = input("OK, looking good, go to site?:(y/n)")
            if uiii == 'y':
                webbrowser.open(mainUr)
                sys.exit()
            if uiii == 'n':
                print("Okay have a good day!")
                sys.exit()		
        if (url0[i] != " "):
            mainUr = url9+url0
            xss = requests.get(mainUr)
            print(mainUr)
            print(xss)
            if xss == "requests.exceptions.ConnectionError:":#
                print("Opps seems we ran into a issue..")
            uiii = input("OK, looking good, go to site?:(y/n)")
            if uiii == 'y':
                webbrowser.open(mainUr)
                sys.exit()
            if uiii == 'n':
                print("Okay have a good day!")
                sys.exit()		


def dEviantart():
    url0 = input("What are we searching for?: ")
    clear()
    url9 = "https://www.deviantart.com/search?q="
    for i in range(0, len(url0), 1):
        if (url0[i] == " "):
            url0 = url0.replace(url0[i], "%20")
            mainUr = url9+url0
            xss = requests.get(mainUr)
            print(mainUr)
            print(xss)
            if xss == "requests.exceptions.ConnectionError:":
                print("Opps seems we ran into a issue..")
            uiii = input("OK, looking good, go to site?:(y/n)")
            if uiii == 'y':
                webbrowser.open(mainUr)
                sys.exit()
            if uiii == 'n':
              print("Okay have a good day!")
              sys.exit()		
        if (url0[i] != " "):
            mainUr = url9+url0
            xss = requests.get(mainUr)
            print(mainUr)
            print(xss)
            if xss == "requests.exceptions.ConnectionError:":
                print("Opps seems we ran into a issue..")
            uiii = input("OK, looking good, go to site?:(y/n)")
            if uiii == 'y':
                webbrowser.open(mainUr)
                sys.exit()
            if uiii == 'n':
                print("Okay have a good day!")
                sys.exit()		


def myAnimeList():
    url0 = input("What are we searching for?: ")
    clear()
    url9 = "https://myanimelist.net/search/all?q="
    urlx = "&cat=all"
    for i in range(0, len(url0), 1):
        if (url0[i] == " "):
            url0 = url0.replace(url0[i], "%20")
            mainUr = url9+url0+urlx
            xss = requests.get(mainUr)
            print(mainUr)
            print(xss)
            if xss == "requests.exceptions.ConnectionError:":
                print("Opps seems we ran into a issue..")
            uiii = input("OK, looking good, go to site?:(y/n)")
            if uiii == 'y':
                webbrowser.open(mainUr)
                sys.exit()
            if uiii == 'n':
              print("Okay have a good day!")
              sys.exit()		
        if (url0[i] != " "):
            mainUr = url9+url0
            xss = requests.get(mainUr)
            print(mainUr)
            print(xss)
            if xss == "requests.exceptions.ConnectionError:":
                print("Opps seems we ran into a issue..")
            uiii = input("OK, looking good, go to site?:(y/n)")
            if uiii == 'y':
                webbrowser.open(mainUr)
                sys.exit()
            if uiii == 'n':
                print("Okay have a good day!")
                sys.exit()		
        

def wikipedia1():
    url0 = input("What are we searching for?: ")
    clear()
    url9 = "https://en.wikipedia.org/w/index.php?search="
    urlx = "&title=Special:Search&profile=advanced&fulltext=1&advancedSearch-current=%7B%7D&ns0=1"
    for i in range(0, len(url0), 1):
            if (url0[i] == " "):
                url0 = url0.replace(url0[i], "+")
                mainUr = url9+url0+urlx
                xss = requests.get(mainUr)
                print(mainUr)
                print(xss)
                if xss == "requests.exceptions.ConnectionError:":
                    print("Opps seems we ran into a issue..")
                uiii = input("OK, looking good, go to site?:(y/n)")
                if uiii == 'y':
                    webbrowser.open(mainUr)
                    sys.exit()
                if uiii == 'n':
                    print("Okay have a good day!")
                    sys.exit()		
            if (url0[i] != " "):
                mainUr = url9+url0
                xss = requests.get(mainUr)
                print(mainUr)
                print(xss)
                if xss == "requests.exceptions.ConnectionError:":
                    print("Opps seems we ran into a issue..")
                uiii = input("OK, looking good, go to site?:(y/n)")
                if uiii == 'y':
                    webbrowser.open(mainUr)
                    sys.exit()
                if uiii == 'n':
                    print("Okay have a good day!")
                    sys.exit()		


def Wikihow():
    url0 = input("What are we searching for?: ")
    clear()
    url9 = "https://www.wikihow.com/wikiHowTo?search="
    for i in range(0, len(url0), 1):
        if (url0[i] == " "):
            url0 = url0.replace(url0[i], "+")
            mainUr = url9+url0
            xss = requests.get(mainUr)
            print(mainUr)
            print(xss)
            if xss == "requests.exceptions.ConnectionError:":
                print("Opps seems we ran into a issue..")
            uiii = input("OK, looking good, go to site?:(y/n)")
            if uiii == 'y':
               webbrowser.open(mainUr)
               sys.exit()
            if uiii == 'n':
                print("Okay have a good day!")
                sys.exit()      
        if (url0[i] != " "):
            mainUr = url9+url0
            xss = requests.get(mainUr)
            print(mainUr)
            print(xss)
            if xss == "requests.exceptions.ConnectionError:":
                print("Opps seems we ran into a issue..")
            uiii = input("OK, looking good, go to site?:(y/n): ")
            if uiii == 'y':
                webbrowser.open(mainUr)
                sys.exit()
            if uiii == 'n':
                print("Okay have a good day!")
                sys.exit()      


def custom():
    asker = input("Do you already have a custom you'd like to use?(y/n): ")
    if asker == 'y':
        objread = open("URL.txt", "r")
        txtContent = objread.read();
        print("The URLS you have saved are : ", txtContent)
        custom()
    if asker == "n":
        url0 = input("Whats search url?: ")
        urlx = input("OK its saved in a text file for re using, what are you searching for?: ")
        with open("URL.txt", "w") as f:
            f.write(url0)
            clear()
        for i in range(0, len(url0), 1):
            if (url0[i] == " "):
                url0 = url0.replace(url0[i], "%20")
                mainUr = url0+urlx
                xss = requests.get(mainUr)
                print(mainUr)
                print(xss)
                if xss == "requests.exceptions.ConnectionError:":
                    print("Opps seems we ran into a issue..")
                uiii = input("OK, looking good, go to site?:(y/n)")
                if uiii == 'y':
                    webbrowser.open(mainUr)
                    sys.exit()
                if uiii == 'n':
                    print("Okay have a good day!")
                    sys.exit()		
            if (url0[i] != " "):
                mainUr = url0+urlx
                xss = requests.get(mainUr)
                print(mainUr)
                print(xss)
                if xss == "requests.exceptions.ConnectionError:":
                    print("Opps seems we ran into a issue..")
                uiii = input("OK, looking good, go to site?:(y/n)")
                if uiii == 'y':
                    webbrowser.open(mainUr)
                    sys.exit()
                if uiii == 'n':
                    print("Okay have a good day!")
                    sys.exit()		
    

def adultFilms():
    clear()
    print("*Adult sites*")
    print("\nPornHub == ph")
    print("\nXvideos = xx")
    print("\nRedTube = rt")
    urlx = input("Whats your posion?: ")
    url0 = input("OK, what kind?: ")
    clear()
    if urlx == "ph":
        url9 = "https://www.pornhub.com/video/search?search="
        for i in range(0, len(url0), 1):
            if (url0[i] == " "):
                url0 = url0.replace(url0[i], "+")
            mainUr = url9+url0
            xss = requests.get(mainUr)
            print(mainUr)
            print(xss)
            if xss == "requests.exceptions.Connection":
                print("Opps seems we ran into a issue..")
            uiii = input("OK, looking good, go to site(y/n:")
            if uiii == 'y':
                webbrowser.open(mainUr)
                sys.exit()
            if uiii == 'n':
                print("Okay have a good day!")
                sys.exit()		
            if (url0[i] != " "):
                mainUr = url9+url0
                xss = requests.get(mainUr)
                print(mainUr)
                print(xss)
                if xss == "requests.exceptions.Connection":
                    print("Opps seems we ran into a issue..")
                uiii = input("OK, looking good, go to site(y/n):")
                if uiii == 'y':
                    webbrowser.open(mainUr)
                    sys.exit()
                if uiii == 'n':
                    print("Okay have a good day!")
                    sys.exit()		
    if urlx == "xx":
        url9 = "https://www.xvideos.com/?k="
        for i in range(0, len(url0), 1):
            if (url0[i] == " "):
                url0 = url0.replace(url0[i], "+")
                mainUr = url9+url0
                xss = requests.get(mainUr)
                print(mainUr)
                print(xss)
                if xss == "requests.exceptions.Connection":
                    print("Opps seems we ran into a issue..")
            uiii = input("OK, looking good, go to site(y/n:")
            if uiii == 'y':
                webbrowser.open(mainUr)
                sys.exit()
            if uiii == 'n':
                print("Okay have a good day!")
                sys.exit()		
            if (url0[i] != " "):
                mainUr = url9+url0
                xss = requests.get(mainUr)
                print(mainUr)
                print(xss)
                if xss == "requests.exceptions.Connection":
                    print("Opps seems we ran into a issue..")
                uiii = input("OK, looking good, go to site(y/n):")
                if uiii == 'y':
                    webbrowser.open(mainUr)
                    sys.exit()
                if uiii == 'n':
                    print("Okay have a good day!")
                    sys.exit()
    if urlx == "rt":
        url9 = "https://www.redtube.com/?search="
        for i in range(0, len(url0), 1):
            if (url0[i] == " "):
                url0 = url0.replace(url0[i], "+")
                mainUr = url9+url0
                xss = requests.get(mainUr)
                print(mainUr)
                print(xss)
                if xss == "requests.exceptions.Connection":
                    print("Opps seems we ran into a issue")
                uiii = input("OK, looking good, go to site(y/n:")
                if uiii == 'y':
                    webbrowser.open(mainUr)
                    sys.exit()
                if uiii == 'n':
                    print("Okay have a good day!")
                    sys.exit()		
            if (url0[i] != " "):
                mainUr = url9+url0
                xss = requests.get(mainUr)
                print(mainUr)
                print(xss)
                if xss == "requests.exceptions.Connection":
                    print("Opps seems we ran into a issue..")
                uiii = input("OK, looking good, go to site(y/n:")
                if uiii == 'y':
                    webbrowser.open(mainUr)
                    sys.exit()
                if uiii == 'n':
                    print("Okay have a good day!")
                    sys.exit()                


def fullInfo():
    url0 = input("What are we searching for?: ")
    clear()
    url9 = "https://www.wikihow.com/wikiHowTo?search="#You can change these links to your liking 
    urlx = "https://en.wikipedia.org/w/index.php?search="
    urlx1 = "https://stackoverflow.com/search?q="
    urlx2 = "https://www.youtube.com/results?search_query="
    urlx3 = "https://www.reddit.com/search?q="#If you'd like to add more ill tagg the areas that need to be added such as here with @
    for i in range(0, len(url0), 1):
        if (url0[i] == " "): 
            url0 = url0.replace(url0[i], "+")
            mainUr1 = url9+url0#@@@@@@@
            mainUr2 = urlx+url0#Combines the search and urls
            mainUr3 = urlx1+url0
            mainUr4 = urlx2+url0
            mainUr5 = urlx3+url0
            xss = requests.get(mainUr1)#@@@@@@@@
            xss1 = requests.get(mainUr2)#Requests the urls and see if the search is fine 
            xss2 = requests.get(mainUr3)
            xss3 = requests.get(mainUr4)
            xss4 = requests.get(mainUr5)
            print("WikiHow:"+mainUr1, "Wiki:"+mainUr2, "StackOverFlow:"+mainUr3, "Youtube:"+mainUr4, "Reddit:"+mainUr5)#Printing name/url for user
            print("WikiHow:")#Couldn't add this all to one print function but this says the name and the request for user
            print(xss)
            print("Wiki:")
            print(xss1)
            print("StackOverFlow:")
            print(xss2)
            print("Youtube:")
            print(xss3)
            print("Reddit:")
            print(xss4)  
            if xss == "requests.exceptions.ConnectionError:":#if theres a error this should show(Not sure have yet to test it, Could add for every site but thats just cluttering already cluttered code)
                print("Opps seems we ran into a issue..")
            uiii = input("OK, looking good, go to site?:(y/n): ")
            if uiii == 'y':
                webbrowser.open(mainUr1)#@@@@@@@@@@
                webbrowser.open(mainUr2)#Opens url
                webbrowser.open(mainUr3)
                webbrowser.open(mainUr4)
                webbrowser.open(mainUr5)
                sys.exit()
            if uiii == 'n':
                print("Okay have a good day!")
                sys.exit()      
        if (url0[i] != " "):
            mainUr1 = url9+url0#@@@@@@@@@@@@
            mainUr2 = urlx+url0
            mainUr3 = urlx1+url0
            mainUr4 = urlx2+url0
            mainUr5 = urlx3+url0
            xss = requests.get(mainUr1)#@@@@@@@@@@@@@
            xss1 = requests.get(mainUr2)
            xss2 = requests.get(mainUr3)
            xss3 = requests.get(mainUr4)
            xss4 = requests.get(mainUr5)
            print("The sites loaded are: ")
            print("WikiHow:"+mainUr1, "Wiki:"+mainUr2, "StackOverFlow:"+mainUr3, "Youtube:"+mainUr4, "Reddit:"+mainUr5)
            print("\nif all 5 below are 200 you should be good!")
            print("\n------------------------------------")
            print("WikiHow:")
            print(xss)
            print("Wiki:")
            print(xss1)
            print("StackOverFlow:")
            print(xss2)
            print("Youtube:")
            print(xss3)
            print("Reddit:")
            print(xss4)  
            if xss == "requests.exceptions.ConnectionError:":
                print("Opps seems we ran into a issue..")
            uiii = input("OK, looking good, go to site?(y/n): ")
            if uiii == 'y':
                webbrowser.open(mainUr1)#@@@@@@@@@@@@
                webbrowser.open(mainUr2)
                webbrowser.open(mainUr3)
                webbrowser.open(mainUr4)
                webbrowser.open(mainUr5)
                sys.exit()
            if uiii == 'n':
                print("Okay have a good day!")
                sys.exit()      

          


    
print("""
....._      
 `.   ``-.                               .-----.._
   `,     `-.                          .:      /`   
     :       `"..                 ..-``       :     
     /   ...--:::`n            n.`::...       :     
     `:``      .` ::          /  `.     ``---..:.   
       `\    .`  ._:   .-:   ::    `.     .-``      
         :  :    :_\\_/: :  .::      `.  /          
         : /      \-../:/_.`-`         \ :
         :: _.._  q` p ` /`             \|         
         :-`    ``(_. ..-----hh``````/-._:   
                     `:      ``     /     `
                     E:            /
         0          :          _/
        /{}\             :    _..-``
         /\             l--``
""")

def choic():
    print("*SITE CHOICES*")
    print("\nYoutube = y //MyAnimeList = mal")
    print("\nReddit = r //Wikipedia = w")
    print("\nStackOverFlow = sf //WikiHow = wh")
    print("\nDeviantart = d //NEXT_PAGE = p2")


def start():
    ffinp = input("Good day! Would you like to see the list?:(y/n): ")
    if ffinp == "n":
        finp = input("\nWhats the choice today sir?: ")
        if finp == "fi":
            fullInfo()
        if finp == "y":
            yOutube()
        if finp == 'r':
            rEddit()    
        if finp == 'sf':
            sTackOverFlow()
        if finp == 'd':
            dEviantart()
        if finp == 'mal':
            myAnimeList()  
        if finp == 'w':
            wikipedia1()
        if finp == "cc":
            custom()
        if finp == "dtf":
            adultFilms()                      
    if ffinp == "y":
            choic()
            finp = input("\nWhats the choice today sir?: ")
            if finp == "y":
                yOutube()
            if finp == 'r':
                rEddit()    
            if finp == 'sf':
                sTackOverFlow()
            if finp == 'd':
                dEviantart()
            if finp == 'mal':
                myAnimeList()  
            if finp == 'w':
                wikipedia1()
            if finp == "cc":
                custom()
            if finp == 'wh':
                Wikihow()
            if finp == "dtf":
                adultFilms()
            if finp == "fi":
                fullInfo()
            if finp == "p2":
                clear()
                print("*PAGE 2*")
                print("\nCustom = cc")
                print("\nShow adult sites = dtf")
                print("Full info search(5 searchs) = fi")
                print("Restarting system..")
                print("_________________________________________")
                start()                      
    if ffinp != "y" or "n":
            print("Uh, No caps please")





start()
