import requests

ba=[]
baCount = {}
url = "https://api.watttime.org:443/api/v1/balancing_authorities/"
urlPage = requests.get(url, headers={'Authorization': 'Token 277f1557ca7358e9ce76467ca708f7fe9a4b387d'})
data = urlPage.json()

for row in data:
    url = "http://api.watttime.org/api/v1/datapoints/?ba=" + row["abbrev"] + "&page_size=1000"
    urlPage = requests.get(url, headers={'Authorization': 'Token 277f1557ca7358e9ce76467ca708f7fe9a4b387d'})
    data = urlPage.json()
    baCount[row["abbrev"].encode("utf-8")] = data["count"]

with open("Balancing_authority_data_count.txt","w") as f:
    for k, v in baCount.items():
        f.write(k+": "+str(v) + "\n")

