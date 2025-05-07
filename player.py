from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shotcooldown = PLAYER_SHOOT_COOLDOWN

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
        print(f"Cooldown {self.shotcooldown}")
        self.shotcooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        #print("Shooting!")
        if self.shotcooldown > 0:
            return
        self.shotcooldown = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED