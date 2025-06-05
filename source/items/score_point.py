from source.items import item_point

class ScorePoint(item_point.Item):
    def __init__(self):
        item_point.Item.__init__(self, 16)

    def update(self, surface, x, y):
        self.state = self.check(x, y)
        self.draw(surface)