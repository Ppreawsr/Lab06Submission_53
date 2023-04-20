import sys 
import pygame as pg
pg.init()

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0, r=0, g=0,b=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.r = r 
        self.g = g 
        self.b = b
    def draw(self,screen):
        pg.draw.rect(screen,(self.r,self.g,self.b),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0, r=0, g=0,b=0):
        Rectangle.__init__(self, x, y, w, h,r,g,b)
    
    def isMouseOn(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        if mouse_x >= self.x and mouse_x <= self.x + self.w and mouse_y >= self.y and mouse_y <= self.y + self.h :
            return True
        else:
            return False
        #Implement your code here
        pass

win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
firstObject = Rectangle(20,20,100,100,0,0,255) # สร้าง Object จากคลาส Rectangle ขึ้นมา
btn = Button(20,20,100,100,255,0,0) # สร้าง Object จากคลาส Button ขึ้นมา

count = 0
while(True):
    screen.fill((255, 255, 255))
    firstObject.draw(screen)
    # if pg.key.get_pressed()[pg.K_w]:
    #     firstObject.y -= 1
    # if pg.key.get_pressed()[pg.K_s]:
    #     firstObject.y += 1
    # if pg.key.get_pressed()[pg.K_d]:
    #     firstObject.x += 1
    # if pg.key.get_pressed()[pg.K_a]:
    #     firstObject.x -= 1
    # if(firstObject.x < 0):
    #     firstObject.x = 0
    # if(firstObject.y < 0):
    #     firstObject.y = 0
    # if(firstObject.x+firstObject.w > win_x):
    #     firstObject.x = win_x-firstObject.w
    # if(firstObject.y+firstObject.h > win_y):
    #     firstObject.y = win_y-firstObject.h
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        if event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกกดลงและเป็นปุ่ม D
            firstObject.x -= 50
            print ("p")
        if event.type == pg.KEYUP and event.key == pg.K_w: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            firstObject.y -= 50
            print ("i")
        if event.type == pg.KEYDOWN and event.key == pg.K_s: #ปุ่มถูกกดลงและเป็นปุ่ม D
            firstObject.y += 50
            print ("j")
        if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
            firstObject.x += 50
            print ("k")
    