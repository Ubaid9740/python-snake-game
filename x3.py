import pygame
import sys
from pygame.math import Vector2
import random
import os

class SNAKE:
    def __init__(self):
        self.body=[Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction=Vector2(1,0)
        self.new_block=False 

        self.a=pygame.image.load('c:\\New folder\\imge.png').convert_alpha()
        self.head_up=pygame.transform.scale(self.a,(cell_s,cell_s)).convert_alpha()
        self.b=pygame.image.load('c:\\New folder\\imgg.png')
        self.head_down=pygame.transform.scale(self.b,(cell_s,cell_s)).convert_alpha()
        self.c=pygame.image.load('c:\\New folder\\imgf.png')
        self.head_right=pygame.transform.scale(self.c,(cell_s,cell_s)).convert_alpha()
        self.d=pygame.image.load('c:\\New folder\\imgh.png')
        self.head_left=pygame.transform.scale(self.d,(cell_s,cell_s)).convert_alpha()

        self.e=pygame.image.load('c:\\New folder\\imgc.png')
        self.tail_up=pygame.transform.scale(self.e,(cell_s,cell_s)).convert_alpha()
        self.f=pygame.image.load('c:\\New folder\\imga.png')
        self.tail_down=pygame.transform.scale(self.f,(cell_s,cell_s)).convert_alpha()
        self.g=pygame.image.load('c:\\New folder\\imgd.png')
        self.tail_right=pygame.transform.scale(self.g,(cell_s,cell_s)).convert_alpha()
        self.h=pygame.image.load('c:\\New folder\\imgb.png')
        self.tail_left=pygame.transform.scale(self.h,(cell_s,cell_s)).convert_alpha()

        self.i=pygame.image.load('c:\\New folder\\imgn.png')
        self.horizontal=pygame.transform.scale(self.i,(cell_s,cell_s)).convert_alpha()
        self.j=pygame.image.load('c:\\New folder\\imgm.png')
        self.vertical=pygame.transform.scale(self.j,(cell_s,cell_s)).convert_alpha()

        self.k=pygame.image.load('c:\\New folder\\imgj.png')
        self.right_up=pygame.transform.scale(self.k,(cell_s,cell_s)).convert_alpha()
        self.l=pygame.image.load('c:\\New folder\\imgl.png')
        self.right_down=pygame.transform.scale(self.l,(cell_s,cell_s)).convert_alpha()
        self.m=pygame.image.load('c:\\New folder\\imgi.png')
        self.left_up=pygame.transform.scale(self.m,(cell_s,cell_s)).convert_alpha()
        self.n=pygame.image.load('c:\\New folder\\imgk.png')
        self.up_right=pygame.transform.scale(self.n,(cell_s,cell_s)).convert_alpha()                                                                                                

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index,block in enumerate(self.body):
         x_pos= int(block.x*cell_s)  
         y_pos= int(block.y*cell_s)
         block_rect=pygame.Rect(x_pos,y_pos,cell_s,cell_s)
         if index == 0:
             screen.blit(self.head,block_rect)
         elif index==len(self.body)-1:
             screen.blit(self.tail,block_rect)    
         else: 
            previouse_block=self.body[index+1]-block
            next_block=self.body[index-1]-block
            if previouse_block.x==next_block.x:
                screen.blit(self.vertical,block_rect)
            elif previouse_block.y==next_block.y:
                screen.blit(self.horizontal,block_rect)        
            else:
                if previouse_block.x==-1 and next_block.y==-1 or previouse_block.y==-1 and next_block.x==-1:
                    screen.blit(self.right_up,block_rect)
                if previouse_block.x==1 and next_block.y==1 or previouse_block.y==1 and next_block.x==1:
                    screen.blit(self.up_right,block_rect)
                if previouse_block.x==-1 and next_block.y==1 or previouse_block.y==1 and next_block.x==-1:
                    screen.blit(self.right_down,block_rect)
                if previouse_block.x==1 and next_block.y==-1 or previouse_block.y==-1 and next_block.x==1:
                    screen.blit(self.left_up,block_rect)                                                            

    def update_head_graphics(self):
        head_relations=self.body[1]-self.body[0]
        if head_relations==(-1,0):self.head=self.head_right
        elif head_relations==(1,0):self.head=self.head_left    
        elif head_relations==(0,-1):self.head=self.head_down
        elif head_relations==(0,1):self.head=self.head_up
    def update_tail_graphics(self):
        tail_relations=self.body[-1]-self.body[-2]
        if tail_relations==(1,0):self.tail=self.tail_right
        elif tail_relations==(-1,0):self.tail=self.tail_left    
        elif tail_relations==(0,1):self.tail=self.tail_down
        elif tail_relations==(0,-1):self.tail=self.tail_up         
    def move_snake(self):
        if self.new_block==True:
            body_copy=self.body[:]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body=body_copy[:] 
            self.new_block=False
        else:
            body_copy=self.body[0:-1]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body=body_copy[:]
    def add_block(self):
        self.new_block=True    

class FRUIT:
    def __init__(self):
        self.randomize()
    def draw_fruit(self):
        fruit_rect=pygame.Rect(int(self.pos.x*cell_s),int(self.pos.y*cell_s),cell_s,cell_s)
        screen.blit(apple,fruit_rect)
        # pygame.draw.rect(screen,(126,166,114),fruit_rect)    
    def randomize(self):
        self.x=random.randint(0,cell_n-1)
        self.y=random.randint(0,cell_n-1)
        self.pos=pygame.math.Vector2(self.x,self.y)        


class MAIN:
    def __init__(self):
        self.snake= SNAKE()
        self.fruit=FRUIT()
    def update(self):
        self.snake.move_snake() 
        self.check_collision() 
        self.check_fail()  
    def draw_element(self):
        self.draw_grass()
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        self.draw_score()      
    def check_collision(self):
        if self.fruit.pos==self.snake.body[0]:
           self.fruit.randomize()
           self.snake.add_block()
    def check_fail(self):
        if not 0<=self.snake.body[0].x<=cell_n or not 0<=self.snake.body[0].y<=cell_n:
            self.game_over()
            # print("x")
        for block in self.snake.body[1:]:
            if block==self.snake.body[0]:
                # self.game_over() 
                print("y")   
    def game_over(self):
            pygame.quit()
            sys.exit()
    def draw_grass(self):
        grass_color=(167,209,61)
        for row in range(cell_n):
            if row%2==0:
              for col in range(cell_n):
                 if col%2==0:  
                  grass_rect=pygame.Rect(col*cell_s,row*cell_s,cell_s,cell_s)
                  pygame.draw.rect(screen,grass_color,grass_rect)        
    def draw_score(self):
        score_text=str(len(self.snake.body)-3)
        score_surface=game_font.render(score_text,True,(56,74,12))
        score_x=int(cell_s*cell_n-60)
        score_y=int(cell_s*cell_n-40)
        score_rect=score_surface.get_rect(center=(score_x,score_y))
        apple_rect=apple.get_rect(midright=(score_rect.left,score_rect.centery))        
        bg_rect=pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width+score_rect.width,apple_rect.height)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)
        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_rect)

