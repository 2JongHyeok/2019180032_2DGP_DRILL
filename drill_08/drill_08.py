from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 824

def running_right ():
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    pass
def running_left ():
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    pass


def handle_events():
    global running
    global dir
    global x
    global way
    global up
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                way = 1
            elif event.key == SDLK_LEFT:
                dir -= 1
                way = 0
            elif event.key == SDLK_UP:
                up += 1
            elif event.key == SDLK_DOWN:
                up -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                way = 1
            elif event.key == SDLK_LEFT:
                dir += 1
                way = 0
            elif event.key == SDLK_UP:
                up -= 1
            elif event.key == SDLK_DOWN:
                up += 1
    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
frame = 0
dir = 0
way = 1
up = 0
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if way == 1:
        running_right()
    else:
        running_left()
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    if x <= KPU_WIDTH - 10 and x >= 10:
        x += dir*5
    elif x >= KPU_WIDTH - 10:
        x = KPU_WIDTH - 5
    elif x <= 10:
        x = 15
    if y <= KPU_HEIGHT - 20 and y >= 20:
        y += up * 5
    elif y >= KPU_HEIGHT - 20:
        y = KPU_HEIGHT - 15
    elif y <= 20:
        y = 25
    delay(0.01)

close_canvas()

