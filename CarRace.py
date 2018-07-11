
#Import tqdm and time from library
import time
from tqdm import tqdm

#Simple progress bar
for i in tqdm(range(100)):
    time.sleep(0.03)

#Importing pygame library as 'py'
import pygame as py
import random

#Initialisation of the pygame function
py.init()

# Assigning variables
# display height and width variables
display_width=400                   #Actually 'height'
display_height=600                  #Actually 'width'

#Cars width and height
car_width=23
car_height=28
enemy_width=23
enemy_height=28


#Assigning variables for colors to be used in game loop inside game
#Defining colors as RGB (255 by 255 by 255)
black=(0,0,0)
white=(255,255,255)
white_B=(230,255,255)
back=(108,108,108)
green_lime=(50,205,50)
green_forest=(34,139,34)
water_blue=(0,135,255)
water_blue_1=(0,135,215)
water_blue_2=(0,135,175)

#Setting up display using display.set_mode() function
gameDisplay=py.display.set_mode((display_height,display_width))

#Setting up title name for the game
py.display.set_caption('Pixel Race: INFINITY ')

#Assigning variable for the game_icon
game_icon=py.image.load("Sprites/Game_Icon.png")
py.display.set_icon(game_icon)

#Global clock() function for gloabal variables
clock=py.time.Clock()

#Passing pause parameter as a global boolean to be used inside Pause_Menu()
pause = True

#Assigning global font
#If Sysfont() are not initialised then global font is to be taken by the function
font = py.font.SysFont("freesansbold.tff", 72)

#Assigning Music and Sound Effects as variables
crash_sound=py.mixer.Sound('sound/Car_Crash.wav')
slide_sound=py.mixer.Sound('sound/Car_Slide.wav')
bonus_sound=py.mixer.Sound('sound/Car_Bonus.wav')
py.mixer.music.load('sound/Car_Moving.wav')
Game_intro_sound=py.mixer.Sound('sound/Game_Intro_Sound.wav')
Button_Press=py.mixer.Sound('sound/Button_Press.wav')
Pause_Menu_Sound=py.mixer.Sound('sound/Pause_Sound.wav')

#Function for drawing ROAD stripes
def stripes(stx,sty,stw,sth,color):
    py.draw.rect(gameDisplay,color,[stx,sty,stw,sth+40])

#All sprite images are contained inside the project folder named as Sprites folder

#Function for displaying Enemy Car Image from Sprites
def enemy2(enemy2x,enemy2y):
    car_2=py.image.load('Sprites/Car_Enemy_2.png')
    gameDisplay.blit(car_2,(enemy2x,enemy2y))

#Functoin for displaying Enemy Car image from Sprites
def enemys(enemyx,enemyy):
    car = py.image.load('Sprites/Car_Enemy_1.png')
    gameDisplay.blit(car,(enemyx,enemyy))

#Fcuntion for displaying COW sprite
def Cow(cx,cy):
    cowimg=py.image.load('Sprites/Cow.png')
    gameDisplay.blit(cowimg,(cx,cy))

#Function for displaying Tree image
def Tree(xt,yt):
    treeimg = py.image.load('Sprites/vegetation.png')
    gameDisplay.blit(treeimg,(xt,yt))

#Function for displaying Second Tree image
#Different (x,y) coordinates are assigned for same sprites used for Tree
def Tree2(xt2,yt2):
    treeimg2 = py.image.load('Sprites/vegetation.png')
    gameDisplay.blit(treeimg2,(xt2,yt2))

#Function for displaying Third Tree image
def Tree3(xt3,yt3):
    treeimg3 = py.image.load('Sprites/vegetation.png')
    gameDisplay.blit(treeimg3,(xt3,yt3))

#Function for displaying Fourth Tree imaged
def Tree4(xt4,yt4):
    treeimg4 = py.image.load('Sprites/vegetation.png')
    gameDisplay.blit(treeimg4,(xt4,yt4))

#Function for displaying Rock Image
def Rock(rx,ry):
    rockimg=py.image.load('Sprites/Rock.png')
    gameDisplay.blit(rockimg,(rx,ry))

