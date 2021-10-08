#
# Example file for parsing and processing JSON
# LinkedIn Learning Python course by Joe Marini
#


import urllib.request  # instead of urllib2 like in Python 2.7
import json


def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    # now we can access the contents of the JSON like any other Python object
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    # output the number of events, plus the magnitude and each event name
    count = theJSON["metadata"]["count"]
    print(str(count) + " events recorded")

    # for each event, print the place where it occurred
    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("--------------\n")

    # print the events that only have a magnitude greater than 4
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
    print("--------------\n")

    # print only the events where at least 1 person reported feeling something
    print("\n\nEvents that were felt:")
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if (feltReports != None):
            if (feltReports > 0):
                print("%2.1f" % i["properties"]["mag"], i["properties"]
                      ["place"], " reported " + str(feltReports) + " times")


def main():
    # define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # Open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))
    if (webUrl.getcode() == 200):
        data = webUrl.read().decode("utf-8")
        # print out our customized results
        printResults(data)
    else:
        print("Received an error from server, cannot retrieve results " +
              str(webUrl.getcode()))


if __name__ == "__main__":
    main()
