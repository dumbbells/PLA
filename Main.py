"""Main file for perceptron."""
import matplotlib.pyplot as plt


def PrintStuff():
    """Print stuff."""
    print("number of samples: {}".format(len(data)))
    print("training data length: {}".format(len(trainingData)))
    print("dimensions: {}".format(dimension))


def PrintWeights():
    """Print the weights."""
    print("Current weights: {}".format(weights))


def AdjustWeights(point):
    """Adjust the weights according to misclassification."""
    for x in range(dimension):
        weights[x] += swing * point[x] * point[dimension]
    weights[dimension] += swing * point[dimension]


def ClassificationMatch(point):
    """Apply the algorithm to the point supplied."""
    threshold = 0
    for x in range(dimension):
        threshold += point[x] * weights[x]
    threshold += weights[dimension]
    if (threshold > 0 and point[dimension] == 1):
        return True
    elif (threshold <= 0 and point[dimension] == -1):
        return True
    else:
        return False


def TrainData():
    """Train the data based on what was read in from the file."""
    errorRate = 1.0
    epochs = 0
    trainingErrors = 0
    list(reversed(trainingData))
    while(errorRate != 0 and epochs < 1000):
        errors = 0
        epochs += 1
        for x in trainingData:
            if (not ClassificationMatch(x)):
                trainingErrors += 1
                errors += 1
                AdjustWeights(x)
        errorRate = float(errors)/len(trainingData)
    print("Training Errors = {}".format(trainingErrors))
    print("Epochs = {}".format(epochs))


def TestPerceptron():
    """Test the competency of the perceptron."""
    errors = 0
    for x in data:
        if(not ClassificationMatch(x)):
            plt.plot(x[0], x[1], 'ro')
            errors += 1
        else:
            plt.plot(x[0], x[1], 'bo')
    print("Total error rate: {}".format(float(errors)/len(data)))


# Begin procedures & initialize data
with open("data.txt") as file:
    data = []
    for line in file:
        data.append([float(x) for x in line.split()])
dimension = len(data[0]) - 1
trainingData = data[0:20]
data = data[20:len(data)]
swing = 1
weights = []
for x in range(dimension + 1):
    weights.append(0)
PrintStuff()
TestPerceptron()
TrainData()
PrintWeights()
TestPerceptron()
p1 = [0, -weights[2]/weights[0]]
p2 = [-weights[2]/weights[1], 0]
print("x and y intercept after training {} {}".format(p1, p2))
plt.plot(p1, p2)
plt.show()
