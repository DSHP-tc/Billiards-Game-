import imp


import pygame as pg

class Board():
    def __init__(self,parent,x,y,width,height):
        self.parent=parent
        self.x=x
        self.y=y
        self.width=width
        self.height=height

        self.rect=pg.Rect(self.x,self.y,self.width,self.height)
        self.dumps=[Dumps(self.x,self.y),Dumps(self.x+self.width//2,self.y),Dumps(self.x+self.width,self.y)
        ,Dumps(self.x,self.y+self.height),Dumps(self.x+self.width//2,self.y+self.height),Dumps(self.x+self.width,self.y+self.height)]

        self.dump_group=pg.sprite.Group()
        for i in range(0,6):
            self.dump_group.add(self.dumps[i])
    def draw(self):
        pg.draw.rect(self.parent,(255,255,255),self.rect,5)
        for dump in self.dumps:
            self.parent.blit(dump.image,dump.rect)


class Dumps(pg.sprite.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__()
        self.image=pg.Surface((50,50))
        pg.draw.circle(self.image, (255,255,255), (25, 25), 25)
        self.rect = self.image.get_rect()
        self.rect.center=(center_x,center_y)