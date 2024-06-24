import requests

from collections import Counter


class Breweries():

    def __init__(self, new_york, maine, alaska):
        self.new_york = new_york
        self.maine = maine
        self.alaska = alaska

    def get_json_data_from_urls(self):
        try:
            response1 = requests.get(self.new_york)
            response2 = requests.get(self.maine)
            response3 = requests.get(self.alaska)
            response1.raise_for_status()
            response2.raise_for_status()
            response3.raise_for_status()
            return response1.json(), response2.json(), response3.json()
        except requests.exceptions.RequestException as e:
            print("Error fetching data: ", e)
            return None


beer = Breweries("https://api.openbrewerydb.org/v1/breweries?by_state=new_york",
                 "https://api.openbrewerydb.org/v1/breweries?by_state=maine",
                 "https://api.openbrewerydb.org/v1/breweries?by_state=alaska")

new_york, maine, alaska = beer.get_json_data_from_urls()

data = [new_york, maine, alaska]

list_of_all = []
for i in data:
    for v in i:
        list_of_all.append(v['name'])

print("The list of all breweries present in all the 3 states are: ", list_of_all)

nos = []

for i in data:
    count = 0
    for v in i:
        count += 1
    nos.append(count)

print("\nThe total no of breweries present in each of the 3 states are: ", nos)

type_of_brewery = []

for i in data:
    for v in i:
        type_of_brewery.append(v["brewery_type"])

x = Counter(type_of_brewery)

print("\nThe count and the list of breweries present are: ", x)

