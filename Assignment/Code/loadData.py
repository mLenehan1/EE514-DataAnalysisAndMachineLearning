import json
import pandas as pd
from pandas.io.json import json_normalize


def loadJson(jsonFile, printMsgs=False):
    jsonInput = pd.read_json(jsonFile, lines=True)
    if(printMsgs == True):
        print(jsonInput.head())
        print("Shape:", jsonInput.shape)
        print("\nFeatures:", jsonInput.columns)
    return jsonInput


def splitFeaturesAndTargets(data, printMsgs=False):
    x = data[data.columns[1:]]
    y = data[data.columns[0]]
    if(printMsgs == True):
        print("Feature Matrix:", x.head())
        print("\nResponse Vector", y.head())
    return x, y


def countRealFake(targetTrainSet, targetTestSet):
    print("Real Headlines in Training Set: %s" % sum(targetTrainSet == 0))
    print("Fake Headlines in Training Set: %s" % sum(targetTrainSet == 1))
    print("Real Headlines in Test Set: %s" % sum(targetTestSet == 0))
    print("Fake Headlines in Test Set: %s" % sum(targetTestSet == 1))
