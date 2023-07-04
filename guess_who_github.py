from random import randint
import pygame as pg
import os
import mysql.connector



db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "indovina_chi",
)

cursor = db.cursor()


pg.init()
        
#Create the suonds functions

def correct():
    pg.mixer.music.load("Correct.mp3")
    pg.mixer.music.play(1, 0.0)

def error():
    pg.mixer.music.load("Error.mp3")
    pg.mixer.music.play(1, 0.0)

def winning():
    pg.mixer.music.load("Winning.mp3")
    pg.mixer.music.play(1, 0.0)


#Inizialization variables
#Single
SingleP=0
#Squad
red_squad=0
blue_squad=0
#Index for the cicle for
i=0
x=0
#Set point
point=0
#Set Loop
loop = True
#Set Random
random = 0
randomB = True
squad = str
utente = str
#Risultati
risultati = None

#Database Creation
cursor.execute("SELECT * FROM GUESS1")
risultati = cursor.fetchall()

'''
 ██████   █████  ███    ███ ███████ ██████  ██       █████  ██    ██     ███████ ██    ██ ███    ██  ██████ ████████ ██  ██████  ███    ██ 
██       ██   ██ ████  ████ ██      ██   ██ ██      ██   ██  ██  ██      ██      ██    ██ ████   ██ ██         ██    ██ ██    ██ ████   ██ 
██   ███ ███████ ██ ████ ██ █████   ██████  ██      ███████   ████       █████   ██    ██ ██ ██  ██ ██         ██    ██ ██    ██ ██ ██  ██ 
██    ██ ██   ██ ██  ██  ██ ██      ██      ██      ██   ██    ██        ██      ██    ██ ██  ██ ██ ██         ██    ██ ██    ██ ██  ██ ██ 
 ██████  ██   ██ ██      ██ ███████ ██      ███████ ██   ██    ██        ██       ██████  ██   ████  ██████    ██    ██  ██████  ██   ████   
                                                                                                                                       '''

def gameplay(i, loop):
    global risultati
    global point
    global randomB
    while loop:
        if(point == 3):
            loop = False
            print(i+1," round")

        if randomB:
            random = randint(1,5)
            
            cursor.execute("SELECT * FROM guess1 where id = %s", (random,))
            persone = cursor.fetchone()
            
            randomB = False
        
        utente = str(input("What do you ask? (Hair color, Hair length, Gender, Facial hair, Glasses or guess who) "))
        if(utente.lower() == "guess who" or i == 3):
            if(i == 3):
                print("You finish your attemp now you must try the person")
            else: 
                print("come on let's try the person ")
            for i in range(0,2):
                guess = str(input("Who is? "))
            
                if guess.lower() == persone[1].lower():
                    correct()
                    print("Congratulation it's correct!")
                    point+=1
                    randomB = True
                    break
                else:
                    error()
                    print("It's not correct, try again. You can try ", 2-i, " times")
        elif utente == "Glasses" or utente == "glasses":
            print(persone[2])

        elif utente == "Hair length" or utente == "hair length":
            print(persone[4])

        elif utente == "Hair color" or utente == "hair color":
            print(persone[3])

        elif utente == "Facial hair" or utente == "facial hair":
            print(persone[5])

        elif utente == "Gender" or utente == "gender":
            print(persone[6])

        elif utente == "Stop" or utente == "stop":
            loop = False
        i+=1
            



               
'''
███████  ██████  ██    ██  █████  ██████      ███████ ██    ██ ███    ██  ██████ ████████ ██  ██████  ███    ██ 
██      ██    ██ ██    ██ ██   ██ ██   ██     ██      ██    ██ ████   ██ ██         ██    ██ ██    ██ ████   ██ 
███████ ██    ██ ██    ██ ███████ ██   ██     █████   ██    ██ ██ ██  ██ ██         ██    ██ ██    ██ ██ ██  ██ 
     ██ ██ ▄▄ ██ ██    ██ ██   ██ ██   ██     ██      ██    ██ ██  ██ ██ ██         ██    ██ ██    ██ ██  ██ ██ 
███████  ██████   ██████  ██   ██ ██████      ██       ██████  ██   ████  ██████    ██    ██  ██████  ██   ████ 
            ▀▀                                                                                              '''
        

