import pygame

class CollisionSystem:
    def validate_movement(self, rect, dx, dy, walls):
        # Predict X
        temp_rect = rect.move(dx, 0)
        for wall in walls:
            if wall.stability >= 0.8:
                wall_rect = pygame.Rect(min(wall.start[0], wall.end[0]), min(wall.start[1], wall.end[1]), 
                                       abs(wall.end[0]-wall.start[0])+5, abs(wall.end[1]-wall.start[1])+5)
                if temp_rect.colliderect(wall_rect): dx = 0
        
        # Predict Y
        temp_rect = rect.move(0, dy)
        for wall in walls:
            if wall.stability >= 0.8:
                wall_rect = pygame.Rect(min(wall.start[0], wall.end[0]), min(wall.start[1], wall.end[1]), 
                                       abs(wall.end[0]-wall.start[0])+5, abs(wall.end[1]-wall.start[1])+5)
                if temp_rect.colliderect(wall_rect): dy = 0
        return dx, dy
