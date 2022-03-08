import random
import sys
import time

import pygame as pg
from board import Board
from ball import Ball
from stick2 import Stick
import math
pg.init()

class Game():
    def __init__(self):
        self.win=pg.display.set_mode((1000,800))
        self.ball_group=pg.sprite.Group()
        self.move_list=[]
        self.board=Board(self.win,100,200,800,400)
        
        self.ball=Ball(self.board,self.ball_group,300,400,(255,0,0))
        self.ball_group.add(self.ball)
        
        self.createBalls(3)
        temp_pos=pg.mouse.get_pos()
        self.stick=Stick()
        self.stick.initLoc(self.ball.rect.centerx,self.ball.rect.centery, 100)
        self.all_sprites = pg.sprite.Group(self.stick)
     
        self.startGame()

    def createBalls(self,num):
        space_width=30
        space_height=30
        spaces=num-1
        initialx=400
        initialy=395
        for i in range(0,num):
            for j in range(0,spaces):
                initialx+=space_width
                print(initialx)
            for k in range(0,i+1):
                temp=Ball(self.board,self.ball_group,initialx,initialy,(0,255,0))
                self.ball_group.add(temp)
                initialx+=space_width
            initialy+=space_height
            spaces-=1
            initialx=400
        
        for i in range(1,num):
            initialx+=space_width*i
            for j in range(num-i,0,-1):
                temp=Ball(self.board,self.ball_group,initialx,initialy,(0,255,0))
                self.ball_group.add(temp)
                initialx+=space_width
                print("created")
            initialy+=space_height
            initialx=400

            

            
            



    def startGame(self):
        run=True
        clock=pg.time.Clock()
        last_time=time.time()
        dt=0
     
        while run:
            new_time=time.time()
            dt=new_time-last_time
            last_time=new_time

            self.move_list.clear()
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    pg.quit()
                    sys.exit()


            for ball in self.ball_group:
                self.move_list.append(ball.ismoving)
            
            if any(self.move_list)==False and self.stick.isdistrubed==True:
                self.stick.resetStick(self.ball.rect.centerx,self.ball.rect.centery,100)
                self.stick.isdistrubed=False
            
            key_pressed=pg.key.get_pressed()
            if key_pressed[pg.K_LCTRL]:
             
                self.stick.is_shooting=True
                
                if key_pressed[pg.K_UP]:
                    self.stick.applyPower(True,dt)
                    
                elif key_pressed[pg.K_DOWN]:
                    self.stick.applyPower(False,dt)
            elif key_pressed[pg.K_LCTRL]==False and self.stick.is_shooting:
                self.stick.is_shooting=False
                self.stick.isdistrubed=True
                temp=self.stick.getMomentum()
                self.ball.velocity=temp[0]
                self.ball.direction=temp[1]
                self.ball.velocity.x*=self.ball.direction.x
                self.ball.velocity.y*=self.ball.direction.y
                self.ball.ismoving=True
            

            
            self.win.fill((0,0,0))
            self.board.draw()
          
            self.ball_group.update(dt)
            self.ball_group.draw(self.win)
           
            self.stick.update()
            self.all_sprites.draw(self.win)   
            pg.display.update()
            clock.tick(60)

game=Game()