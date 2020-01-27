from sklearn.feature_extraction.text import CountVectorizer
from yellowbrick.text import FreqDistVisualizer
import seaborn as sns
from matplotlib import pyplot as plt


def bagOfWords(featureTrain, stopWords=False, countWords=False, plot=False):
    if(stopWords == False):
        count_vect = CountVectorizer()
    else:
        count_vect = CountVectorizer(stop_words='english')
    X_train_counts = count_vect.fit_transform(featureTrain.headline)

    if countWords:
        features = count_vect.get_feature_names()
        visualizer = FreqDistVisualizer(features=features, n=20, orient='v')
        visualizer.fit(X_train_counts)
        words = countTopWords(X_train_counts, count_vect, 20)
        if stopWords:
            visualizer.show(outpath="SWRemovedYB")
            visualizer.show()
            plotBagOfWords("Stop Words Removed", words, 20, stopWords)
        else:
            visualizer.show(outpath="SWIncludedYB")
            visualizer.show()
            plotBagOfWords("Stop Words Included", words, 20, stopWords)
    return count_vect, X_train_counts


def countTopWords(featureTrainCounts, count_vect, n):
    sum_words = featureTrainCounts.sum(axis=0)
    words_freq = [(word, sum_words[0, idx])
                  for word, idx in count_vect.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    return words_freq


def plotBagOfWords(plotTitle, data, n, stopWords):
    sns.set(style="darkgrid")
    x = []
    y = []
    for N in range(n):
        x += [data[N][0]]
        y += [data[N][1]]
        # print(x)
        # print(y)
    ax = sns.barplot(x=y, y=x, color="blue")
    ax.set(xlabel='Frequency', ylabel='Word', title=plotTitle)
    if stopWords:
        plt.savefig('stopWordsRemoved.png')
    else:
        plt.savefig('stopWordsIncluded.png')
    plt.show()
