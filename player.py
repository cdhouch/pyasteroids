from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        #print(f"DEBUG a: {a}, b: {b}, c: {c}")
        return [a, b, c]

    def draw(self, screen):
        #color = pygame.Color("white")
        #points = [(v.x, v.y) for v in self.triangle()]  # Convert Vector2 to tuples
        #points = [(self.triangle()[0].x, self.triangle()[0].y),
        #          (self.triangle()[1].x, self.triangle()[1].y),
        #          (self.triangle()[2].x, self.triangle()[2].y)]
        # pygame.draw.polygon(screen, color, points, width=2)
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt