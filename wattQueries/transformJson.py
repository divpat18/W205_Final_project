from pprint import pprint
import re, urllib.request, json

url = "http://api.watttime.org/api/v1/datapoints/?ba=MISO&authorization=277f1557ca7358e9ce76467ca708f7fe9a4b387d"

def prettyPrintObject(someObject):
    pprint(vars(someObject))

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                if type(a) is dict and "fuel" in a:
                    flatten(a,name+a["fuel"]+"_")
                else:
                    flatten(a, name + str(i) + '_')
                    i += 1
        else:
            out[str(name[:-1])] = str(x)

    flatten(y)
    return out


def url_to_flat_json(url):
    dbFriendlyJson = {}
    dbFriendlyJson["results"] = []
    with urllib.request.urlopen(url) as url:
        response = url.read()

    data = json.loads(response.decode("utf-8"))

    for row in data["results"]:
        flatJson=flatten_json(row)
        dbFriendlyJson["results"].append(flatJson)

    return dbFriendlyJson


url_to_flat_json(url)
