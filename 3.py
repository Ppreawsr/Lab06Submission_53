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
        
COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

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

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
        
input_box1 = InputBox(200, 100, 140, 32) # สร้าง InputBox1
input_box2 = InputBox(200, 150, 140, 32) # สร้าง InputBox2
input_box3 = InputBox(200, 200, 140, 32) #
input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True

win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

# font = pg.font.Font('freesansbold.ttf', 100) # font and fontsize
# text = font.render('FRA 142', True, (255,255,255), (20,20,100)) # (text,is smooth?,letter color,background color)
# textRect = text.get_rect() # text size
# textRect.center = (win_x // 2, win_y // 2)

font = pg.font.Font(None, 32) # font and fontsize
text = font.render('First name', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRect = text.get_rect() # text size
textRect.center = (100,115)

text1 = font.render('Last name', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRect1 = text1.get_rect() # text size
textRect1.center = (100,165)

text2 = font.render('Age', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRect2 = text2.get_rect() # text size
textRect2.center = (100,215)

text3 = font.render('', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRect3 = text3.get_rect() # text size
textRect3.center = (550,265)

btn = Button(150,315,250,50,255,0,0)
        
while(1):
    screen.fill((255, 255, 255))
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    if btn.isMouseOn():
        if pg.mouse.get_pressed()[0]==1:
            if(input_box3.text.isnumeric()):
                txt = "Hello " + input_box1.text + " " + input_box2.text + "! You are " + input_box3.text + " years old."
                text3 = font.render(txt, True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
                textRect3 = text3.get_rect() # text size
                textRect3.center = (550,265)
            else:
                txt = " "
                text3 = font.render(txt, True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
                textRect3 = text3.get_rect() # text size
                textRect3.center = (550,265)                
        else:
            count = 0
            btn.r = 192
            btn.g = 192
            btn.b = 192
    else:

        btn.b = 0
        btn.g = 0
    btn.draw(screen)
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()