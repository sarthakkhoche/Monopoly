import pygame  #The main module!
import time    #To delay the execution of a certain code, as will be explained wherever used!
import random  #To generate a random number, substituting the actual dice!
import pygame.mixer #For sound effects

pygame.init()       #pygame initialisation
pygame.font.init()  #font initialisation
pygame.mixer.init() #sounds initialisation

#Colors according to RGB conventions, which is compatible with pygame
white =        (255,255,255)
red =          (255,0,0)
lightred =     (100,0,0)
blue =         (0,50,100)
darkblue =     (0,0,255)
green =        (0,255,0)
yellow =       (250,150,0)
lightyellow =  (200,150,0)
black =        (0,0,0)
lightgreen =   (34,177,76)
lightblue =    (205, 230, 208)
violet =       (0, 0, 128)
cream =        (255, 228, 181)

#Dimensions, and title of the main screen.
display_width=1300
display_height=710
gamedisplay=pygame.display.set_mode((display_width, display_height)) #Screen Dimension
pygame.display.set_caption('MONOPOLY') #Title

#Dimensions of marbles for both the players
x1 = 267 
y1 = 536
x2 = 267
y2 = 566

#Fonts initialisation
font = pygame.font.Font(None, 25)
verysmallfont = pygame.font.SysFont("comicsansms",15)
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

#Function which helps to print message on the screen
def message_to_screen(msg, color):
    screen_text = font.render(msg , True , color)
    gamedisplay.blit(screen_text, [display_width/2, display_height/2])

#Dice function which generates a random number between 1 to 6
a=0
def dice():
	b=0
	global a
	a=random.randint(1,6)
    	b=b+a
	if(b>22):
		b=b-22 #Since 22 blocks in our board, one lap completion will result in a decrease of 22
	#print b
	return b


#Used in the main game loop, helps to switch between chances of different players
def alternate():
    global alt
    alt=not alt
    return alt
alt=True  #The first call to alternate will return False (0)

#The cost function which deducts or increases the 'CashinHand' of player, whenever the player lands on a certain box.
initial_cost1=50000
def amountp1():
			global x1
			global y1
			global initial_cost1
			if(x1<341 and y1<610 and y1>500):
                            initial_cost1 -= 0 #Start
                        elif(x1<341 and y1<500 and y1>415):
			    initial_cost1-=250
                        elif(x1<341 and y1<415 and y1>321):
                            initial_cost1 -= 500
                        elif(x1<341 and y1<321 and y1>240):
                            initial_cost1 += 700  #Chance
                        elif(x1<341 and y1<240 and y1>159):
                            initial_cost1 -= 2250
                        elif(x1<341 and y1<159 and y1>53):
                            initial_cost1 -= 1000  #Jail

                        elif(y1<159 and x1<487 and x1>341):
                            initial_cost1 -= 1250
                        elif(y1<159 and x1<621 and x1>487):
                            initial_cost1 -= 500
                        elif(y1<159 and x1<725 and x1>621):
                            initial_cost1 -= 1000 #Community chest!
                        elif(y1<159 and x1<852 and x1>725):
                            initial_cost1 -= 1750
                        elif(y1<159 and x1<972 and x1>852):
                            initial_cost1 -= 750
                        elif(y1<159 and x1<1095 and x1>972):
                            initial_cost1 -= 0  #Free ride!

                        elif(x1>972 and y1<253 and y1>159):
                            initial_cost1 -= 750
                        elif(x1>972 and y1<327 and y1>253):
                            initial_cost1 -= 500 #Community chest
                        elif(x1>972 and y1<423 and y1>327):
                            initial_cost1 -= 250
                        elif(x1>972 and y1<500 and y1>423):
                            initial_cost1 -= 1250
                        elif(x1>972 and y1<610 and y1>500):
                            initial_cost1 -= 1000 #Go to jail

                        elif(y1>500 and x1<972 and y1>854):
                            initial_cost1 -= 2500
                        elif(y1>500 and x1<854 and y1>729):
                            initial_cost1 += 1500 #Chance
                        elif(y1>500 and x1<729 and y1>621):
                            initial_cost1 -= 1500
                        elif(y1>500 and x1<621 and y1>486):
                            initial_cost1 -= 750
                        elif(y1>500 and x1<486 and y1>341):
                            initial_cost1 -= 500
			return initial_cost1

