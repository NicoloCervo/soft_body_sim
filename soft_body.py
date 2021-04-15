import numpy as np
import math
import itertools
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Node():

    def __init__(self, position = np.array([0, 0]), mass = 1, speed = np.array([0, 0]), force = np.array([0, 0])):
        self.position = position
        self.speed = speed
        self.force = force
        self.mass = mass
        self.lneighbor = None
        self.rneighbor = None
        
    def set_neighbors(left, right):
        self.lneighbor = left
        self.rneighbor = right

    def add_force(new_force):
        self.force += new_force
        

class SoftBody():
        
    def __init__(self, center = [0,0], radius = 2, segments = 10):

        self.segments = segments
        self.coordinates = []
        angle = 2 * math.pi / segments

        for i in range(segments):
            position = (radius * math.cos(i * angle), radius * math.sin(i * angle))
            node = Node(position = position)
            self.coordinates.append(node.position)

        return

    def get_coordinates(self):

        x, y = zip(*self.coordinates)
        return x, y

    def calc_area(self):

        area=0
        for vertex in range(self.segments):
            area += abs(self.nodes[vertex].position[0] * self.nodes[vertex + 1].position[1] 
                - self.nodes[vertex + 1].position[0] * self.nodes[vertex].position[1])
        return area/2

    def update_pressure(self):
        return

    def update_tension(self):
        return

    def update_gravity(self):
        return

    def update_position(self):
        return

if __name__ == '__main__':
    b=SoftBody()



