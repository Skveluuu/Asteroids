import pygame
import random
from constants import *
from circleshape import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.x = x
        self.y =y
        self.radius = radius
    

    def draw(self,screen):
        pygame.draw.circle(screen,(255, 255, 255),(self.position),self.radius,2)
    def update(self,dt):
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        self.split_angle = random.uniform(20,50)
        self.split_vector_pos = self.velocity.rotate(self.split_angle)
        self.split_vector_neg = self.velocity.rotate(-self.split_angle)
        self.split_radius = self.radius-ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x,self.position.y,self.split_radius)
        new_asteroid1.velocity = self.split_vector_pos *1.2
        new_asteroid2 = Asteroid(self.position.x,self.position.y,self.split_radius)
        new_asteroid2.velocity = self.split_vector_neg *1.2
    



    

    