#Function for diplaying bonus opject
def bonus(fx,fy):
    bonus_img=py.image.load('Sprites/empty_bonus.png')
    gameDisplay.blit(bonus_img,(fx,fy))

#Function for disaplying Eplosion Image for Car_User(player)
def Explosion_User(ex,ey):
    expimg=py.image.load('Sprites/Explosion.png')
    gameDisplay.blit(expimg,(ex-30,ey-28))

#Function for dispalying Explosion image for coordinating with Enemy_Car
def Explosion_Enemy(ex1,ey1):
    expimg1=py.image.load('Sprites/Explosion.png')
    gameDisplay.blit(expimg1,(ex1-34,ey1-28))

#Function for displaying Car_User image
def Car(x,y):
    #blit draws over background
    car_img=py.image.load('Sprites/Car_User.png')
    gameDisplay.blit(car_img,(x,y))

#Defining a function for game Exit to windows
def quit_game():
    py.quit()
    quit()

#Defining attributes to Button usinf function
def button(msg,x,y,w,h,hx,hy,hand,function=None):

    #Retracing path of mouse pointer
    mouse_point = py.mouse.get_pos()
    click=py.mouse.get_pressed()           #Checking if the mouse if pressed
     #Defining area for button
    if x + w > mouse_point[0] > x and y + h > mouse_point[1] > y:
        gameDisplay.blit(hand, (hx,hy))
        #Checking click over button area defined
        if click[0] == 1 and function!=None:
            py.mixer.Sound.set_volume(Button_Press, 0.5)      #Playing sound variables
            py.mixer.Sound.play(Button_Press)
            time.sleep(0.78)
            function()                        #calling of the function
    else:
        py.draw.rect(gameDisplay, black, (x, y, w, h))
     #Text variable for displaying button text
    smallText = py.font.SysFont('bookman medium', 45)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + 40), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


#Funtion  defining Game menu
def Game_Menu():
    menu=True
    py.mixer.Sound.play(Game_intro_sound,-1)

    while menu:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
        gameDisplay.fill(black)
        game_background = py.image.load('Sprites/background_Menu.png')
        gameDisplay.blit(game_background,(0,0))

        largeText=py.font.SysFont('bookman',68)
        TextSurf,TextRect=text_objects("Pixel Race: INFINITY",largeText)
        TextRect.center=((display_width/2+105),(display_height/2-210))
        gameDisplay.blit(TextSurf,TextRect)

        hand1=py.image.load("Sprites/Hand1.png")
        hand2=py.image.load("Sprites/Hand2.png")
        button("Play",240,180,80,30,180,185,hand1,game_loop)
        button("Quit",240,240,80,30,180,245,hand2,quit_game)

        py.display.update()
        clock.tick(15)

#Defining function for Un-pausing of the game
def unpause():
    global pause
    pause = False
    py.mixer.music.play(-1)
    py.mixer.Sound.stop(Pause_Menu_Sound)

#Defining Pause Menu
def Pause_Menu():
    py.mixer.Sound.set_volume(Pause_Menu_Sound,0.5)
    py.mixer.Sound.play(Pause_Menu_Sound,-1)


    while pause:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()

        gameDisplay.fill(black)
        game_background = py.image.load('Sprites/Background_Menu.png')
        gameDisplay.blit(game_background,(0,0))

        pause_icon=py.image.load('Sprites/pause.png')
        gameDisplay.blit(pause_icon,((display_width/2+60),(display_height/2-210)))

        largeText=py.font.SysFont('bookman',50)
        TextSurf,TextRect=text_objects("Game Paused",largeText)
        TextRect.center=((display_width/2+100),(display_height/2-245))
        gameDisplay.blit(TextSurf,TextRect)

        hand1=py.image.load("Sprites/Hand1.png")
        hand2=py.image.load("Sprites/Hand2.png")
        button("Continue",250,210,80,30,165,210,hand1,unpause)
        button("Quit",250,270,80,30,190,275,hand2,quit_game)

        py.display.update()
        clock.tick(15)


#Keeping the check of the score inside Text vairable
def Cars_Notcollided(count):
    font=py.font.SysFont(None,30)
    text = font.render("Score:"+str(count),True,black)
    gameDisplay.blit(text,(510,10))