pygame.init()
cell_s=35
cell_n=20
screen=pygame.display.set_mode((cell_n*cell_s,cell_n*cell_s))
clock=pygame.time.Clock()
snake=SNAKE()
fruit=FRUIT()
main=MAIN()
SCREEN_UPDATE=pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,1000)
im=pygame.image.load('c:\\New folder\\download-removebg-preview.png')
apple=pygame.transform.scale(im,(cell_s,cell_s)).convert_alpha()
# font_path = os.path.abspath(r'c:\\New folder\\Kanit\\Kanit-Bold.ttf')
game_font=pygame.font.Font(r'C:\\New folder\\KGRedHands.ttf',25)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main.game_over()
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
              if main.snake.direction.y !=1:
                main.snake.direction = Vector2(0,-1)  
            if event.key == pygame.K_DOWN:
              if main.snake.direction.y !=-1:  
                main.snake.direction = Vector2(0,1)        
            if event.key == pygame.K_RIGHT:
              if main.snake.direction.x !=-1: 
                main.snake.direction = Vector2(1,0)  
            if event.key == pygame.K_LEFT:
              if main.snake.direction.x !=1:  
                 main.snake.direction = Vector2(-1,0)  

    screen.fill((180,210,70))
    main.draw_element()
    main.update()
    pygame.display.update()        
    clock.tick(3)
