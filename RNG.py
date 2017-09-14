"""Random data set generator."""
import random

dimension = 2
sampleSize = 50
with open('data.txt', 'w') as data:
    for y in range(sampleSize):
        for x in range(dimension):
            data.write("{} ".format(random.random()))
        data.write("{}\n".format(random.choice([1, -1])))
