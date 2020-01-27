import json
import pandas as pd
from pandas.io.json import json_normalize


def exportTestTrain(X_train, X_test, y_train, y_test, printMsgs=False):
    Export = X_train.to_json(r'./XTrain.json', orient='records')
    Export = X_test.to_json(r'./XTest.json', orient='records')
    Export = y_train.to_json(r'./YTrain.json', orient='records')
    Export = y_test.to_json(r'./YTest.json', orient='records')
    if(printMsgs == True):
        print("Training Features output to XTrain.json")
        print("Test Features output to XTest.json")
        print("Training Targets output to YTrain.json")
        print("Test Targets output to YTest.json")
