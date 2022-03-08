import pygame as pg

class Ball(pg.sprite.Sprite):
    def __init__(self,board,group,center_x,center_y,color) :
        super(Ball,self).__init__()
        self.board=board
        self.group=group
        self.image=pg.Surface((20,20))
        pg.draw.circle(self.image, color, (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.center=(center_x,center_y)
        self.velocity=pg.Vector2((0,0))
        self.drag=10
        self.ismoving=False
        self.direction=pg.Vector2((0,0))
        self.mass=1
    def update(self,dt):
        self.checkCollisions()
        if self.velocity.x>0:
            self.velocity.x-=self.drag*dt
            if self.velocity.x<0:
                self.velocity.x=0
        elif self.velocity.x<0:
            self.velocity.x+=self.drag*dt
            if self.velocity.x>0:
                self.velocity.x=0
        
        if self.velocity.y>0:
            self.velocity.y-=self.drag*dt
            if self.velocity.y<0:
                self.velocity.y=0
        elif self.velocity.y<0:
            self.velocity.y+=self.drag*dt
            if self.velocity.y>0:
                self.velocity.y=0

        if self.velocity.x==0 and self.velocity.y==0:
            self.ismoving=False
        else:
            self.ismoving=True

        self.rect.centerx+=self.velocity.x*dt*30
        self.rect.centery+=self.velocity.y*dt*30

    def checkCollisions(self):
        if self.rect.y<=self.board.rect.y+20:
            self.velocity.y*=-1
            self.rect.y+=5
        if self.rect.y>=self.board.rect.y+380:
            self.velocity.y*=-1
            self.rect.y-=5
        if self.rect.x<=self.board.rect.x+20:
            self.velocity.x*=-1
            self.rect.x+=5
        if self.rect.x>=self.board.rect.x+780:
            self.velocity.x*=-1
            self.rect.x-=5

        self.group.remove(self)
        result=pg.sprite.spritecollide(self,self.group,False)
        self.group.add(self)
        if len(result)>0:
            v2f=self.velocity
            v1f=result[0].velocity
            self.velocity=v1f
            result[0].velocity=v2f
        result.clear()

        dump_result=pg.sprite.spritecollide(self,self.board.dump_group,False)
        if len(dump_result)>0:
            self.group.remove(self)
            del self

        
