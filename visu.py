import pygame
import json

# Load the labyrinth JSON data
with open('labyrinth.json') as f:
    labyrinth_data = json.load(f)

# Set up the display
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Calculate tile size based on window dimensions and labyrinth size
labyrinth_width = len(labyrinth_data['map'][0])
labyrinth_height = len(labyrinth_data['map'])
tile_size = min(WINDOW_WIDTH // labyrinth_width, WINDOW_HEIGHT // labyrinth_height)

# Calculate adjusted window size based on the scaled labyrinth
adjusted_width = labyrinth_width * tile_size
adjusted_height = labyrinth_height * tile_size

pygame.init()
screen = pygame.display.set_mode((adjusted_width, adjusted_height))
clock = pygame.time.Clock()

# Define colors for different tile types
WALL_COLOR = (0, 0, 0)
EMPTY_COLOR = (255, 255, 255)
START_COLOR = (0, 255, 0)
END_COLOR = (255, 0, 0)

# Draw the labyrinth
def draw_labyrinth():
    for y, row in enumerate(labyrinth_data['map']):
        for x, tile in enumerate(row):
            tile_rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
            if tile == '1':
                pygame.draw.rect(screen, WALL_COLOR, tile_rect)
            elif tile == '0':
                pygame.draw.rect(screen, EMPTY_COLOR, tile_rect)
            elif tile == '2':
                pygame.draw.rect(screen, START_COLOR, tile_rect)
            elif tile == '3':
                pygame.draw.rect(screen, END_COLOR, tile_rect)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    draw_labyrinth()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
