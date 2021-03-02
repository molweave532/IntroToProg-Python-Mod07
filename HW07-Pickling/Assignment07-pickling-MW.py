# ------------------------------------------------- #
# Title: HW07 - pickling
# Description: A brief description of pickling
# ChangeLog: (Who, When, What)
# Molly Weaver, 02/28/21, Created Script
# ------------------------------------------------- #

# import pickle module
import pickle

# create a simple dictionary
dicScores = {"Reign": "100", "Leo": "67", "Hank": "82"}

# pickle it - write to a binary file
filePickle = open("pickledScores.pkl", "wb")
pickle.dump(dicScores, filePickle)
filePickle.close()

# unpickle it - read from a binary file
fileUnpickle = open("pickledScores.pkl", "rb")
dicScoresP = pickle.load(fileUnpickle)
fileUnpickle.close()

# print the dictionary
print(dicScoresP)
