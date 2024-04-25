import pygame

# Initialize the game engine
pygame.init()

# ---------------------------
# Set window settings (size and name) 
WIDTH = 700
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Bouncing Rectangle")
# ---------------------------

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

# Rectangle
## Location
rect_x = 50
rect_y = 50

## Speed
rect_speed_x = 3
rect_speed_y = 3


# ---------------------------
# Colours
cherry = (255, 204, 204)
white = (255, 255, 255)

# ---------------------------

# ---------------------------
# Functions
screen.fill(white)  # always the first drawing command

# ---------------------------

# --------------- Main program loop ---------------
running = True
while running:
    # ----- EVENT HANDLING -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ----- GAME STATE UPDATES -----
    # All game math and comparisons happen here
     # Update rectangle location 
    rect_x += rect_speed_x
    rect_y += rect_speed_y

     # Change rectangle y direction when colliding with edge
    if rect_y > (HEIGHT - 50) or rect_y < 0:
       rect_speed_y *= -1
    
    # Change rectangle x direction when colliding with edge
    if rect_x > (WIDTH - 50) or rect_x < 0:
        rect_speed_x *= -1

    # ----- DRAWING -----
    
    # Rectangle 
    pygame.draw.rect(screen, cherry, [rect_x, rect_y, 50, 50])

    # Must be the last two lines of the game loop
    pygame.display.flip()
    clock.tick(30)
    # ---------------------------

pygame.quit()
