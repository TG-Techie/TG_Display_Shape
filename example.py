from board import DISPLAY
from displayio import *
import display_shapes as shapes, time
size = 50
disp_grp = Group(max_size = 10)
background = shapes.rect(0,0,320,240,0)
disp_grp.append(shapes.rect(0, 0, size*2, size, shapes.color(255, 0, 0)))
disp_grp.append(shapes.roundrect(0, size, size*2, size, size//2, shapes.green))#HEY<-
disp_grp.append(shapes.roundrect(0, size*2, size*2, size, size//4, shapes.color(0, 0, 255)))
disp_grp.append(shapes.hline(5, size*3 + size//2, size*3, 4, shapes.white))
disp_grp.append(shapes.vline(size*3 + 5, 5, size*3, 4, shapes.color(200,196,50)))
disp_grp.append(shapes.circle(size *5, size *2, size, shapes.color(255, 0, 255)))

DISPLAY.show(disp_grp)


time.sleep(50)
