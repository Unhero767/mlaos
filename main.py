# main.py
import pygame
import sys
from src.level_geometry import spine_hub
from src.player_controller import PlayerController
from src.collision_system import CollisionSystem
from src.map_renderer import AdaptiveChiaroscuroRenderer
from src.light_engine import LightEngine
from src.combat_rituals import ConsensusBolt
from src.glitch_entity_spawner import GlitchSpawner
from src.ui_overlay import UIOverlay

class NeonShadowsEngine:
    def __init__(self):
        pygame.init()
        self.screen_res = (1280, 720)
        self.screen = pygame.display.set_mode(self.screen_res)
        pygame.display.set_caption("Neon Shadows: Phase 11 Load Test")
        
        # 1. Initialize Systems
        self.renderer = AdaptiveChiaroscuroRenderer(1280, 720)
        self.physics = CollisionSystem()
        self.controller = PlayerController(speed=5.0)
        self.light_engine = LightEngine(self.screen_res)
        self.spawner = GlitchSpawner(spawn_limit=5)
        self.ui = UIOverlay()
        
        # 2. Initialize Entities & Map
        self.map = spine_hub
        self.map.tension_index = 1.0
        
        # The Architect's Body
        self.observer_image = pygame.Surface((24, 24), pygame.SRCALPHA)
        pygame.draw.rect(self.observer_image, (200, 200, 255), [0, 0, 24, 24], 2)
        self.observer_rect = self.observer_image.get_rect(center=(200, 150))
        self.observer_angle = 0.0
        
        self.bolts = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        """The primary pulse of the Neon Veil."""
        while self.running:
            # --- Phase 1: Input & Agency ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    bolt = ConsensusBolt(self.observer_rect.center, pygame.mouse.get_pos())
                    self.bolts.add(bolt)

            dx, dy, angle = self.controller.process_input(self.observer_rect)
            self.observer_angle = angle

            # --- Phase 2: Physics & Stability ---
            safe_dx, safe_dy = self.physics.validate_movement(self.observer_rect, dx, dy, self.map.walls)
            self.observer_rect.move_ip(safe_dx, safe_dy)

            # --- Phase 3: Tension & Spawning ---
            # Update Tension based on proximity to the Sub-Level 0 Breach (X=500, Y=200-400)
            dist_to_breach = abs(self.observer_rect.x - 500)
            self.map.tension_index = max(1.0, 7.0 - (dist_to_breach / 100))
            
            self.spawner.monitor_breach(pygame.Vector2(self.observer_rect.center), self.map.walls)
            self.bolts.update()

            # --- Phase 4: Optical Rendering (Chiaroscuro) ---
            # Draw base geometry and entities
            temp_surface = pygame.Surface(self.screen_res)
            self.renderer.render_manifold_state(temp_surface, self.map)
            
            # Draw Observer
            rotated_obs = pygame.transform.rotate(self.observer_image, self.observer_angle)
            temp_surface.blit(rotated_obs, rotated_obs.get_rect(center=self.observer_rect.center))
            
            # Draw Rituals
            self.bolts.draw(temp_surface)
            
            # Apply Light Engine (Shadow Casting)
            light_rad = 500 * (1.1 - (self.map.tension_index / 10))
            vis_points = self.light_engine.calculate_visibility(self.observer_rect.center, self.map.walls, light_rad)
            self.light_engine.draw_shadows(temp_surface, vis_points)
            
            # Final Blit to Screen
            self.screen.blit(temp_surface, (0, 0))
            self.ui.draw(self.screen, self.map.tension_index)
            
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    engine = NeonShadowsEngine()
    engine.run()