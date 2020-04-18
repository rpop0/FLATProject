import matplotlib.pyplot as plt
import computations


def plotHighestReviews(reviewData):
    reviewDataKeys = [key for key in reviewData[0].keys()]
    reviewDataKeys = reviewDataKeys[1:]
    highestReviews = dict()

    for key in reviewDataKeys:
        highestReviews[key] = computations.getHighestRating(reviewData, key)

    highestReviewsSorted = {k: v for k, v in sorted(highestReviews.items(), key=lambda item: item[1])}
    print(highestReviewsSorted)
    plt.barh([x for x in highestReviewsSorted.keys()], [x for x in highestReviewsSorted.values()])
    plt.title("Highest rating of each category")
    plt.tight_layout()
    plt.show()





