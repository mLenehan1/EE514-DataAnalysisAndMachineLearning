def square(x):
    return x**2

class Particle(object):
    """
    This class models a particle with a name and a speed.
    """

    def __init__(self, name, speed=1):
        self.name = name
        self.speed = speed
    
    def speed_up(self):
        self.speed += 1.0

    def slow_down(self):
        self.speed -=1.0

class BetterParticle(Particle):
    """
    Like a Particle, but knows how to convert itself to a string!
    """

    def __str__(self):
        return '{} with speed {}'.format(self.name, self.speed)