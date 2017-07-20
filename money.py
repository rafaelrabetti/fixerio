import urllib, json, datetime, operator
from datetime import timedelta
from datetime import datetime

# getting the date within the url so we can work with it
api = "http://api.fixer.io/";
start_date = '2009-08-07';
base = "?base=USD";
stop_date = '2011-11-17';
url = api + start_date + base;

# valeus from the first and last day so we can make the final calculations
value_start_date = 1.8344
value_stop_date = 1.7804

# creating a date variable from the date string so we can iterate through the days
start = datetime.strptime(start_date, "%Y-%m-%d")
stop = datetime.strptime(stop_date, "%Y-%m-%d")

# dictionay to storage values and dates
d = {}
# variable to sum the values
aux = 0
# variable to count how many values
count = 0
# loop that gets the value for a date inside the json through the url
while start <= stop:
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        start = start + timedelta(days=1)
        # creates a string from the date to build the new url
        url = api + start.strftime("%Y-%m-%d") + base
        d[data['date']] = data['rates']['BRL']
        aux = aux + float(data['rates']['BRL'])
        count = count + 1

# gets the date where the values are maximum and minimum in the dictionary
max_value = max(d.iteritems(), key=operator.itemgetter(1))[0]
min_value = min(d.iteritems(), key=operator.itemgetter(1))[0]

media = (float(aux) - value_start_date - value_stop_date)/(count-2)
media_string = "{:.4f}".format(media)

print "Data do menor valor observado: " + min_value
print "Data do maior valor observado: " + max_value
print "Media de cotacao para o periodo excetuando os dias de inicio e fim: " + media_string
