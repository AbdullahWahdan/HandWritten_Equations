import pygame as pg

# pip install pygame==2.0.0.

"""
With this program you can draw on the 
screen with pygame


pythonprogramming.altervista.org
"""


def init():
    global screen
    pg.init()
    screen = pg.display.set_mode((1216, 416))
    mainloop()


drawing = False
last_pos = None
w = 1
color = (255, 0, 255)


def draw(event):
    global drawing, last_pos, w

    if event.type == pg.MOUSEMOTION:
        if (drawing):
            mouse_position = pg.mouse.get_pos()
            if last_pos is not None:
                pg.draw.line(screen, color, last_pos, mouse_position, w)
            last_pos = mouse_position
    elif event.type == pg.MOUSEBUTTONUP:
        mouse_position = (0, 0)
        drawing = False
        last_pos = None
    elif event.type == pg.MOUSEBUTTONDOWN:
        drawing = True


def mainloop(img_name="Image"):
    global screen

    loop = 1
    while loop:
        # checks every user interaction in this list
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.image.save(screen, img_name)
                loop = 0
	
            draw(event)
        pg.display.flip()
    pg.quit()

