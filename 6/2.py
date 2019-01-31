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


now = Point(10, 20)
print("[SEOJI] now: " + str(now.get()))

now.move(10, 20)
print("[SEOJI] first move x(10), y(20) -> " + str(now.get()))

now.setx(1)
print("[SEOJI] now: " + str(now.get()))

now.sety(1)
print("[SEOJI] now: " + str(now.get()))