#Same for player 2
initial_cost2=50000
def amountp2():
			global x2
			global y2
			global initial_cost2
 			if(x2<341 and y2<610 and y2>500):
                            initial_cost2 -= 0 #Start
                        elif(x2<341 and y2<500 and y2>415):
                            initial_cost2 -= 250
                        elif(x2<341 and y2<415 and y2>321):
                            initial_cost2 -= 500
                        elif(x2<341 and y2<321 and y2>240):
                            initial_cost2 += 700  #Chance
                        elif(x2<341 and y2<240 and y2>159):
                            initial_cost2 -= 2250
                        elif(x2<341 and y2<159 and y2>53):
                            initial_cost2 -= 1000  #Jail

                        elif(y2<159 and x2<487 and x2>341):
                            initial_cost2 -= 1250
                        elif(y2<159 and x2<621 and x2>487):
                            initial_cost2 -= 500
                        elif(y2<159 and x2<725 and x2>621):
                            initial_cost2 -= 1000 #Community chest!
                        elif(y2<159 and x2<852 and x2>725):
                            initial_cost2 -= 1750
                        elif(y2<159 and x2<972 and x2>852):
                            initial_cost2 -= 750
                        elif(y2<159 and x2<1095 and x2>972):
                            initial_cost2 -= 0  #Free ride!

                        elif(x2>972 and y2<253 and y2>159):
                            initial_cost2 -= 750
                        elif(x2>972 and y2<327 and y2>253):
                            initial_cost2 -= 500 #Community chest
                        elif(x2>972 and y2<423 and y2>327):
                            initial_cost2 -= 250
                        elif(x2>972 and y2<500 and y2>423):
                            initial_cost2 -= 1250
                        elif(x2>972 and y2<610 and y2>500):
                            initial_cost2 -= 1000 #Go to jail

                        elif(y2>500 and x2<972 and y2>854):
                            initial_cost2 -= 2500
                        elif(y2>500 and x2<854 and y2>729):
                            initial_cost2 += 1500 #Chance
                        elif(y2>500 and x2<729 and y2>621):
                            initial_cost2 -= 1500
                        elif(y2>500 and x2<621 and y2>486):
                            initial_cost2 -= 750
                        elif(y2>500 and x2<486 and y2>341):
                            initial_cost2 -= 500
			return initial_cost2


#The side function responsible for game controls. i.e. the INSTRUCTION button as well as the quit button! 				
def game_controls():
    gcont= True
    pygame.mixer.music.stop()
    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gamedisplay.fill(cream)
        background= pygame.image.load('display.png')
        gamedisplay.blit(background,(450,0))
        #using the defined text_to_button function in order to produce text to the screen
        text_to_button("INSTRUCTIONS",blue,630,125,50,100)
        text_to_button2("1. The game begins with player '1' rolling the dice. The marble moves the respective number of blocks ahead!",black,428,220,10,10)
        text_to_button2("2. Once on a block, the player must decide whether to buy the property or not(Provided that the given property is not already purchased).",black,495,240,10,10)
        text_to_button2("3. If a player lands on a property which is already purchased, the player has to pay an amount which is equal to one-fourth of the initial property rate, as a visiting rent to the munci",black,599,260,10,10)
        text_to_button2("-pality of the city",black,206,280,10,10)
        text_to_button2("4. Player who finishes three laps of the game fastest, wins.",black,305,300,10,10)
        text_to_button2("   5. If during the gameplay, a person falls short of money provided, this automatically results as awin-situation for another player.",black,467,320,10,10)
        text_to_button2("  6. If a player lands on block of either of 'Chance' or 'Community Chest', the player has to follow the rules of them seperately.",black,456,340,10,10)
        text_to_button2("7. Jail : Player who lands on the 'Jail' block skips one turn                                               ",black,368,360,10,10)
        text_to_button2("8. Free Ride : Player who lands on the 'Free Ride' block gets another turn.",black,333,380,10,10)
        text_to_button("Chance : ",blue,70,415,10,10)
        text_to_button2("Chance is one of the two types of card-drawing spaces in Monopoly. If a player lands on a space marked for 'chance', Uncle Pennybag(the main character of monopoly) draws a card,",black,640,445,10,10)
        text_to_button2("player is entitled to do whatever is written on that card.",black,206,465,10,10)
        text_to_button("Community Chest :",blue,120,500,10,10)
        text_to_button2("Community Chest is another of the two types of card-drawing spaces in Monopoly. If a player lands on a space marked for 'Community Chest', Uncle Pennybag(the main character of ",black,640,530,10,10)
        text_to_button2("monopoly) draws a card, and the player is entitled to do whatever is written on that card.",black,317,550,10,10)

        button("back",300,600,150,40,darkblue,blue,action="back")
        button("quit",900,600,150,40,lightgreen,green,action="quit")
        pygame.display.update()