#Function for displaying msg over game main scene()
def Game_Pause():
    font=py.font.SysFont(None,20)
    text = font.render("Press 'p'",True,black)
    text2 = font.render("to Pause",True,black)
    gameDisplay.blit(text,(520,40))
    gameDisplay.blit(text2,(518,58))

#Info msg for Controls
def Game_Contols():
    font=py.font.SysFont(None,25)
    text = font.render("Use",True,black)
    text2 = font.render("W",True,black)
    text3 = font.render("A  S  D",True,black)
    text4 = font.render("to move",True,black)
    gameDisplay.blit(text,(532,290))
    gameDisplay.blit(text2,(540,310))
    gameDisplay.blit(text3,(522,330))
    gameDisplay.blit(text4,(517,350))

#Defining Text objects
def text_objects(text,font):
    textSurface=font.render(text,True,white)
    return textSurface,textSurface.get_rect()

def GameOver_msg(text):

    L_Text=py.font.Font('freesansbold.ttf',32)
    TextSurf,TextRect= text_objects(text,L_Text)
    TextRect.center=(display_width/2+53,20)
    gameDisplay.blit(TextSurf,TextRect)
    py.display.update()
    time.sleep(2.67)
    #Calling of the game_loop() after 2.67 secs
    game_loop()

#Fucntions for text display
def info_msg(text):
    L_Text=py.font.Font('freesansbold.ttf',28)
    TextSurf,TextRect= text_objects(text,L_Text)
    TextRect.center=(display_width/2+53,25)
    gameDisplay.blit(TextSurf,TextRect)
    py.display.update()

def bonus_msg(text):
    L_Text=py.font.Font('freesansbold.ttf',15)
    TextSurf,TextRect= text_objects(text,L_Text)
    TextRect.center=(display_width/2+345,47)
    gameDisplay.blit(TextSurf,TextRect)
    py.display.update()

#Defining crash function
def crash():
    py.mixer.music.stop()
    py.mixer.Sound.play(crash_sound)
    py.mixer.Sound.set_volume(crash_sound,0.5)
    GameOver_msg("GameOver")

def Warn():
    info_msg("Speed UP!!")

def bonus_():
    py.mixer.Sound.play(bonus_sound)
    py.mixer.Sound.set_volume(bonus_sound, 0.1)
    bonus_msg("+Bonus")

