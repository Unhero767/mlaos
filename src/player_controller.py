import pygame
import math

class PlayerController:
    def __init__(self, speed=5.0):
        self.base_speed = speed
        self.angle = 0.0

    def process_input(self, rect):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_w]: dy -= self.base_speed
        if keys[pygame.K_s]: dy += self.base_speed
        if keys[pygame.K_a]: dx -= self.base_speed
        if keys[pygame.K_d]: dx += self.base_speed
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - rect.centerx, mouse_y - rect.centery
        self.angle = -math.degrees(math.atan2(rel_y, rel_x))
        return dx, dy, self.angle
