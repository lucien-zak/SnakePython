import pygame
import random

pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

size = 50

snake_x = random.randrange(0, WINDOW_WIDTH, 10)
snake_y = random.randrange(0, WINDOW_HEIGHT, 10)

food_x = random.randrange(0, WINDOW_WIDTH, 10)
food_y = random.randrange(0, WINDOW_HEIGHT, 10)

running = True

score = 0

tick = 0

lastMove = []
direction = 'LEFT'

while running:

    if direction == 'LEFT':
        snake_x -= 5
    elif direction == 'RIGHT':
        snake_x += 5
    elif direction == 'UP':
        snake_y -= 5
    elif direction == 'DOWN':
        snake_y += 5

    if snake_x > WINDOW_WIDTH:
        snake_x = 0
    elif snake_x < 0:
        snake_x = WINDOW_WIDTH

    if snake_y > WINDOW_HEIGHT:
        snake_y = 0
    elif snake_y < 0:
        snake_y = WINDOW_HEIGHT


    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                # snake_x -= 50
                direction = 'LEFT'
                print(lastMove)
            elif event.key == pygame.K_RIGHT:
                # snake_x += 50
                direction = 'RIGHT'
            elif event.key == pygame.K_UP:
                # snake_y -= 50
                direction = 'UP'
            elif event.key == pygame.K_DOWN:
                direction = 'DOWN'
                # snake_y += 50

    # window.fill(255,255,255)
    window.fill((255,255,255), rect=None, special_flags=0)   
    food = pygame.draw.rect(window, (0, 255, 0), (food_x, food_y, size, size))
    snake = pygame.draw.rect(window, (255, 0, 0), (snake_x, snake_y, size, size))
    lastMove.append([snake.x, snake.y])
    decal = 5
    for snakeLastPos in range(0,score):
        pygame.draw.rect(window, (255, 0, 0), ((lastMove[len(lastMove) - (decal - 1)][0]), (lastMove[len(lastMove) - (decal - 1)][1]), size, size))
        decal = decal + 5
    # Ajoute la collision entre la tete et food
    collideWithFood = pygame.Rect.colliderect(food, snake)
    if collideWithFood:
        score += 1
        food_x = random.randrange(0, WINDOW_WIDTH, 50)
        food_y = random.randrange(0, WINDOW_HEIGHT, 50)
    
    # Limite la taille du tableau contenant les dernères positions de la tete
    if len(lastMove) > 1000:
        lastMove.pop(0)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
