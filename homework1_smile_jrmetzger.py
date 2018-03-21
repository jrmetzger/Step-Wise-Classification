# Jonathan Metzger
# CS453x Jacob Whitehill
# March 20th 2018


import numpy as np
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import itertools

# Taken from lecture 1 fPC
def fPC (y, yhat):
    if (len(y)==len(yhat)):
        return float(sum(1 for i in range(len(y)) if y[i] == yhat[i]))/ len(y)
    else:
        print "** ERROR: cannot proceed - y and yhat do not match up **"

# This takes a long time... 3 hours?
def stepwiseRegression (trainingFaces, trainingLabels, testingFaces, testingLabels):
    m = 5
    pixels = list(itertools.product(range(24), range(24)))
    tests = []
    
    while len(tests) < m:
        new_test = None
        new_test_accuracy = None

        # find pixel 1 and pixel 2 in set
        for pixel_1 in pixels:
            
            for pixel_2 in pixels:
                
                if pixel_1 == pixel_2: continue
                c1, r1 = pixel_1
                c2, r2 = pixel_2

                # constraints
                test_smile_results = [
                    1 if face[c1][r1] > face[c2][r2] else 0
                    for face in trainingFaces
                ]
                
                for test in tests:
                    predicted_c1, predicted_r1, predicted_c2, predicted_r2 = test
                    
                    for i in range(len(trainingFaces)):
                        test_smile_results[i] *= 1 if trainingFaces[i][predicted_c1][predicted_r1] > trainingFaces[i][predicted_c2][predicted_r2] else 0
                
                accuracy = fPC(trainingLabels, test_smile_results)
                
                if accuracy > new_test_accuracy:
                    new_test_accuracy = accuracy
                    new_test = (c1, r1, c2, r2)

                    percent_complete = float(1000*new_test[0] + 100*new_test[1] + 10*new_test[2] + new_test[3] ) / float(1000*23 + 100*23 + 10*23 + 23) * 200
                    print("Found best: %s\t Accuracy: %.2f%%\t Progress: %.2f%%\n" % (new_test, new_test_accuracy * 100, percent_complete))
        
        tests.append(new_test)
        print("Found best for m = %d\n", len(tests))
        print(tests)
        print("%d%\n",new_test_accuracy * 100)
        print

    # Here with all tests calculated
    print("Learned Things")
    print(tests)
    training_set_results = [1 for face in trainingFaces]
    
    for test in tests:
        
        for i in range(len(trainingFaces)):
            predicted_c1, predicted_r1, predicted_c2, predicted_r2 = test
            training_set_results[i] *= 1 if trainingFaces[i][predicted_c1][predicted_r1] > trainingFaces[i][predicted_c2][predicted_r2] else 0
    
    print("Accuracy on training set: %.3f\n" % fPC(trainingLabels, training_set_results))

    # Do it on testing
    testing_set_results = [1 for face in testingFaces]
    
    for test in tests:
        for i in range(len(testingFaces)):
            predicted_c1, predicted_r1, predicted_c2, predicted_r2 = test
            testing_set_results[i] *= 1 if testingFaces[i][predicted_c1][predicted_r1] > testingFaces[i][predicted_c2][predicted_r2] else 0
    
    print("Accuracy on testing set: %.3f\n" % fPC(testingLabels, testing_set_results))

    show = False
    if show:
        # Show an arbitrary test image in grayscale
        im = testingFaces[0,:,:]
        fig,ax = plt.subplots(1)
        ax.imshow(im, cmap='gray')
        # Show r1,c1
        rect = patches.Rectangle((c1,r1),1,1,linewidth=2,edgecolor='r',facecolor='none')
        ax.add_patch(rect)
        # Show r2,c2
        rect = patches.Rectangle((c2,r2),1,1,linewidth=2,edgecolor='b',facecolor='none')
        ax.add_patch(rect)
        # Display the merged result
        plt.show()

# load the data from .npy
def loadData (which):
    faces = np.load("{}ingFaces.npy".format(which))
    faces = faces.reshape(-1, 24, 24)  # Reshape from 576 to 24x24
    
    labels = np.load("{}ingLabels.npy".format(which))
    return faces, labels

if __name__ == "__main__":
    print("\nJonathan Metzger\nHomework1b\nCS453x Machine Learning\n")
    testingFaces, testingLabels = loadData("test")
    trainingFaces, trainingLabels = loadData("train")
    stepwiseRegression(trainingFaces, trainingLabels, testingFaces, testingLabels)
