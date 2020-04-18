def getHighestRating(reviewData, category):
    max = 0
    for i in reviewData:
        if float(i[category]) > max:
            max = float(i[category])
    return max