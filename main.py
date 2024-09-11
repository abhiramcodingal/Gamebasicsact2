import pygame

pygame.init()
screen = pygame.display.set_mode((300,400))
screen.fill((255,255,255))

done = False
red = (255,0,0)
blue = (0,0,255)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.circle(screen, red, (100,100) ,50, 5)
    pygame.draw.circle(screen, red, (200,300) ,50)
    pygame.display.flip()

pygame.quit()