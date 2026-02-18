import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collides_with(self, other):
        pos_1 = self.position
        pos_2 = other.position
        rad_1 = self.radius
        rad_2 = other.radius
        distance = pos_1.distance_to(pos_2)
        if distance <= (rad_1 + rad_2):
            return True
        else:
            return False
         