#Main scene area for the game
def game_loop():
    time.sleep(1)
    global pause
    py.mixer.Sound.stop(Game_intro_sound)

    #Assinging variables for postion of objects/Sprites over the display area

    #Car_User posi
    x = (display_width*0.60)
    y = (display_height*0.54)
    x_change = 0
    y_change = 0

    #initio for score display
    score = 0

    #Enemy_1 car
    enemy_startx = random.randrange(150,330)
    enemy_starty = -1700
    enemy_speed = 7

    #Enemy_2 Car
    enemy_start2x = random.randrange(150,330)
    enemy_start2y = -22000
    enemy2_speed = 9.2

    #Road Stripes
    stx = (140+359)/2
    sty = -400
    stw = 9
    sth = 40
    st_speed = 8

    #Tree_1
    xt = random.randrange(55,95)
    yt = -120
    yt_speed = 3.67

    #Tree_2
    xt2=random.randrange(360,390)
    yt2 = -200
    yt_speed2 = 3.67

    #Tree_3
    xt3 = random.randrange(390,410)
    yt3 = -400
    yt_speed3 = 3.67

    #Tree_4
    xt4 = random.randrange(0,40)
    yt4 = -600
    yt_speed4 = 3.67

    #Rock
    rx=415
    ry=-1800
    r_speed=3.47

    #Cow
    cx= random.randrange(10,80)
    cy=-2000
    cy_speed= 3.47

    #Bonus
    fx=random.randrange(140,320)
    fy=-16000
    fy_speed=6.89

    py.mixer.music.play(-1)
    py.mixer.music.set_volume(0.7)

    Exit=False

    while not Exit:

        #Event handling Loop for game checking for the keys being pressed
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
            if event.type==py.KEYDOWN:
                if event.key==py.K_a:
                   x_change=-3.5
                   py.mixer.Sound.play(slide_sound)
                   py.mixer.Sound.set_volume(slide_sound,0.4)
                if event.key==py.K_d:
                   x_change=3.5
                   py.mixer.Sound.play(slide_sound)
                   py.mixer.Sound.set_volume(slide_sound,0.4)
                if event.key==py.K_w:
                    y_change=-1.98
                if event.key==py.K_s:
                    y_change=1.5
                if event.key==py.K_p:
                    pause = True
                    py.mixer.music.stop()
                    Pause_Menu()
            if event.type==py.KEYUP:
                if event.key==py.K_a or event.key==py.K_d:
                    x_change=0
            if event.type==py.KEYUP:
                if event.key==py.K_w or event.key==py.K_s:
                    y_change=0

        #Adding pos values to img variables of the Car_User
        x += x_change
        y += y_change

        #Calling of the Sprites as functions declared before loop
        #Layering is done as TOP to BOTTOM proprotionate to LOWER TO UPPER layer
        gameDisplay.fill(back)

        stripes(stx, sty, stw, sth, white)
        sty += st_speed

        enemys(enemy_startx, enemy_starty)
        enemy_starty += enemy_speed

        enemy2(enemy_start2x,enemy_start2y)
        enemy_start2y+=enemy2_speed

        bonus(fx,fy)
        fy+=fy_speed

        #Grass corner
        py.draw.rect(gameDisplay,green_lime,[0,0,140,400])
        py.draw.rect(gameDisplay,green_lime,[370,0,140,400])

        #Grass stripes draw
        py.draw.rect(gameDisplay,green_forest,[0,0,20,400])
        py.draw.rect(gameDisplay,green_forest,[40,0,20,400])
        py.draw.rect(gameDisplay, green_forest, [80, 0, 20, 400])
        py.draw.rect(gameDisplay, green_forest, [120, 0, 20, 400])

        py.draw.rect(gameDisplay,green_forest,[370,0,20,400])
        py.draw.rect(gameDisplay, green_forest, [410, 0, 20, 400])
        py.draw.rect(gameDisplay, green_forest, [450, 0, 20, 400])
        py.draw.rect(gameDisplay, green_forest, [490, 0, 20, 400])


        #Water display using draw
        py.draw.rect(gameDisplay, water_blue, [515, 0, 85, 400])
        py.draw.rect(gameDisplay, water_blue_1, [490, 0, 58, 400])
        py.draw.rect(gameDisplay, water_blue_2, [490, 0, 10, 400])

        py.draw.rect(gameDisplay,white,[140,0,8,400])
        py.draw.rect(gameDisplay,white,[361,0,8,400])

        #Calling of the display functions
        Rock(rx,ry)
        ry+=r_speed

        Tree(xt,yt)
        yt+=yt_speed

        Tree2(xt2, yt2)
        yt2 += yt_speed2

        Cow(cx,cy)
        cy+=cy_speed

        Tree3(xt3,yt3)
        yt3+=yt_speed3

        Tree4(xt4, yt4)
        yt4 += yt_speed4

        Cars_Notcollided(score)
        Game_Pause()
        Game_Contols()

        Car(x,y)

        #Checing for the collision of the car within defined range
        if x > 355.95-car_width or x < 144.55:
            Explosion_User(x,y)
            crash()
        if y > 400-car_height or y < 0:
            Explosion_User(x, y)
            crash()

        #Loop for Enemy_Car_1 to be displayed over and over with y value defined
        if enemy_starty > 450:
            enemy_starty = 0 - enemy_height
            enemy_startx = random.randrange(150,330)

            score += 1  #Adding +1 For score if Enemy_Car_1 avoided
            #Increasing speed  of the game with each frame
            r_speed += 0.005
            st_speed += 0.05
            cy_speed += 0.067
            yt_speed += 0.01
            yt_speed2 += 0.01
            yt_speed3 += 0.01
            yt_speed4 += 0.01
            enemy_speed += 0.06

        #Loop for Enemy_Car_2
        if enemy_start2y > random.randrange(2200,4400):
            enemy_start2y=0-enemy_height
            enemy_start2x=random.randrange(150,330)
            enemy2_speed+=0.07

        #Loop for Road Stripes
        if sty > 490:
            sty=0-sth
            stx=(140+359)/2

        #Loop for Tree_1
        if yt > 650:
            yt=0-sth-30
            xt=random.randrange(55,80)

        #Loop for Trees_2
        if yt2 > 450:
            yt2=0-sth-30
            xt2=random.randrange(350,395)

        #Loop for Tree_3
        if yt3 > 550:
            yt3=0-sth-30
            xt3=random.randrange(400,410)

        #Loop for Trees_4
        if yt4 > 850:
            yt4=0-sth-30
            xt4=random.randrange(0,40)

        #Loop for Cow
        if cy > 900:
            cy=0-45
            cx=random.randrange(10,75)

        #Loop for Rock image
        if ry > 1200:
            ry=0-50
            rx=415

        if score==30:
            Warn()
            enemy_speed+=0.02
            r_speed += 0.0005
            st_speed += 0.01
            cy_speed += 0.0005
            yt_speed += 0.001
            yt_speed2 += 0.001
            yt_speed3 += 0.001
            yt_speed4 += 0.001

        #Loop for bonus Score
        if fy > random.randrange(22000,42000):
            fx = random.randrange(140,320)
            fy = 0 - 15
            score+=5

        #Crash SQUENCE FOr Enemy 1
        if (enemy_startx+enemy_width>=x>=enemy_startx) and (enemy_starty+enemy_height>=y>=enemy_starty):
            Explosion_User(x,y)
            Explosion_Enemy(enemy_startx,enemy_starty)
            crash()

        if (enemy_startx+enemy_width>=x+car_width>=enemy_startx) and (enemy_starty+enemy_height>=y>=enemy_starty):
            Explosion_User(x, y)
            Explosion_Enemy(enemy_startx, enemy_starty)
            crash()

        if (enemy_startx+enemy_width>=x>=enemy_startx) and (enemy_starty+enemy_height>=y+car_height>=enemy_starty):
            Explosion_User(x, y)
            Explosion_Enemy(enemy_startx, enemy_starty)
            crash()

        if (enemy_startx+enemy_width>=x+car_width>=enemy_startx) and (enemy_starty+enemy_height>=y+car_height>=enemy_starty):
            Explosion_User(x, y)
            Explosion_Enemy(enemy_startx, enemy_starty)
            crash()



        #Crash SQUENCE FOr Enemy 2
        if (enemy_start2x+enemy_width>=x>=enemy_start2x) and (enemy_start2y+enemy_height>=y>=enemy_start2y):
            Explosion_User(x, y)
            Explosion_Enemy(enemy_start2x, enemy_start2y)
            crash()

        if (enemy_start2x+enemy_width>=x+car_width>=enemy_start2x) and (enemy_start2y+enemy_height>=y>=enemy_start2y):
            Explosion_User(x, y)
            Explosion_Enemy(enemy_start2x, enemy_start2y)
            crash()

        if (enemy_start2x+enemy_width>=x>=enemy_start2x) and (enemy_start2y+enemy_height>=y+car_height>=enemy_start2y):
            Explosion_User(x, y)
            Explosion_Enemy(enemy_start2x, enemy_start2y)
            crash()

        if (enemy_start2x+enemy_width>=x+car_width>=enemy_start2x) and (enemy_start2y+enemy_height>=y+car_height>=enemy_start2y):
            Explosion_User(x, y)
            Explosion_Enemy(enemy_start2x, enemy_start2y)
            crash()

        #Bonus score
        if (fx+500>=x>=fx) and (fy+550>=y>=fy):
            bonus_()
        if (fx+500>=x+car_width>=fx) and (fy+550>=y>=fy):
            bonus_()
        if (fx+500>=x>=fx) and (fy+550>=y+car_height>=fy):
            bonus_()
        if (fx+500>=x+car_width>=fx) and (fy+550>=y+car_height>=fy):
            bonus_()


        # or py.display.flip() = updates entire surface
        py.display.update()
        clock.tick(64)

Game_Menu()  #Calling of the Game Menu inside main Game Loop
game_loop()
py.quit()
quit()