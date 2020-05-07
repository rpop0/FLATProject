def getHighestRating(reviewData, category):
    maxValue = 0

    for i in reviewData:
        if float(i[category]) > maxValue:
            maxValue = float(i[category])
    return maxValue


def getLowestRating(reviewData, category):
    minValue = 5
    for i in reviewData:
        if float(i[category]) <= minValue:
            minValue = float(i[category])
    return minValue


def getAverage(reviewData, category):
    average = 0
    divideAverage = 0
    for i in reviewData:
        average = average + float(i[category])
        divideAverage += 1
    average = round(average / divideAverage, 2)
    return average


def getMedian(reviewData, category):
    sortedReviews = []
    for i in reviewData:
        sortedReviews.append(float(i[category]))
    sortedReviews = sorted(sortedReviews)
    middlePoint = len(sortedReviews) // 2
    # Compute median
    return round((sortedReviews[middlePoint - 1] + sortedReviews[middlePoint + 1]) / 2, 2)


def getReviewsBetween(reviewData, category, lowerLimit, upperLimit):
    counter = 0

    for i in reviewData:
        if lowerLimit < float(i[category]) < upperLimit:
            counter += 1
    return counter
