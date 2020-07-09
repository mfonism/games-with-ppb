import ppb
from ppb import keycodes


class UnitDirection:
    NONE = ppb.Vector(0, 0)
    LEFT = ppb.Vector(-1, 0)
    RIGHT = ppb.Vector(1, 0)


class Cart(ppb.Sprite):
    speed = 0
    direction = UnitDirection.NONE
    size = 2.5

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.position = ppb.Vector(0, -8)

    def on_update(self, update_event, signal):
        self.position += self.speed * update_event.time_delta * self.direction

    def on_key_pressed(self, key_event, signal):
        if key_event.key is keycodes.Left:
            self.speed = 4
            self.direction = UnitDirection.LEFT
        elif key_event.key is keycodes.Right:
            self.speed = 4
            self.direction = UnitDirection.RIGHT
        elif key_event.key is keycodes.Space:
            self.speed = 0
            self.direction = UnitDirection.NONE
        else:
            pass


def setup(scene):
    scene.add(Cart(pos=(0, 0)))


ppb.run(setup=setup)
