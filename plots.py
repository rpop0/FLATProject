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
    x = [x for x in highestReviewsSorted.keys()]
    y = [x for x in highestReviewsSorted.values()]
    plt.style.use("seaborn-whitegrid")
    plt.barh(x, y)
    plt.title("Highest rating of each category")
    plt.tight_layout()

    for i, v in enumerate(y):
        plt.text(0.15, i-0.12, str(v), fontweight="bold", color="white")


    plt.show()


def plotLowestReviews(reviewData):
    reviewDataKeys = [key for key in reviewData[0].keys()]
    reviewDataKeys = reviewDataKeys[1:]
    lowestReviews = dict()

    for key in reviewDataKeys:
        lowestReviews[key] = computations.getLowestRating(reviewData, key)

    lowestReviewsSorted = {k: v for k, v in sorted(lowestReviews.items(), key=lambda item: item[1])}
    print(lowestReviewsSorted)
    plt.barh([x for x in lowestReviewsSorted.keys()], [x for x in lowestReviewsSorted.values()])
    plt.title("Lowest rating of each category")
    plt.tight_layout()
    plt.show()
