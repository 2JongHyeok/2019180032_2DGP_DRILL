from pico2d import *

def baby_up(x,y,frame):
    clear_canvas()
    map.draw(400,30)
    baby.clip_draw(frame*100,0,90,75,x,y)
    update_canvas()
    delay(0.1)
    
def baby_go(x,y,frame):
    clear_canvas()
    map.draw(400,30)
    if frame >=6:
        baby.clip_draw(frame%2*97,280,75,75,x,y)
    else:
        baby.clip_draw(frame*97,350,75,75,x,y)
    update_canvas()
    delay(0.1)

def baby_jump(x,y,frmae):
    clear_canvas()
    map.draw(400,30)
    baby.clip_draw(frame*97,0,75,75,x,y)
    update_canvas()
    delay(0.1)
    
def baby_stand(x,y,frame):
    clear_canvas()
    map.draw(400,30)
    baby.clip_draw(frame*97,425,75,75,x,y)
    update_canvas()
    delay(0.1)

def baby_fall(x,y,frame):
    clear_canvas()
    map.draw(400,30)
    if frame == 0:
        baby.clip_draw(97*5,140,75,75,x,y)
    else:
        baby.clip_draw((frame-1)*97,70,75,75,x,y)
    update_canvas()
    delay(0.1)

def baby_fight(x,y,frame):
    clear_canvas()
    map.draw(400,30)
    baby.clip_draw((frame+1)*97,140,100,75,x,y)
    update_canvas()
    delay(0.1)

def baby_roll(x,y,frame):
    clear_canvas()
    map.draw(400,30)
    if frame >= 17:
        baby.clip_draw((frame-17)*97,140,75,75,x,y)
    if frame >= 11:
        baby.clip_draw((frame-11)*97,210,75,75,x,y)
    elif frame >=5:
        baby.clip_draw((frame-5)*97,280,75,75,x,y)
    else:
        baby.clip_draw(frame*97,350,75,75,x,y)
    update_canvas()
    delay(0.1)



    
open_canvas()

map = load_image('grass.png')
baby = load_image('baby.png')

#close_canvas()
x = 100
frame = 0
y = 90
while (x<500):
    baby_go(x,y,frame)
    frame = (frame+1)%8
    x+=5
    get_events()
frame = 0
for i in range ( 0 , 50, 1):
    baby_stand(x,y,frame)
    frame = (frame+1)%6
frame = 0
while (y < 300 ):
    baby_up(x,y,frame)
    frame = (frame+1)%4
    y+=5
    get_events()
frame = 0
while(y > 90):
    baby_fall(x,y,frame)
    frame = (frame+1)%7
    if y == 120:
        frame = 6
    x-=30
    y-=30
    get_events()
baby_fall(x,y,frame)
baby_fall(x,y,frame)
baby_fall(x,y,frame)
baby_fall(x,y,frame)
baby_fall(x,y,frame)
frmae = 0
for i in range(0,36,1):
    baby_fight(x,y,frame)
    frame = (frame+1)%4
frame = 0

for i in range(0,36,1):
    baby_roll(x,y,frame)
    frame = (frame+1)%18
    x+=5
frame = 0
for i in range ( 0 , 50, 1):
    baby_stand(x,y,frame)
    frame = (frame+1)%6
        

close_canvas()


