import random
import time

import ppb
from ppb import keycodes


class UnitDirection:
    NONE = ppb.Vector(0, 0)
    LEFT = ppb.Vector(-1, 0)
    RIGHT = ppb.Vector(1, 0)
    UP = ppb.Vector(0, 1)
    DOWN = ppb.Vector(0, -1)


class Cart(ppb.RectangleSprite):
    position = ppb.Vector(0, -8)
    height = 2
    width = 6
    speed = 0
    direction = UnitDirection.NONE

    def on_update(self, update_event, signal):
        viewport = update_event.scene.main_camera
        if self.left <= viewport.left:
            self.direction = UnitDirection.RIGHT
        elif self.right >= viewport.right:
            self.direction = UnitDirection.LEFT
        self.position += self.speed * update_event.time_delta * self.direction

    def on_key_pressed(self, key_event, signal):
        if key_event.key is keycodes.Left:
            self.speed = 8
            self.direction = UnitDirection.LEFT
        elif key_event.key is keycodes.Right:
            self.speed = 8
            self.direction = UnitDirection.RIGHT
        elif key_event.key is keycodes.Space:
            self.speed = 0
            self.direction = UnitDirection.NONE
        else:
            pass


class Star(ppb.Sprite):
    last_caught = None
    last_missed = None

    def __init__(self, delay=0, perf_counter=None, **args):
        super().__init__(**args)
        self._delay = delay
        self._perf_counter = perf_counter or time.perf_counter()

    def is_born(self):
        return time.perf_counter() - self._perf_counter >= self._delay

    def on_scene_started(self, scene_event, signal):
        signal(ppb.events.PlaySound(ppb.Sound(name="intro.wav")))
        self.width = 1
        self.speed = 3
        self.direction = UnitDirection.DOWN
        far_left = scene_event.scene.main_camera.left
        far_right = scene_event.scene.main_camera.right
        top = scene_event.scene.main_camera.top
        rand_x = random.randrange(
            round(far_left + 2 * self.width), round(far_right + 1 - 2 * self.width)
        )
        self.position = ppb.Vector(rand_x, top + self.width)

    def on_update(self, update_event, signal):

        if not self.is_born():
            return

        self.position += self.speed * update_event.time_delta * self.direction
        cart = next(update_event.scene.get(kind=Cart, tags="cart"))

        if self.bottom > cart.top:
            return

        self.speed = 0
        self.direction = UnitDirection.NONE

        if cart.left <= self.position.x <= cart.right:
            # Hoorah! Cart in box.
            signal(ppb.events.PlaySound(ppb.Sound(name="ding.wav")))
            if self.__class__.last_caught is None:
                self.top_right = update_event.scene.main_camera.top_right
            else:
                self.top_right = self.__class__.last_caught.bottom_right

            self.__class__.last_caught = self
        else:
            # Oopsie! Missed that one!!
            signal(ppb.events.PlaySound(ppb.Sound(name="chord.wav")))
            self.image = ppb.Image(name="star--red.png")
            if self.__class__.last_missed is None:
                self.top_left = update_event.scene.main_camera.top_left
            else:
                self.top_left = self.__class__.last_missed.bottom_left

            self.__class__.last_missed = self


def setup(scene):
    scene.add(Cart(), tags=["cart"])
    pc = time.perf_counter()
    for i in range(1, 14):
        scene.add(Star(delay=i * 1.5, perf_counter=pc))


ppb.run(setup=setup)
