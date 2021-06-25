##
## Image-Compressor-python-
## File description:
## K-means
##

from PIL.Image import *
from random import randint
from math import sqrt

class K_means :
    def __init__(self, filePath, nb, convergence):
        str = filePath.split('.') 
        self.filePath = str[0]
        self.image = open(filePath)
        self.nb_cluster = nb
        self.convergence = convergence
        self.pixels =  []
        self.clusters = []
        self.pixels_cluster = []
        self.init_pixels()
        self.init_cluster()
        self.prev_cluster = []
        
    def init_cluster(self) :
        for i in range(self.nb_cluster) :
            self.clusters.append(self.pixels[randint(0, len(self.pixels))][1])
            self.pixels_cluster.append([])
    
    def init_pixels(self) :
        self.pixels = []
        (width, height) = self.image.size
        for x in range(width):
            for y in range(height) :
                self.pixels.append(((x,y), self.image.getpixel((x,y))))
    
    def start(self) :
        condition = False
        while (condition != True) :
            self.prev_cluster = self.clusters[:]
            self.calculate_cluster()
            self.calculate_new_cluster()
            condition = self.try_convergence()

    def cal_euclidean_distance (self, value1, value2) :
       return (sqrt(((value1[0] - value2[0]) ** 2) + ((value1[1] - value2[1]) ** 2) + ((value1[2] - value2[2]) ** 2)))

    def calculate_cluster(self) :
        for cluster in self.pixels_cluster :
            cluster.clear()
        for pixel in self.pixels :
            last_value = 10000000
            pos_cluster = (0, 0, 0)
            for cluster in self.clusters :
                value = self.cal_euclidean_distance(pixel[1], cluster)
                if (value <= last_value) :
                    last_value = value
                    pos_cluster = cluster
            self.pixels_cluster[self.clusters.index(pos_cluster)].append(pixel)
            
    def calculate_new_cluster(self) :
        for i in range(self.nb_cluster) :
            moyenne = (0.0, 0.0, 0.0)
            for cluster in self.pixels_cluster[i] :
                moyenne = ((moyenne[0] + cluster[1][0]), (moyenne[1] + cluster[1][1]),(moyenne[2] + cluster[1][2]))
            size = len(self.pixels_cluster[i])
            self.clusters[i] = (int(moyenne[0] / size) , int(moyenne[1] / size), int(moyenne[2] / size))
                        
    
    def try_convergence(self):
        pos = 0
        for cluster in self.clusters :
            cal = self.cal_euclidean_distance(cluster , self.prev_cluster[pos])
            if (cal > self.convergence) :
                return False
            pos += 1
        return True
    
    def transform(self) :
        index = 0
        for cluster in self.pixels_cluster:
            for pos in cluster :
                self.image.putpixel(pos[0],self.clusters[index])
            index += 1
        self.image.save(self.filePath + "_compressing.jpg", "JPEG")
