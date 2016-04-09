from pprint import pprint
import re, sys, urllib, json, requests

url = "http://api.watttime.org/api/v1/datapoints/?ba="+sys.argv[1]+"&page_size=1000&freq=5m"

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

def fill_out_json(row):

    fields = ["genmix_thermal_gen_MW", "genmix_solar_gen_MW", "genmix_renewable_gen_MW", "genmix_biomass_gen_MW",
              "genmix_oil_gen_MW","genmix_wind_gen_MW", "genmix_nonwind_gen_MW", "genmix_refuse_gen_MW", "genmix_biogas_gen_MW",
             "genmix_nuclear_gen_MW","genmix_other_gen_MW", "genmix_natgas_gen_MW", "genmix_hydro_gen_MW", "genmix_coal_gen_MW",
             "ba", "url", "timestamp", "created_at", "carbon", "freq", "market"]

    fieldsPresent = row.keys()
    missingFields = [field for field in fields if field not in fieldsPresent]
    extraneousFields = [field for field in fieldsPresent if field not in fields]

    for field in missingFields:
        row[field] = "0"
    for field in extraneousFields:
        row.pop(field)
    for field in row:
	if row[field] == "None":
		row[field] = "0"
    return row

def url_to_flat_json(url):
    dbFriendlyJson = {}
    dbFriendlyJson["results"] = []
    urlPage = requests.get(url, headers={'Authorization': 'Token 277f1557ca7358e9ce76467ca708f7fe9a4b387d'})
    data = urlPage.json()

    try:
        for row in data["results"]:
            flatJson=flatten_json(row)
            flatJson = fill_out_json(flatJson)
            dbFriendlyJson["results"].append(flatJson)
    except:
        pass

    return {"nextUrl": data["next"], "json": dbFriendlyJson}

def extract_entire_dataset(url):
    with open(sys.argv[1]+'_energy_data.json', 'w') as f:
        while (url):
            myJson = url_to_flat_json(url)
            url = myJson["nextUrl"]
            for row in myJson["json"]["results"]:
                f.write(json.dumps(row) + '\n')

extract_entire_dataset(url)
