class Robot:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def act(self):
        print("Hello my name is "+self.name)

robo=robot("R2D2","White")
robo.act()
