from pico2d import *
import random
import game_framework

class Bird:
    def __init__(self):
        self.image = load_image('bird_animation.png')
        self.x, self.y = random.randint(100, 1500), 400
        self.frame = random.randint(0,5)
        self.dir = 1
        self.need_frame = 5
        self.count = 1

    def update(self):
        if self.x + self.dir > 1570:
            self.dir = - 1
        elif self.x + self.dir < 30:
            self.dir = 1
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.need_frame
        if int(self.frame) == 0:
            if self.count == 1:
                self.count = 2
                self.need_frame = 5
            elif self.count == 2:
                self.count = 3
                self.need_frame = 5
            elif self.count == 3:
                self.count = 1
                self.need_frame = 4
        print(int(self.frame))



    def draw(self):
        if self.dir == -1:
            if self.count == 1:
                self.image.clip_composite_draw(int(self.frame) * 184, 0, 180, 165, 0 ,'h', self.x, self.y, 180, 165)
            if self.count == 2:
                self.image.clip_composite_draw(int(self.frame) * 184, 170, 180, 165, 0 ,'h', self.x, self.y, 180, 165)
            if self.count == 3:
                self.image.clip_composite_draw(int(self.frame) * 184, 340, 180, 165, 0 ,'h', self.x, self.y, 180, 165)

        elif self.dir == 1:
            if self.count == 1:
                self.image.clip_draw(int(self.frame) * 184, 0, 180, 165, self.x, self.y)
            elif self.count == 2:
                self.image.clip_draw(int(self.frame) * 184, 170, 180, 165, self.x, self.y)
            elif self.count == 3:
                self.image.clip_draw(int(self.frame) * 184, 340, 180, 165, self.x, self.y)



FRAMES_PER_ACTION = 8
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
PIXEL_PER_METER = 10/0.3
RUN_SPEED_KMPH = 20 # Km /h 마라토너의 평속
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000 / 60
RUN_SPEED_MPS = RUN_SPEED_MPM / 60
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER