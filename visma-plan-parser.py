## The libraries
from bs4 import BeautifulSoup
import re
import sys
import json
import array

## Args
if sys.argv[1] == "-v" or sys.argv[1] == "--version":
    print ("v1.1")
    sys.exit()

## The init data
if str(sys.argv[2]) != "":
    doc = open(str(sys.argv[2]), "r")
    print ("Using: " + sys.argv[2])
else:
    doc = open("Startside - Visma InSchool.htm", "r")
soup = BeautifulSoup(doc.read(), 'html.parser')
day = soup.findAll("div", {"class": "Timetable-TimetableDays_day"})

days = ["monday", "thuesday", "wednesday", "thursday", "friday"]


## Generates a basic HTML website
def makeWeb(fileName):
    finalWebsite = ""

    i = 0
    if len(day) > 0:
        for d in day:
            #finalWebsite += str(days[i] + str(d) + "</br></br></br></br>" + "\n")
            i += 1
            finalWebsite += '<p style="margin: 0;">' + str(days[i - 1]) + "</p>\n"

            elements = d.findAll("div", {"class": "Timetable-TimetableItem Timetable-TimetableItem-m"})
            #finalWebsite += str(len(elements))
            for e in elements:
                #finalWebsite += str(e) + "."
                #e.find("div", {"class": "Timetable-TimetableItem-subtitle"})

                clock = str(e.findAll("small")[0])[:-9][-13:]

                className = e.find("p")

                cleanr = re.compile('<.*?>')

                classCodeTag = e.find("small", {"class": "Timetable-TimetableItem-subtitle"})
                classCode = re.sub(cleanr, '', str(classCodeTag))[:-1][1:]

                classTypeTag = e.find("small", {"class": "Timetable-TimetableItem-type"})
                classType = re.sub(cleanr, '', str(classTypeTag))[:-1][1:]

                finalWebsite += clock + "\n" + str(className.text) + "\n" + classCode + "\n" + classType + "\n" + "</br></br>" + "\n\n"

            finalWebsite += "</br></br></br></br> \n\n\n\n"

    #return finalWebsite

    file = open(fileName, 'w')
    file.write(finalWebsite)
    file.close()

## Makes an array type file
def makeArray(type, fileName):
    plan = []

    i = 0
    if len(day) > 0:
        ## Loop for each day
        for d in day:
            i += 1
            dayArray = [str(days[i - 1])]

            elements = d.findAll("div", {"class": "Timetable-TimetableItem Timetable-TimetableItem-m"})
            for e in elements:
                clock = str(e.findAll("small")[0])[:-9][-13:]

                className = e.find("p")

                cleanr = re.compile('<.*?>')

                classCodeTag = e.find("small", {"class": "Timetable-TimetableItem-subtitle"})
                classCode = re.sub(cleanr, '', str(classCodeTag))[:-1][1:]

                classTypeTag = e.find("small", {"class": "Timetable-TimetableItem-type"})
                classType = re.sub(cleanr, '', str(classTypeTag))[:-1][1:]

                elementsArray = [clock, str(className.text), classCode, classType]

                dayArray.append(elementsArray)
            plan.append(dayArray)

    file = open(fileName, 'w')
    file.write(json.dumps(plan, indent=2))
    file.close()


## Checks if a name is given
if sys.argv[3] != "":
    ## The main
    if sys.argv[1] == "web":
        makeWeb(sys.argv[3])
    elif sys.argv[1] == "json":
        makeArray("JSON", sys.argv[3])
else:
    ## The main
    if sys.argv[1] == "web":
        makeWeb("plan.html")
    elif sys.argv[1] == "json":
        makeArray("JSON", "plan.json")
