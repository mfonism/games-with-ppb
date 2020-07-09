import ppb


class Cart(ppb.Sprite):

    def on_update(self, update_event, signal):
        self.position = ppb.Vector(0, 0)


def setup(scene):
    scene.add(Cart(pos=(0, 0)))


ppb.run(setup=setup)
