import random
import string
import time
import sys 


#This small script will take input at launch and try to guess what you put as input randomly.

pass_at = set()

attempts = 0

def crack(passw):
    passw = f"{passw}"
#Set these three to anything you want to speed up the start times.
    start_range = input("Start Range: ")

    end_range = input("End Range: ")

    asked_speed = input("1.Fast 2.Slow \n --Choose a number-- \n ---Fast won't show attempts--- \n :")


#Slow just prints off anything that it attempts, this will really slow things down..Hence the name! 
    def slow():
        pass_at = set()
        start_time = time.time()
        attempts = 0
        pchoice = ""
        while pchoice != passw:
            random_cho = random.randint(int(start_range), int(end_range))
            #Remove any string from here(cchar) or on the slow speed to speed up things(this is just the type of printable characters)
            cchar =  string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
            pchoice = ''.join(random.choices(cchar, k=random_cho))
            if pchoice in pass_at:               
                pass 
            elif pchoice not in pass_at:
                pass_at.add(pchoice)
                attempts += 1
                #continue
            if pchoice == passw:
                end_time = time.time()
                t_output = end_time - start_time
                print("Password is: \n------------")
                print(pchoice)
                print("------------\n Took %.2f seconds to figure out!" % t_output)
                print("Also took this many attempts..", attempts)
                #print(pass_at)
                break
            else:
                print(pchoice)


    def fast():
        pass_at = set()
        start_time = time.time()
        attempts = 0
        pchoice = ""
        while pchoice != passw:
            random_cho = random.randint(int(start_range), int(end_range))
            #Remove any string from here(cchar) or on the slow speed to speed up things(this is just the type of printable characters)
            cchar =  string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
            pchoice = ''.join(random.choices(cchar, k=random_cho))
            if pchoice in pass_at:               
                pass 
            elif pchoice not in pass_at:
                pass_at.add(pchoice)
                attempts += 1
                #continue
            if pchoice == passw:
                end_time = time.time()
                t_output = end_time - start_time
                print("Password is: \n------------")
                print(pchoice)
                print("------------\n Took %.2f seconds to figure out!" % t_output)
                print("Also took this many attempts..", attempts)
                #print(pass_at)
                break


    if asked_speed == "1":
        fast()


    if asked_speed == "2":
        slow()

#Just making sure you gave some type of input.. 
if __name__ == "__main__":
    if len(sys.argv) > 1:
        variable_value = sys.argv[1]
        crack(variable_value)
    else:
        print("Please provide input with script like such: \n python3 script.py password")