#The main function responsible for the game-play.Everything after clicking the play button is hard-coded in the given fubction
def gameloop():
    global x1
    global y1
    global x2
    global y2
    pygame.mixer.music.stop()
    gloop=True
    while gloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
		cur=pygame.mouse.get_pos()
		if((765>cur[0]>565 ) and (690>cur[1]>650)):
			if(alternate()==0): #condition for alternate turn using the 'alternate' function
                		for i in range(dice()):
					pygame.mixer.music.stop()
   					pygame.mixer.music.load('dice.mp3')
    					pygame.mixer.music.play(0)
					if(y1>=120 and x1<=267): #Conditions for moving the marbles..
	                	        	y1 -= 85
	                	    	elif(y1<120 and x1 < 1015 and x1 >=267):
	                	        	x1 += 125
	                	    	elif(y1>110 and x1>1015 and y1 < 500):
					            	y1 +=85
	                	    	elif(y1 > 500 and x1 < 1040 and x1 >= 267):
					            	x1 -= 125
				print amountp1()
			else:	#Same for other player
				for i in range(dice()):	
					pygame.mixer.music.stop()	
   					pygame.mixer.music.load('dice.mp3')
    					pygame.mixer.music.play(0)				
					if(y2>=150 and x2<=267):
	                	        	y2 -= 85
	                	    	elif(y2<150 and x2 < 1015 and x2 >=267):
	                	        	x2 += 125
	                	    	elif(y2>140 and x2>1015 and y2 < 500):
					            	y2 +=85
	                	    	elif(y2 > 500 and x2 < 1040 and x2 >= 267):
					            	x2 -= 125
				print amountp2()
    	    elif event.type==pygame.MOUSEBUTTONUP:
		pass
	    if(initial_cost1<=0 or initial_cost2<=0): #THe winning condition
		gameover = font.render("Gameover",1, green)
		gamedisplay.blit(gameover,[660,640])
		pygame.quit()
                quit()
	    
        gamedisplay.fill(cream)
        background1= pygame.image.load('board1.jpeg')
        gamedisplay.blit(background1, (220,50))
        button("ROLL THE DICE", 565, 650, 200, 40, darkblue, green, action="roll")

        pygame.draw.circle(gamedisplay, green, [x1, y1], 10) #Marbles on screen
        pygame.draw.circle(gamedisplay, blue, [x2, y2], 10)  #Cordinates are in form of variables, for their movement!

	#printing all player related information on the screen
        player1_heading = font.render("Player 1",1, green)
        player1_subheading = font.render('CashinHand:'+str(initial_cost1), 1, black)
        gamedisplay.blit(player1_heading,[70,186])
        gamedisplay.blit(player1_subheading,[40,220])
        player2_heading = font.render("Player 2",1,blue)
        player1_subheading = font.render('CashinHand:'+str(initial_cost2), 1, black)
        gamedisplay.blit(player2_heading,[1165,186])
        gamedisplay.blit(player1_subheading,[1120,220])
	dicenumber = pygame.font.Font(None, 75)
	text1 = dicenumber.render(str(a),1,black)
	gamedisplay.blit(text1,[642,290])
        pygame.display.update()

#The button fuction responsible for creating buttons throughout the code, and redirecting to the appropriate function after the mouse click
def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x+width > cur[0] > x) and (y+height > cur[1]> y):
        pygame.draw.rect(gamedisplay, active_color, (x, y, width, height))
        text_to_button(text, black ,x, y, width, height)
        if click[0] == 1 and action != None :
            if action == "quit": #the actions redirect to the corresponding function
                pygame.quit()
                quit()
            if action == "controls":
                game_controls()
            if action == "play":
                gameloop()
            if action == "back":
                game_intro()
            if action == "roll":
		
                pygame.display.update()

    else:
        pygame.draw.rect(gamedisplay,inactive_color,(x,y,width,height))
        text_to_button(text,black,x,y,width,height)

def text_objects(text, color, size=None):
    textsurface=verysmallfont.render(text,True,color)
 
    if size == "small":
        textsurface = smallfont.render(text,True,color)
    if size == "medium":
        textsurface = medfont.render(text,True,color)
    if size == "large":
        textsurface = largefont.render(text,True,color)

    return textsurface,textsurface.get_rect()

#All text_to_button functions have the same functionality, i.e. to produce text to the screen. The only difference is the font size!!
def text_to_button(msg, color, button_x, button_y, button_width, button_height, size="small"):
        textsurf, textrect = text_objects(msg,color,size)
        textrect.center=((button_x+(button_width/2)), button_y+(button_height/2))
        gamedisplay.blit(textsurf, textrect)

def text_to_button2(msg,color,buttonx,buttony,buttonwidth,buttonheight, size="verysmall"):
        textsurf,textrect = text_objects(msg,color,size)
        textrect.center=((buttonx+(buttonwidth/2)),buttony+(buttonheight/2))
        gamedisplay.blit(textsurf,textrect)

def text_to_button3(msg,color,buttonx,buttony,buttonwidth,buttonheight, size="large"):
        textsurf,textrect = text_objects(msg,color,size)
        textrect.center=((buttonx+(buttonwidth/2)),buttony+(buttonheight/2))
        gamedisplay.blit(textsurf,textrect)

#The very first function which runs as soon as the game starts
def game_intro():
    time.sleep(0.2)
    pygame.mixer.music.load('monopoly.mp3') #Sound in the background
    pygame.mixer.music.play(0)
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gamedisplay.fill(violet)
        background2= pygame.image.load('monopoly2.jpeg')
        background= pygame.image.load('monopoly.jpeg') #Image in the background
	gamedisplay.blit(background2, (0, 0))
        gamedisplay.blit(background, (450, 200)) #Adding the image

        button("PLAY",300,500,150,40, darkblue, blue, action="play") #Creating buttons using the predefined function 'button'
        button("INSTRUCTIONS",570,500,220,40, lightyellow, yellow, action="controls")
        button("QUIT",900,500,150,40, lightgreen, green, action="quit")

        pygame.display.update()

game_intro()
gameloop()
