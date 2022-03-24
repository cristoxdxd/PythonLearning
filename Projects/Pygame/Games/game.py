import pygame
from Characters.Characters import Ghost, Monster
from Characters.Position import Position

ScreenResolution =  (600,500)
BackgroundColor = (117,80,123)
initialPosition = {
    'monster': Position((0,0)),
    'ghost': Position((100,10))
}

pygame.init()

screen = pygame.display.set_mode(ScreenResolution)

ghost = Ghost(initialPosition['ghost'], screen)
monster = Monster(initialPosition['monster'],screen)

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

end = False

while not end:
    screen.fill(BackgroundColor)

    # Game settings
    pygame.display.set_caption("Mounsters")  

    # Dynamic elements

    # Events Manager
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveLeft = True
            if event.key == pygame.K_RIGHT:
                moveRight = True
            if event.key == pygame.K_UP:
                moveUp = True
            if event.key == pygame.K_DOWN:
                moveDown = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveLeft = False
            if event.key == pygame.K_RIGHT:
                moveRight = False
            if event.key == pygame.K_UP:
                moveUp = False
            if event.key == pygame.K_DOWN:
                moveDown = False              

    # Efectuar movimientos
    if moveLeft:
        ghost.position.setX(ghost.position.getCoordinates()[0]-1)
    elif moveRight:
        ghost.position.setX(ghost.position.getCoordinates()[0]+1)
    elif moveUp:
        ghost.position.setY(ghost.position.getCoordinates()[1]-1)
    elif moveDown:
        ghost.position.setY(ghost.position.getCoordinates()[1]+1)

    ghost.draw()
    monster.draw()

    pygame.display.update()
