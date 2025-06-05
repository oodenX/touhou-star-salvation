from source.items import item_point

class PowerPoint(item_point.Item):
    def __init__(self):
        item_point.Item.__init__(self, 0)

    def update(self, surface, x, y):
        self.state = self.check(x, y)
        self.draw(surface)