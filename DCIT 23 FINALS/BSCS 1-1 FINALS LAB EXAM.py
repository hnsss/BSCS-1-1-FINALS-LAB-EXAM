import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Window size
width = 360
height = 640

# Create the window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Dodging Game")

clock = pygame.time.Clock()

# Load images
background_image = pygame.image.load("background.png")
car_image = pygame.transform.scale(pygame.image.load("car.png").convert_alpha(), (45, 90))
other_car_images = [
    pygame.transform.scale(pygame.image.load("car1.png").convert_alpha(), (45, 90)),
    pygame.transform.scale(pygame.image.load("car2.png").convert_alpha(), (45, 90)),
    pygame.transform.scale(pygame.image.load("car3.png").convert_alpha(), (45, 90)),
    pygame.transform.scale(pygame.image.load("car4.png").convert_alpha(), (45, 90))
]
restart_button = pygame.font.Font(None, 40).render("Restart", True, (255, 255, 255))

# Car properties
car_width = 45
car_height = 90

# Colors
white = (255, 255, 255)

# Display the menu screen
def menu_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                #start
                if 100 <= mouse_pos[0] <= 450:
                    return

        window.blit(background_image, (0, 0))

        start_rect = pygame.draw.rect(window, (0, 255, 0), (150, 300, 100, 40))

        # Display button texts
        start_font = pygame.font.Font(None, 40)
        start_text = start_font.render("Start", True, white)
        window.blit(start_text, (170,305))

        pygame.display.update()

# Display the car on the screen
def car(x, y):
    window.blit(car_image, (x, y))

# Display the score
def display_score(score):
    font = pygame.font.Font(None, 30)
    text = font.render("Score: " + str(score), True, white)
    window.blit(text, (10, 10))

# Main game loop
def game_loop():
    x = (width - car_width) // 2
    y = height - car_height

    car_speed = 5
    other_car_width = 45
    other_car_height = 90
    other_car_x = random.randint(0, width - other_car_width)
    other_car_y = -other_car_height
    other_car_speed = 7

    score = 0
    game_over = False

    car_image_index = 0  # Counter variable to track the car image index
    score_increment = 10  # Score increment threshold

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 0:
            x -= car_speed
        if keys[pygame.K_RIGHT] and x < width - car_width:
            x += car_speed

        window.blit(background_image, (0, 0))

        other_car_y += other_car_speed
        car(x, y)

        if other_car_y > height:
            other_car_y = -other_car_height
            other_car_x = random.randint(0, width - other_car_width)
            score += 1
            car_image_index = (car_image_index + 1) % len(other_car_images)  # Increment the counter and wrap around

            # Check if the score is a multiple of 10 and increase the other car speed
            if score % score_increment == 0:
                other_car_speed += 1

        car_image = other_car_images[car_image_index]
        window.blit(car_image, (other_car_x, other_car_y))

        display_score(score)

        if y < other_car_y + other_car_height and y + car_height > other_car_y:
            if x < other_car_x + other_car_width and x + car_width > other_car_x:
                game_over = True

        pygame.display.update()
        clock.tick(60)

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 150 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 290:
                    game_loop()

        window.blit(background_image, (0, 0))
        restart_button_rect = display_restart_button()
        pygame.display.update()

def display_restart_button():
    restart_button_rect = window.blit(restart_button, (130, 250))
    return restart_button_rect

# Run the game
menu_screen()
game_loop()
