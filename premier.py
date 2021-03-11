import requests
import json
import string

def search_name(name):
    response = requests.get("https://pro-premier-inn.emergyalabs.com/v1/autocomplete?input=/" + name + "&gplaces%5Bcomponents%5D=country:uk")
    a = json.loads(response.text)
    return [x for x in a["properties"] if x["brand"] == "PI"]


premierinns = {}
for c1 in string.ascii_lowercase:
    for c2 in string.ascii_lowercase:
        results = search_name(c1 + c2)
        print(c1 + c2)
        if len(results) > 0:
            for c3 in string.ascii_lowercase:
                results = search_name(c1 + c2 + c3)
                for result in results:
                    premierinns[result["suggestion"]] = result["geometry"]["coordinates"]

print(premierinns)
