
import random
import sys
import pygame
from pygame.locals import*

pygame.init()

RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WHITE=(255,255,255)

# Global Variables
screenwidth = 289
screenlength = 511
sprite = {}
sound = {}
pipe1 = []
pipe2 = []


# Set Screen Size
setscreen = pygame.display.set_mode((screenwidth, screenlength))
pygame.display.set_caption("Flappy Bird by AK.")


# Welcme Screen Funtion
def welcomeScreen():

# Game Loop for Welcome Page
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_UP or event.key==13):
                return
           
                
        setscreen.blit(sprite['message'], (0, 0))
       
        pygame.display.update()

# Generate Random Pipe Height
def Generatepipeheight():
    upperPipeX=int(screenwidth*0.95)
    lowerPipeX=int(screenwidth*0.95)
    
    upperPipeY= random.randrange(
        -int(sprite['pipe1'].get_height()),0)
    
    randomplayersize = random.randrange(
        4*sprite['player'].get_height(), 8*sprite['player'].get_height())
    
    lowerPipeY= sprite['pipe1'].get_height(
    ) + upperPipeY+randomplayersize

    randompipe = [[upperPipeX,upperPipeY],[lowerPipeX,lowerPipeY]]
    return randompipe

# Main Game
def MainGame():

    # local Varriable
    flag=True
    flag1=True
    score=0
    scoreDigit=0
    digit=[]
    flag2=False

    birdX=int(screenwidth/3)
    birdY=int(screenlength/2)

    Pipe=[Generatepipeheight()]
    # print(Pipe)
   


    #  Game Loop
    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                sound['wing'].play()
                birdY=birdY-54

        # if Bird isCollide to lowerPipe
        if(birdY+sprite['player'].get_height())>Pipe[0][1][1] and ( Pipe[0][1][0] <=(birdX+sprite['pipe2'].get_width())<=(Pipe[0][1][0]+sprite['pipe2'].get_width()) or Pipe[0][1][0] <=birdX<=(Pipe[0][1][0]+sprite['pipe2'].get_width()) ):
            sound['hit'].play()
            setscreen.blit(sprite['gameover'], (50,200))
            pygame.display.update()
            break
            
            # print("true")
        # if Bird isCollide to upperPipe
        if birdY<=(Pipe[0][0][1]+sprite['pipe1'].get_height()-20) and ( Pipe[0][0][0]<=(birdX+sprite['player'].get_width())<=(Pipe[0][0][0]+sprite['pipe1'].get_width()) or Pipe[0][0][0]<=birdX<=(Pipe[0][0][0]+sprite['pipe1'].get_width())):
             
            sound['hit'].play()
            setscreen.blit(sprite['gameover'], (50,200))
            pygame.display.update()
            pygame.time.delay(20)
            break
             
            #  print("true1")

        #  if Bird isCollide to upper and lower surface   
        if (birdY+sprite['player'].get_height())>400  or birdY<0:
             sound['hit'].play()
             sound['die'].play()
             setscreen.blit(sprite['gameover'], (50,200))
             pygame.display.update()
             break
            

        # if Bird is get across coloum then score wil increase
        if birdX>(Pipe[0][0][0]+sprite['pipe1'].get_width()) and flag1==True :
            score=score+1
            sound['point'].play()
            flag1=False
            # print(score)
        scoreDigit=score

        # to change score in digit
        while scoreDigit !=0 :
            digit.append(scoreDigit%10)
            scoreDigit=scoreDigit//10
            flag2=True    
            # print(digit)
        # bird is  Droping
        birdY=birdY+15

        # if Coloum is out of screen then delete coloum
        if -57< Pipe[0][0][0]<-52:
            Pipe.pop(0)
            flag1=True
            # print(Pipe)
      

        # to add Coloum
        if 109<Pipe[-1][0][0]<114 and  flag==True:
           
            Pipe.append(Generatepipeheight())
            # print(Pipe)

       
        # Blit All Object In Screen
        setscreen.blit(sprite['background'], (0,0))
        setscreen.blit(sprite['player'], (birdX,birdY))

        setscreen.blit(sprite['pipe1'],(Pipe[0][0][0],Pipe[0][0][1]))
        setscreen.blit(sprite['pipe2'],(Pipe[0][1][0],Pipe[0][1][1]))
        setscreen.blit(sprite['base'],(0,screenlength*0.8))
      
        setscreen.blit(sprite['pipe1'],(Pipe[0][0][0]+180,Pipe[-1][0][1]))
        setscreen.blit(sprite['pipe2'],( Pipe[0][1][0]+180,Pipe[-1][1][1]))
        setscreen.blit(sprite['base'],(0,screenlength*0.8))
       
    #    Move Pipe
        Pipe[0][0][0]=Pipe[0][0][0]-4
        Pipe[0][1][0]=Pipe[0][1][0]-4

        if len(Pipe) != 1:
            Pipe[-1][0][0]=Pipe[-1][0][0]-4
            Pipe[-1][1][0]=Pipe[-1][1][0]-4
    
        # Blit Score in Screen
        if len(digit)>1:
            setscreen.blit(sprite['number'][digit[-1]], (5,5))
        
        # print("yes")
        if score==0:
            setscreen.blit(sprite['number'][0], (40,5))
        else:
            setscreen.blit(sprite['number'][digit[0]], (40,5))
           

       
        
        pygame.display.update()

        while flag2==True:
            digit.clear()
            flag2=False
        
        pygame.time.delay(100)


