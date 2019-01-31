class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def get(self):
        ret = (self.x, self.y)
        return ret

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
