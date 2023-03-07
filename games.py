import pygame
import random

pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

size = 50

snake_x = random.randrange(0, WINDOW_WIDTH, 50)
snake_y = random.randrange(0, WINDOW_HEIGHT, 50)

food_x = random.randrange(0, WINDOW_WIDTH, 50)
food_y = random.randrange(0, WINDOW_HEIGHT, 50)

running = True

score = 0

lastMove = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                snake_x -= 50
                lastMove.append([snake.x, snake.y])
            elif event.key == pygame.K_RIGHT:
                snake_x += 50
                lastMove.append([snake.x, snake.y])
            elif event.key == pygame.K_UP:
                snake_y -= 50
                lastMove.append([snake.x, snake.y])
            elif event.key == pygame.K_DOWN:
                snake_y += 50
                lastMove.append([snake.x, snake.y])

    # window.fill(255,255,255)
    
    window.fill((255,255,255), rect=None, special_flags=0)   
    food = pygame.draw.rect(window, (0, 255, 0), (food_x, food_y, size, size))
    snake = pygame.draw.rect(window, (255, 0, 0), (snake_x, snake_y, size, size))
    for snakeLastPos in range(0,score):
        pygame.draw.rect(window, (255, 0, 0), (lastMove[len(lastMove) - (1+snakeLastPos)][0], lastMove[len(lastMove) - (1+snakeLastPos)][1], size, size))

    # Ajoute la collision entre la tete et food
    collide = pygame.Rect.colliderect(food, snake)
    if collide:
        score += 1
        food_x = random.randrange(0, WINDOW_WIDTH, 50)
        food_y = random.randrange(0, WINDOW_HEIGHT, 50)
        
    # Limite la taille du tableau contenant les dernères positions de la tete
    if len(lastMove) > 1000:
        lastMove.pop(0)
    pygame.display.update()

pygame.quit()
