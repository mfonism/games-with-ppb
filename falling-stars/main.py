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


class Star(ppb.RectangleSprite):
    position = ppb.Vector(0, 8)
    height = 1
    width = 1
    speed = 4
    direction = UnitDirection.DOWN

    def on_update(self, update_event, signal):
        cart = next(update_event.scene.get(kind=Cart, tags="cart"))
        if self.bottom > cart.top:
            self.position += self.speed * update_event.time_delta * self.direction
            return
        if (self.left > (cart.left - self.width)) and (
            self.right < (cart.right + self.width)
        ):
            # Hoorah! Star in cart!!
            update_event.scene.remove(self)
        else:
            # Oopsie! Missed that one!!
            self.position = update_event.scene.main_camera.top_right - ppb.Vector(
                self.size, self.size
            )
            self.speed = 0
            self.direction = UnitDirection.NONE


def setup(scene):
    scene.add(Cart(), tags=["cart"])
    scene.add(Star())


ppb.run(setup=setup)
