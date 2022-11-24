import random
from pico2d import *
import game_world
import server

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.x = random.randint(10, 1600 - 10)
        self.y = random.randint(10, 1000 - 10)
        self.draw_x = 0
        self.draw_y = 0


    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if 500<server.boy.x< 1330:
            self.x -= server.boy.move_x
        if 500 < server.boy.y < 600:
            self.y -= server.boy.move_y


    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, other, group):
        print('ball disappear')
        if group == 'boy:ball':
            game_world.remove_object(self)