from urllib.request import urlopen

import requests


def getCovid(state):
    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'American Samoa': 'AS',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of Columbia': 'DC',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Guam': 'GU',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Northern Mariana Islands': 'MP',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Puerto Rico': 'PR',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virgin Islands': 'VI',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'
    }
    if state in us_state_abbrev:
        state = us_state_abbrev[state]
        print(state)
    print("afadjfkjalfajfasl")
    html = urlopen(f"http://coronavirusapi.com/getTimeSeries/{state}")
    stuff = html.read()
    # print (stuff.split("\n")[-12:])
    encoding = 'utf-8'
    stuff = stuff.decode('utf-8')
    print(type(stuff))
    ls = []
    niranjan = str(stuff).replace("\\\\n", "break").replace(",", "break")
    for x in niranjan.split("break")[-4:]:
        try:
            ls.append(int(x))
        except ValueError:
            pass
    infected = ls[1]
    return infected



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
        "Connecticut": "5",
        "Delaware": "6",
        "Florida": "7",
        "Georgia": "9",
        "Hawaii": "10",
        "Idaho": "11",
        "Illinois": "12",
        "Indiana": "13",
        "Iowa": "14",
        "Kansas": "15",
        "Kentucky": "16",
        "Louisiana": "17",
        "Maine": "18",
        "Maryland": "19",
        "Massachusetts": "20",
        "Michigan": "21",
        "Minnesota": "22",
        "Mississippi": "23",
        "Missouri": "24",
        "Alaska": "25",
        "Nebraska": "26",
        "Nevada": "27",
        "New Hampshire": "28",
        "New Jersey": "29",
        "New Mexico": "30",
        "New York": "31",
        "North Carolina": "32",
        "North Dakota": "33",
        "Ohio": "34",
        "Oklahoma": "35",
        "Oregon": "36",
        "Pennsylvania": "37",
        "Rhode Island": "38",
        "South Carolina": "39",
        "South Dakota": "40",
        "Tennessee": "41",
        "Texas": "42",
        "Utah": "43",
        "Vermont": "44",
        "Virginia": "45",
        "Washington": "46",
        "West Virginia": "47",
        "Wisconsin": "48",
        "Wyoming": "49",
    }
    if state in list(thisdict):  # if state in dict
        c = "huh"
        a = int(thisdict[state])
        #c = data['data'][str(a)]['Population']
        for d in data["data"]:
            if d["State"] == state:
                try:
                    c = d["Population"]
                    break
                except:
                    print("bruh")

        return c
    else:
        print("hey, you sure you typed the state currectly? It has to be capitalized! ex: North Dakota")

