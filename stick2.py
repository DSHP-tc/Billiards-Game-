from re import X
import pygame as pg
import math
class Stick(pg.sprite.Sprite):
    def __init__(self):
        super(Stick,self).__init__()
        self.original_img=pg.image.load(r"stick.png").convert_alpha()
        self.image=self.original_img
        self.rect=self.image.get_rect()
        self.power=0
        self.angle = 0
        self.max_power=25
        self.min_power=0
        self.power_countdown=0
        self.is_shooting=False
        self.isdistrubed=False
        self.momentum=pg.Vector2((0,0))
        self.direction=pg.Vector2((0,0))

    def initLoc(self, x,y, radius):
        self.pos = (x,y)
        self.radius = radius
    def update(self):
        key_pressed=pg.key.get_pressed()
        if key_pressed[pg.K_KP_8]:
            self.turnLeft()
        elif key_pressed[pg.K_KP_2]:
            self.turnRight()
        
    
        center = pg.math.Vector2(self.pos) + pg.math.Vector2(0, -self.radius).rotate(-self.angle) 
        self.image = pg.transform.rotate(self.original_img, self.angle)
        self.rect = self.image.get_rect(center = (round(center.x), round(center.y)))            

    def turnLeft(self):
        self.angle = (self.angle + 1) % 360

    def turnRight(self):
        self.angle = (self.angle - 1) % 360
    
    def applyPower(self,factor,dt):
        cooldown=1
        if factor==True and self.power_countdown==cooldown:
            self.power_countdown=0
            if self.power>self.max_power:
                self.power=self.max_power
            else:
                self.power+=1
            if self.power<self.max_power:
                self.radius+=150*dt
        elif factor==False and self.power_countdown==cooldown:
            self.power_countdown=0
            if self.power<self.min_power:
                self.power=self.min_power
            else:
                self.power-=1
            if self.power>self.min_power:
                self.radius-=150*dt
        else:
            self.power_countdown+=1

    def calculateDistance(self):   
        if self.angle>=0 and self.angle<=90:
            x=math.sin(math.radians(self.angle))
            y=math.cos(math.radians(self.angle))
            self.direction.x=1
            self.direction.y=1
        elif self.angle>=90 and self.angle<=180:
            temp_angle=self.angle-90
            x=math.cos(math.radians(temp_angle))
            y=math.sin(math.radians(temp_angle))
            self.direction.x=1
            self.direction.y=-1
        elif self.angle>=180 and self.angle<=270:
            temp_angle=self.angle-180
            x=math.sin(math.radians(self.angle))
            y=math.cos(math.radians(self.angle))
            self.direction.x=-1
            self.direction.y=-1
        elif self.angle>=270 and self.angle<=360:
            temp_angle=self.angle-270
            x=math.cos(math.radians(temp_angle))
            y=math.sin(math.radians(temp_angle))
            self.direction.x=-1
            self.direction.y=1

   
        return (x,y)

    def getMomentum(self):
        pos=self.calculateDistance()
        self.momentum.x=abs(pos[0]*self.power)
        self.momentum.y=abs(pos[1]*self.power)
        
        return (self.momentum,self.direction)

    def resetStick(self,x,y,radius):
        self.pos=(x,y)
        self.radius=radius
        self.power_countdown=0
        self.power=0
        self.angle = 0
        self.is_shooting=False
        self.momentum=pg.Vector2((0,0))
        self.direction=pg.Vector2((0,0))
        
        