import pygame

class AdaptiveChiaroscuroRenderer:
    def __init__(self, w, h):
        self.screen = pygame.display.set_mode((w, h))

    def render_manifold_state(self, surface, geometry):
        surface.fill((5, 8, 15)) # Void
        for wall in geometry.walls:
            color = (77, 144, 254) if wall.stability > 0.5 else (255, 0, 85)
            pygame.draw.line(surface, color, wall.start, wall.end, 3)
