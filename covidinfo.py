from urllib.request import urlopen
import requests
import json
def getCovid():
    html = urlopen("http://coronavirusapi.com/getTimeSeries/CA")
    stuff = html.read()
    # print (stuff.split("\n")[-12:])
    encoding = 'utf-8'
    stuff = stuff.decode('utf-8')
    print (type(stuff))
    ls = []
    niranjan = str(stuff).replace("\\n","break").replace(",","break")
    for x in niranjan.split("break")[-4:]:
        try:
            ls.append(int(x))
        except ValueError:
            pass
    print(ls[0])
    print(ls[1])
    print(ls[2])
getCovid()

def getStatePopulation(state):
    url = "https://datausa.io/api/data?drilldowns=State&measures=Population&year=latest"
    res = requests.get(url)
    data = res.json()
    thisdict = {
        "Alabama": "0",
        "Arizona": "1",
        "Arkansas": "2",
        "California": "3",
        "Colorado": "4",
        "5": "Connecticut",
        "6": "Delaware",
        "7": "Florida",
        "9": "Georgia",
        "10": "Hawaii",
        "11": "Idaho",
        "12": "Illinois",
        "13": "Indiana",
        "14": "Iowa",
        "15": "Kansas",
        "16": "Kentucky",
        "17": "Louisiana",
        "18": "Maine",
        "19": "Maryland",
        "20": "Massachusetts",
        "21": "Michigan",
        "22": "Minnesota",
        "23": "Mississippi",
        "24": "Missouri",
        "25": "Alaska",
        "26": "Nebraska",
        "27": "Nevada",
        "28": "New Hampshire",
        "29": "New Jersey",
        "30": "New Mexico",
        "31": "New York",
        "32": "South Carolina",
        "33": "North Dakota",
        "34": "Ohio",
        "35": "Oklahoma",
        "36": "Oregon",
        "37": "Pennsylvania",
        "38": "Rhode Island",
        "39": "South Carolina",
        "40": "South Dakota",
        "41": "Tennessee",
        "42": "Texas",
        "43": "Utah",
        "44": "Vermont",
        "45": "Virginia",
        "46": "Washington",
        "47": "West Virginia",
        "48": "Wisconsin",
        "49": "Wyoming"
    }


