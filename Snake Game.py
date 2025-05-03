import pygame
import time
import random
import os

# Initialize pygame
pygame.init()

# Window settings
width = 600
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
yellow = (255, 255, 102)

# Snake settings
block_size = 20
base_speed = 10
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 30)

# High score file
score_file = "highscore.txt"


def get_high_score():
    if not os.path.exists(score_file):
        with open(score_file, "w") as f:
            f.write("0")
    with open(score_file, "r") as f:
        return int(f.read())


def update_high_score(score):
    high = get_high_score()
    if score > high:
        with open(score_file, "w") as f:
            f.write(str(score))


def draw_score(score, level, high_score):
    value = score_font.render(f"Score: {score}  Level: {level}  High: {high_score}", True, yellow)
    window.blit(value, [10, 10])


def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(window, green, [block[0], block[1], block_size, block_size])


def game_loop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2
    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1
    score = 0

    food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    high_score = get_high_score()
    level = 1
    snake_speed = base_speed

    while not game_over:

        while game_close:
            window.fill(blue)
            msg = font.render("You lost! Press C-Play Again or Q-Quit", True, red)
            window.blit(msg, [width / 6, height / 3])
            draw_score(score, level, high_score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = block_size
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        window.fill(black)
        pygame.draw.rect(window, red, [food_x, food_y, block_size, block_size])

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check collision with self
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_list)
        draw_score(score, level, high_score)
        pygame.display.update()

        # Snake eats food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            snake_length += 1
            score += 1

            # Level up every 5 points
            if score % 5 == 0:
                level += 1
                snake_speed += 2

        clock.tick(snake_speed)

    update_high_score(score)
    pygame.quit()
    quit()


# Start the game
game_loop()
