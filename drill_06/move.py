from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

i = 1

x = 400
y = 90
while True:
    if i == 1:
      while (x<780):
          clear_canvas_now()
          grass.draw_now(400,30)
          character.draw_now(x,y)
          x+=2
          delay(0.01)
      while (y<580):
          clear_canvas_now()
          grass.draw_now(400,30)
          character.draw_now(x,y)
          y+=2
          delay(0.01)
      while (x>0):
          clear_canvas_now()
          grass.draw_now(400,30)
          character.draw_now(x,y)
          x-=2
          delay(0.01)
      while (y>90):
          clear_canvas_now()
          grass.draw_now(400,30)
          character.draw_now(x,y)
          y-=2
          delay(0.01)
      while (x<400):
          clear_canvas_now()
          grass.draw_now(400,30)
          character.draw_now(x,y)
          x+=2
          delay(0.01)
      i = 0
    else:
        while (y<510):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(int(x),y)
            y+=2
            x = 400 -(210**2 - (300 - y) ** 2) ** (1/2)
            delay(0.01)
        while (y > 90):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(int(x),y)
            y-=2
            x = 400 +(210**2 - (300 - y) ** 2) ** (1/2)
            delay(0.01)
        i = 1
close_canvas()
