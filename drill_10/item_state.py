import pico2d
from pico2d import *
import game_framework
import play_state
import title_state


image = None

def enter():
    global image
    image = load_image('add_delete_boy.png')

def exit():
    global image
    del image

def update():
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400,300)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_a:
                    play_state.team.append(play_state.Boy())
                    game_framework.pop_state()
                case pico2d.SDLK_MINUS:
                    if len(play_state.team) > 1:
                        play_state.team.pop()
                    game_framework.pop_state()





