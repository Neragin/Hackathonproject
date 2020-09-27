from urllib.request import urlopen
html = urlopen("http://coronavirusapi.com/getTimeSeries/CA")
stuff = html.read()
# print (stuff.split("\n")[-12:])
encoding = 'utf-8'
stuff = stuff.decode('utf-8')
print (type(stuff))
print (stuff.split("\n")[-1:])
