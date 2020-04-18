import csv


def modify():
    newHeader = ["ID", "Art Galleries", "Dance Clubs", "Juice Bars", "Restaurants", "Museums", "Resorts", "Parks",
                 "Beaches", "Theathers", "Religious"]
    with open("data/tripadvisor_review.csv", "r") as csvfile:
        csvReader = csv.reader(csvfile)
        next(csvReader)
        with open("data/modified_reviews.csv", "w") as newFile:
            csvWriter = csv.writer(newFile)
            csvWriter.writerow(newHeader)
            for line in csvReader:
                csvWriter.writerow(line)
