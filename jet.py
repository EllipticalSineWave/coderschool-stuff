import pygame
from random import randint
import math

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))
running = True

class Jet:
    def __init__(self):
        self.x = 300
        self.y = 300

class Bullet:
    def __init__(self, target_x, target_y):
        self.x = randint(0, 600)
        self.y = 600
        self.speed = 5

        # Calculate direction towards the plane
        delta_x = target_x - self.x
        delta_y = target_y - self.y
        distance = math.hypot(delta_x, delta_y)
        self.dx = delta_x / distance * self.speed
        self.dy = delta_y / distance * self.speed

    def move(self):
        self.x += self.dx
        self.y += self.dy

class Missile:
    def __init__(self, target_x, target_y):
        self.x = randint(0, 600)
        self.y = 600

        # Calculate direction towards the plane
        delta_x = target_x - self.x
        delta_y = target_y - self.y
        distance = math.hypot(delta_x, delta_y)
        self.dx = delta_x / distance
        self.dy = delta_y / distance

    def move(self):
        self.x += self.dx * 10
        self.y += self.dy * 10
        # Calculate direction towards the plane
        delta_x = player.x - self.x + randint(-20,20)
        delta_y = player.y - self.y + randint(-20,20)
        distance = math.hypot(delta_x, delta_y)
        self.dx = delta_x / distance
        self.dy = delta_y / distance

player = Jet()
bullets = []
missiles = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]: player.y -= 2
    if keys[pygame.K_s]: player.y += 2
    if keys[pygame.K_a]: player.x -= 3
    if keys[pygame.K_d]: player.x += 3

    # Spawn a new bullet every 30 frames (half a second at 60 FPS)
    if pygame.time.get_ticks() % 30 == 0:
        bullets.append(Bullet(player.x, player.y))
        missiles.append(Missile(player.x, player.y))

    screen.fill((135, 206, 235))
    plane = pygame.draw.rect(screen, (150, 150, 150), (player.x, player.y, 20, 30))

    for bullet in bullets[:]:
        bullet.move()
        pygame.draw.circle(screen, (255, 0, 0), (int(bullet.x), int(bullet.y)), 5)
        if bullet.x < 0 or bullet.x > 600 or bullet.y < 0 or bullet.y > 600:
            bullets.remove(bullet)

    for missile in missiles[:]:
        missile.move()
        # Draw the missile pointing towards the plane
        missile_angle = math.atan2(missile.dy, missile.dx)
        missile_rect = pygame.Rect(missile.x, missile.y, 20, 10)
        rotated_missile = pygame.transform.rotate(pygame.Surface((20, 10)), -math.degrees(missile_angle))
        screen.blit(rotated_missile, missile_rect.topleft)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
