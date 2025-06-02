import pygame

pygame.init()
display_surface = pygame.display.set_mode((500, 1000))

fonts = pygame.font.get_fonts()
print(fonts)
text = []
textRect = []
x = 50
y = 50
for e in fonts:
    font = pygame.font.SysFont(e, 32)
    t = font.render(e, False, (0,0,0))
    text.append(t)
    tr = t.get_rect()
    tr.center = (x,y)
    textRect.append(tr)
    y += 50
    if y > 1000:
        y = 50
        x += 100

while True:
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:

            # deactivates the pygame library
            pygame.quit()

            # quit the program.
            quit()

        # Draws the surface object to the screen.
        display_surface.fill(white)
        for i in range(len(text)):
            display_surface.blit(text[i], textRect[i])
        pygame.display.update()