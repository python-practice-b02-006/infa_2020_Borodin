import pygame
from pygame.draw import *

pygame.init()

FPS = 200
screen = pygame.display.set_mode((1200, 600))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SCREEN_SIZE = (800, 600) 


def rand_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

class Ball():
     def __init__(self, coord, vel, rad=20, color=None):
        
        self.coord = coord
        self.vel = vel
        if color == None:
            color = rand_color()
        self.color = color
        self.rad = rad
        self.is_alive = True
        
        def check_corners(self, refl_ort=0.8, refl_par=0.9):
        
        for i in range(2):
            if self.coord[i] < self.rad:
                self.coord[i] = self.rad
                self.vel[i] = -int(self.vel[i] * refl_ort)
                self.vel[1-i] = int(self.vel[1-i] * refl_par)
            elif self.coord[i] > SCREEN_SIZE[i] - self.rad:
                self.coord[i] = SCREEN_SIZE[i] - self.rad
                self.vel[i] = -int(self.vel[i] * refl_ort)
                self.vel[1-i] = int(self.vel[1-i] * refl_par)
                 
        def move(self, time=1, grav=0):
        
         self.vel[1] += grav
        for i in range(2):
            self.coord[i] += time * self.vel[i]
        self.check_corners()
        if self.vel[0]**2 + self.vel[1]**2 < 2**2 and self.coord[1] > SCREEN_SIZE[1] - 2*self.rad:
            self.is_alive = False
         
        def draw(self, screen):
       
        pg.draw.circle(screen, self.color, self.coord, self.rad)
        
        

  
        
class Target():
  
    def __init__(self, coord=None, color=None, rad=30):
        
        if coord == None:
            coord = [randint(rad, SCREEN_SIZE[0] - rad), randint(rad, SCREEN_SIZE[1] - rad)]
        self.coord = coord
        self.rad = rad

        if color == None:
            color = rand_color()
        self.color = color
        
    def check_collision(self, ball):
        
        dist = sum([(self.coord[i] - ball.coord[i])**2 for i in range(2)])**0.5
        min_dist = self.rad + ball.rad
        return dist <= min_dist
    def draw(self, screen):
        
        pg.draw.circle(screen, self.color, self.coord, self.rad)



class gun():

    def __init__(self, coord=[30, SCREEN_SIZE[1]//2], angle=0, max_pow=50, min_pow=10, color=RED):
        
        self.coord = coord
        self.angle = angle
        self.max_pow = max_pow
        self.min_pow = min_pow
        self.color = color
        self.active = False
        self.pow = min_pow

class Table():
    def __init__(self, t_destr=0, b_used=0):
        self.t_destr = t_destr
        self.b_used = b_used
        self.font = pg.font.SysFont("dejavusansmono", 25)


class Manager():
    def __init__(self):
        self.gun = Gun()
        self.score_t = Table()
    def draw(self, screen):
        screen.fill(BLACK)
    
    def process(self, events, screen):
        done = self.handle_events(events)
        self.draw(screen)
        return done
    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pygame.QUIT:
                done = True 
        return done

mgr = Manager()

done = False

while not done :
    mgr.process(pygame.event.get(), screen)

    pygame.display.flip()

pygame.quit()