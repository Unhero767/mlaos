import pygame
class ConsensusBolt(pygame.sprite.Sprite):
    def __init__(self, pos, target):
        super().__init__()
        self.image = pygame.Surface((10, 10)); self.image.fill((0, 255, 204))
        self.rect = self.image.get_rect(center=pos)
        self.velocity = pygame.Vector2(target) - pos
        if self.velocity.length() > 0: self.velocity = self.velocity.normalize() * 10
    def update(self): self.rect.x += self.velocity.x; self.rect.y += self.velocity.y
