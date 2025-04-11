#canva erase
#the work of step 02 list 


import pygame

pygame.init()

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

blue = (0, 0, 225)
pink = (225, 182, 193)
white = (255, 255, 255)

screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
pygame.display.set_caption("Enter effect in Pygame")

clock = pygame.time.Clock()  

grid = []
for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        rect = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)
        grid.append(rect)

eraser = pygame.Rect(200, 200, ERASER_SIZE, ERASER_SIZE)

running = True
while running:
    clock.tick(60)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    for rect in grid:
        pygame.draw.rect(screen, blue, rect)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser.topleft = (mouse_x, mouse_y)

    # Remove collided rectangles
    new_grid = []
    for rect in grid:
        if not eraser.colliderect(rect):
            new_grid.append(rect)
    grid = new_grid

    pygame.draw.rect(screen, pink, eraser)

    pygame.display.flip()

pygame.quit()
