import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


def countHeadlineLength(features, target):
    fakeLen = np.array([])
    realLen = np.array([])
    for index, value in target.items():
        # print("Index: {}, Value: {}".format(index, value))
        if(value == 1):
            fakeLen = np.append(fakeLen, len(features.headline.loc[index]))
        else:
            realLen = np.append(realLen, len(features.headline.loc[index]))
        # print(features.headline.loc[index])
    print(np.mean(fakeLen))
    print(np.max(fakeLen))
    print(np.min(fakeLen))
    print(np.mean(realLen))
    print(np.max(realLen))
    print(np.min(realLen))
    plotHeadlineLength(fakeLen, realLen)


def plotHeadlineLength(fake, real):
    dataFake = pd.DataFrame(fake)
    dataReal = pd.DataFrame(real)
    sns.set(style='darkgrid')
    ax = sns.boxplot(data=dataFake, orient="h")
    ax.set(xlabel='Headline Length', ylabel='', title="Fake Headline Length")
    plt.savefig('fakeHeadlineLength.png')
    plt.show()
    bx = sns.boxplot(data=dataReal, orient="h")
    bx.set(xlabel='Headline Length', ylabel='', title="Real Headline Length")
    plt.savefig('realHeadlineLength.png')
    plt.show()
