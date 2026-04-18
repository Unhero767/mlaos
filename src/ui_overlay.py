import pygame
class UIOverlay:
    def __init__(self):
        self.font = pygame.font.SysFont("monospace", 20)
    def draw(self, surface, tension):
        img = self.font.render(f"TENSION: {tension:.2f}", True, (255, 0, 85))
        surface.blit(img, (20, 20))
