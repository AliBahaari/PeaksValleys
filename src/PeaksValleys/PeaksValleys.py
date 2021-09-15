# Modules

import pandas as pd, itertools, random


# Detect Peaks and Valleys

def detectPeaksValleys(dataframeSeries, rollingNumber, averageSize):


    # Moving Average List

    movingAverageChart = dataframeSeries.rolling(rollingNumber).mean()
    movingAverageChart.dropna(inplace=True)
    movingAverageList = movingAverageChart.to_list()


    # Find Peaks & Vallies

    peaks = []
    valleys = []

    for i, obj in enumerate(movingAverageList):

        if i >= (averageSize - 1) and i <= (len(movingAverageList) - 1 - (averageSize - 1)):

            front = movingAverageList[i : (i + averageSize)]
            back = movingAverageList[(i - (averageSize - 1)) : (i + 1)]

            if (obj > sum(back) / len(back)) and (obj > sum(front) / len(front)):
                peaks.append((i , obj))

            if (obj < sum(back) / len(back)) and (obj < sum(front) / len(front)):
                valleys.append((i , obj))


    # Find Maxs & Mins

    maxPeaks = []
    minValleys = []

    for k, group in itertools.groupby(enumerate(peaks), key=lambda x: x[0] - x[1][0]):
        maxPeaks.append(max([(val, id) for idx, (id, val) in list(group)]))

    for k, group in itertools.groupby(enumerate(valleys), key=lambda x: x[0] - x[1][0]):
        minValleys.append(min([(val, id) for idx, (id, val) in list(group)]))

    return [maxPeaks, minValleys]