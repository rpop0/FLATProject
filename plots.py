import matplotlib.pyplot as plt
import computations


def sortReviews(reviewDict):
    reviewsSorted = {k: v for k, v in sorted(reviewDict.items(), key=lambda item: item[1])}
    return reviewsSorted


def plot_bar(sortedReviewDict, title):
    x = [x for x in sortedReviewDict.keys()]
    y = [x for x in sortedReviewDict.values()]
    for i in range(len(x)):
        x[i] = f"{x[i]}\n{str(y[i])}"
    plt.style.use("seaborn-whitegrid")
    plt.barh(x, y)
    plt.title(title)
    plt.tight_layout()
    plt.show()


class FLATPlot:
    def __init__(self, reviewData):
        self.reviewData = reviewData
        self.reviewDataKeys = self.formatReviewData(reviewData)

    def formatReviewData(self, reviewData):
        reviewDataKeys = [key for key in self.reviewData[0].keys()]
        reviewDataKeys = reviewDataKeys[1:]
        return reviewDataKeys

    def plotHighest(self):
        highestReviews = dict()
        for key in self.reviewDataKeys:
            highestReviews[key] = computations.getHighestRating(self.reviewData, key)
        highestReviewsSorted = sortReviews(highestReviews)
        plot_bar(highestReviewsSorted, "Highest rating of each category")

    def plotLowest(self):
        lowestReviews = dict()
        for key in self.reviewDataKeys:
            lowestReviews[key] = computations.getLowestRating(self.reviewData, key)
        lowestReviewsSorted = sortReviews(lowestReviews)
        plot_bar(lowestReviewsSorted, "Lowest rating of each category")

    def plotAverage(self):
        averageReviews = dict()
        for key in self.reviewDataKeys:
            averageReviews[key] = computations.getAverage(self.reviewData, key)
        averageReviewsSorted = sortReviews(averageReviews)
        plot_bar(averageReviewsSorted, "Average of each category")

    def plotMedian(self):
        medianReviews = dict()
        for key in self.reviewDataKeys:
            medianReviews[key] = computations.getMedian(self.reviewData, key)
        averageReviewsSorted = sortReviews(medianReviews)
        plot_bar(averageReviewsSorted, "Median of each category")

    def plotGetReviewsBetween(self, lowerLimit, upperLimit):
        reviews = dict()
        for key in self.reviewDataKeys:
            reviews[key] = computations.getReviewsBetween(self.reviewData, key, lowerLimit, upperLimit)
        reviewsSorted = sortReviews(reviews)
        plot_bar(reviewsSorted, "Number of reviews between " + str(lowerLimit) + " and " + str(upperLimit))
