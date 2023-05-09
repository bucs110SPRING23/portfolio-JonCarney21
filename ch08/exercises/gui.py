class Enemy:
    def __initi__(self, num=2):
        self.enemy_num = num
        self.lives = 1
        self.speed = 3
        self.size = 2
        self.hitbox = 1

class Block:
    def __initi__(self):
       self.hit = 1
       self.destroy = False
       self.powerup = False
       self.nextblock = 1
       self.x = 10
       self.y = 10

class Mario:
    def __initi__(self, pnum=1):
        self.Mario = pnum
        self.lives = 3
        self.is_large = False
        self.speed = 4

class Words:
    def __init__(self):
        self.font = None
        self.size = 5
        self.color = "white"
        self.position = (40,40)