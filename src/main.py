import pygame
import webbrowser

rickrolled = False
pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("ElonMuskRickrolled")
background = pygame.image.load("moon.png") # replace with your image
gameover = pygame.image.load("game-over-duh.png") # replace with your image

# make this thing move idk
x = 0
# in mainloop we would add this var
# to background size

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x = 0
    
    x += 1

    if x >= 800:
        screen.blit(gameover, (0, 0))
        pygame.display.update()
        if rickrolled == False:
            webbrowser.open("https://www.youtube.com/watch?v=3BFTio5296w")
            rickrolled = True
    else:
        x += 1
        screen.blit(background, (x, 0))
        pygame.display.update()