def GameOver():
    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            


# Load All image 

sprite['number'] = (pygame.image.load('Flappy Game/gallery/sprites/0.png').convert_alpha(),
                    pygame.image.load(
                        'Flappy Game/gallery/sprites/1.png').convert_alpha(),
                    pygame.image.load(
                        'Flappy Game/gallery/sprites/2.png').convert_alpha(),
                    pygame.image.load(
                        'Flappy Game/gallery/sprites/3.png').convert_alpha(),
                    pygame.image.load(
                        'Flappy Game/gallery/sprites/4.png').convert_alpha(),
                    pygame.image.load(
                        'Flappy Game/gallery/sprites/5.png').convert_alpha(),
                    pygame.image.load(
                        'Flappy Game/gallery/sprites/6.png').convert_alpha(),
                    pygame.image.load(
                        'Flappy Game/gallery/sprites/7.png').convert_alpha(),
                    pygame.image.load(
                        'Flappy Game/gallery/sprites/8.png').convert_alpha(),
                    pygame.image.load(
                        'Flappy Game/gallery/sprites/9.png').convert_alpha(),
                    )
sprite['message'] = pygame.image.load(
    'Flappy Game/gallery/sprites/message.png').convert_alpha()
sprite['base'] = pygame.image.load(
    'Flappy Game/gallery/sprites/base.png').convert_alpha()
sprite['pipe1'] = pygame.transform.rotate(pygame.image.load(
    'Flappy Game/gallery/sprites/pipe.png').convert_alpha(), 180)
sprite['pipe2'] = pygame.image.load(
    'Flappy Game/gallery/sprites/pipe.png').convert_alpha()

sprite['background'] = pygame.image.load(
    'Flappy Game/gallery/sprites/background.png').convert()
sprite['player'] = pygame.image.load(
    'Flappy Game/gallery/sprites/bird.png').convert_alpha()
sprite['gameover']=pygame.image.load(
    'Flappy Game/gallery/sprites/gameover.jpg').convert_alpha()


# Game sounds
sound['die'] = pygame.mixer.Sound('Flappy Game/gallery/audio/die.wav')
sound['hit'] = pygame.mixer.Sound('Flappy Game/gallery/audio/hit.wav')
sound['point'] = pygame.mixer.Sound('Flappy Game/gallery/audio/point.wav')
sound['swoosh'] = pygame.mixer.Sound('Flappy Game/gallery/audio/swoosh.wav')
sound['wing'] = pygame.mixer.Sound('Flappy Game/gallery/audio/wing.wav')





welcomeScreen()
MainGame()
GameOver()
