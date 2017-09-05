"""Main file for perceptron."""


def PrintStuff():
    """Print stuff."""
    print("number of samples: {}".format(len(data)))
    print("training data length: {}".format(len(trainingData)))
    print("dimensions: {}".format(dimension))


def AdjustWeights(point):
    """Adjust the weights according to misclassification."""
    for x in range(0, dimension):
        weights[x] += swing * point[x] * point[dimension]
    weights[dimension] += swing * point[dimension]


def ClassificationMatch(point):
    """Apply the algorithm to the point supplied."""
    threshold = 0
    for x in range(0, dimension):
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
    trials = 0
    while(errorRate != 0 and trials < 10):
        errors = 0
        trials += 1
        for x in trainingData:
            if (not ClassificationMatch(x)):
                errors += 1
                AdjustWeights(x)
        errorRate = float(errors)/len(trainingData)


def TestPerceptron():
    """Test the competency of the perceptron."""
    errors = 0
    for x in data:
        if(not ClassificationMatch(x)):
            errors += 1
    print("Total error rate: {}".format(float(errors)/len(data)))


# Begin procedures & initialize data
with open("data.txt") as f:
    data = []
    for line in f:
        data.append([int(x) for x in line.split()])
dimension = len(data[0]) - 1
trainingData = data[0:len(data)/2]
swing = .1
weights = []
for x in range(0, dimension + 1):
    weights.append(0)
PrintStuff()
TrainData()
TestPerceptron()