def Squad():
    global red_squad
    global blue_squad
    loop = True

    for x in range(0,3):
        print("You're red Squad")
        gameplay(i, loop,)
        red_squad+=point
        point = 0
        
        print("You're blue squad")
        gameplay(i, loop,)
        blue_squad = point
        x+=1
       

    if(red_squad > blue_squad):
        winning()
        print("Red Squad win!!")
    elif(blue_squad > red_squad):
        winning()
        print("Blue squad win!!")
    else:
        print("Draw")

'''
███████ ██ ███    ██  ██████  ██      ███████     ███████ ██    ██ ███    ██  ██████ ████████ ██  ██████  ███    ██ 
██      ██ ████   ██ ██       ██      ██          ██      ██    ██ ████   ██ ██         ██    ██ ██    ██ ████   ██ 
███████ ██ ██ ██  ██ ██   ███ ██      █████       █████   ██    ██ ██ ██  ██ ██         ██    ██ ██    ██ ██ ██  ██ 
     ██ ██ ██  ██ ██ ██    ██ ██      ██          ██      ██    ██ ██  ██ ██ ██         ██    ██ ██    ██ ██  ██ ██ 
███████ ██ ██   ████  ██████  ███████ ███████     ██       ██████  ██   ████  ██████    ██    ██  ██████  ██   ████
                                                                                                                '''


def Single(i, loop, username):
    global SingleP
    global pointM
    
    gameplay(i, loop)
    cursor.execute("SELECT pointM FROM point WHERE Name = %s", (username,))
    pointM = cursor.fetchone()
    if(pointM[0] > point):
        print("You didn't break your record ")
        
    elif(pointM[0] < point):
        print("Nice you break your record!! This is your new record", point)
        cursor.execute("UPDATE point SET pointM = %s WHERE name = %s", (point, username))
        db.commit()

    else:
        print("You equalized your record", point)



'''
██       ██████   ██████  ██ ███    ██     ███████ ██    ██ ███    ██  ██████ ████████ ██  ██████  ███    ██ 
██      ██    ██ ██       ██ ████   ██     ██      ██    ██ ████   ██ ██         ██    ██ ██    ██ ████   ██ 
██      ██    ██ ██   ███ ██ ██ ██  ██     █████   ██    ██ ██ ██  ██ ██         ██    ██ ██    ██ ██ ██  ██ 
██      ██    ██ ██    ██ ██ ██  ██ ██     ██      ██    ██ ██  ██ ██ ██         ██    ██ ██    ██ ██  ██ ██ 
███████  ██████   ██████  ██ ██   ████     ██       ██████  ██   ████  ██████    ██    ██  ██████  ██   ████
                                                                                                         '''


def Login():
    login = input("Have you ever played? Yes or No ")
    if login.lower() == "yes":
        username = str(input("Insert your username: "))
        cursor.execute("SELECT Name FROM point WHERE Name = %s", (username,))
        name = cursor.fetchone()
        
        print("Welcome back to our game ",name[0]," !")
        Single(i, loop, username)
    elif login.lower() == "no":
        valore=True
        index = 0
        while True:
            username = input("Insert your username: ")
            cursor.execute("SELECT name FROM point")
            totName = cursor.fetchall()
            lengthTotName = len(totName)
            while(index <= lengthTotName-1):
                if username == totName[index][0]:
                    print("Username not Aviable. Choose another username.")
                    valore=False
                    break
                index+=1
            if valore:
                cursor.execute("INSERT INTO point(Name) VALUES(%s)", (username,))
                db.commit()
                print("Welcome to our game ", username, "!")
                Single(i, loop, username)
                break
            print("This username is already used")



'''
 █████  ███████ ██   ██     ███    ███  ██████  ██████   █████  ██      ██ ████████ ██    ██ 
██   ██ ██      ██  ██      ████  ████ ██    ██ ██   ██ ██   ██ ██      ██    ██     ██  ██  
███████ ███████ █████       ██ ████ ██ ██    ██ ██   ██ ███████ ██      ██    ██      ████   
██   ██      ██ ██  ██      ██  ██  ██ ██    ██ ██   ██ ██   ██ ██      ██    ██       ██    
██   ██ ███████ ██   ██     ██      ██  ██████  ██████  ██   ██ ███████ ██    ██       ██ 
                                                                                         '''

#Ask modality
while True:
    modality = str(input("Choose a modality. Single or Squad "))

    if(modality == "Single" or modality == "single"):
        Login()
        print("Thanks to playng our game! ")
        break
        

    elif(modality == "Squad" or modality == "squad"):
        Squad()
        print("Thanks to playng our game! ")
        break
    
    else:
        print("It's not exist. Check the syntax")
   


cursor.close()
db.close()
